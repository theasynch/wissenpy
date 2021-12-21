import discord
import datetime
import os
from discord import message
from datetime import date
from discord.ext import tasks, commands
from itertools import cycle
from discord_components import *
import psutil


ts = 0
tm = 0
th = 0
td = 0
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='w?', intents=intents)
client.remove_command('help')
status = cycle(['Study Wars', 'for: w?help', 'Upcoming Exams', 'for: w?help', 'For Your Doubts',
               'for: w?help', 'Large Cardinal Project', 'for: w?help', 'For An Answer to Musks Question', 'for: w?help', 'you watching this :P', 'for: w?help'])

print(client)


@client.event
async def on_ready():
    DiscordComponents(client)
    change_status.start()
    uptimeCounter.start()


@tasks.loop(seconds=6)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

@tasks.loop(seconds=1)
async def uptimeCounter():
    global ts, tm, th, td
    ts += 2
    if ts ==  60:
        ts - 0
        tm = 1
        if tm == 60:
            tm = 0
            th += 1
            if th == 24:
                th = 0 
                td += 1

@uptimeCounter.before_loop
async def beforeuptimeCounter():
    await client.wait_until_ready()

@client.command()
async def stats(ctx):
    latency = round(client.latency, 2)
    guild = len(client.guilds)
    users = sum([len(guild.members) for guild in client.guilds])
    global ts, tm, th, td
    embed = discord.Embed(title='Stats from `Wissen`', color=0x4b33d3)
    embed.add_field(name = 'General Stats', value = f"```yaml\n Servers: {guild}\n Users: {users}\n Latency: {latency}\n Prefix: w? \n Client Version: v1.2.5\n Pycord Version: v1.7.3\n```",inline = False)
    embed.add_field(name = "Server Stats", value = f"```yaml\n OS: Windows\n CPU Usage: {psutil.cpu_percent()}%\n RAM Usage: {psutil.virtual_memory()[2]}%\n```")
    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    await client.process_commands(message)





@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def ping(ctx):
    await ctx.send('ping')


@client.command()
async def guilds(ctx):
    list = []
    for guild in client.guilds():
        list.append(guild)
        print(list)




# buttons array
buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]
# calculates answer


def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred.'
    return result


@ client.command(name='calc', aliases=['cula', 'lator'])
async def calc(ctx):
    m = await ctx.send(content='Loading Calculators...')
    expression = 'None'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'**{ctx.author.name}\'s** calculator | {ctx.author.id}', description=expression,
                      timestamp=delta)
    await m.edit(components=buttons, embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
                0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == 'None' or expression == 'An error occurred.':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed', type=7)
                break
            elif res.component.label == '←':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression = 'None'
            elif res.component.label == '=':
                expression = calculate(expression)
            else:
                expression += res.component.label
            f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression,
                              timestamp=delta)
            await res.respond(content='', embed=f, components=buttons, type=7)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

for filename in os.listdir('./cogs'):
    # Slicing the extension for cogs.py. so that the program can understand the language.
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODY5OTcwMzA2MjU5ODkwMTk2.YQF8_A.hcat303E4yFg5M5Dur8OHrJR474')
