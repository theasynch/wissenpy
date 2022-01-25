import discord
import datetime
import random
from discord.ext import tasks, commands
from itertools import cycle
from discord_components import *
import psutil

ts = 0
tm = 0
th = 0
td = 0


class Technical(commands.Cog):

    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online 🔥')

    # commands
    
    
    @commands.command(name='help')
    async def help(self,ctx):
        colors = [0x340BFE, 0x2746E3, 0x2583B6, 0x24A19F,
                  0x39D47C, 0x52FB7C, 0x49FB76, 0x37FB68, 0x23FB59]
        random_colors = random.choice(colors)
        user = ctx.author
        embed = discord.Embed(
            description="[`Invite Me!`](https://discord.com/oauth2/authorize?client_id=869970306259890196&permissions=473295959&scope=bot) | [`Support Server`](https://discord.gg/TsM9uVc48y)",
            colour=random_colors
        )
        #embed.add_field
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="©Wissen 2021")
        await ctx.send(embed=embed)

    '''@commands.group(name='help')
    async def help(self, ctx):
        colors = [0x3408bfe, 0x2746E3, 0x2583B6, 0x24A19F, 0x39D47C, 0x52FB7C, 0x49FB76, 0x37FB68, 0x23FB59]
        random_colors = random.choice(colors)
        user = ctx.author
        embed = discord.Embed(
            description="[`Invite Me!`](https://discord.com/oauth2/authorize?client_id=869970306259890196&permissions=473295959&scope=bot) | [`Support Server`](https://discord.gg/TsM9uVc48y)",
            colour= random_colors
        )

        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="©Wissen 2021")
        await ctx.send(embed=embed, components = 
        [Select(placeholder = "Choose what you want to view.",
                            options = [
                                SelectOption(
                                    label = "Image Manipulation",
                                    value = "See the commands for Image Manipulation!",
                                    description = "See the commands for Image Manipulation!",
                                    emoji = "📸"
                                ),
                                SelectOption(
                                    label = "Utilities",
                                    value = "See the commands for Utilities!",
                                    description = "See the commands for Utilities!",
                                    emoji = "🔨"
                                ),
                                SelectOption(
                                    label = "Learning",
                                    value = "See the commands for helping you in Studying and Learning!",
                                    description = "See the commands for Utilities!",
                                    emoji = "📖"
                                ),
                            ])])

        e1 = discord.Embed(title = "Here are all the commands for Image Manipulation!",  color = 0xff4162) 
        e1.add_field(name = "__wanted__", value = "> Make someone wanted and place a price on their heads!", inline = False)
        e1.add_field(name = "__rip__ ", value = "> Kill someone peacefully. May he `Rest in peace`.")
        e2 = discord.Embed(title = "Here are all the commands for Utilities!", description = "Reminder \n > Why are you so clumsy, now I have to remind you every time 🤦🏻‍♂️ \n AFK \n > Why do you even turn on your device if you are going `A.F.K?!` (Releasing Soon! :P)", color = 0xff7F50)
        e3 = discord.Embed(title="Here are all the commands for Learning purposes!", description="Calculator \n > Dont even think to use it in exams >:( \n Convert \n Convert something sensible douchébag.")
        while True:
            try: # try except is not required but i would recommend using it
                event = await self.client.wait_for("select_option", check=None)

                label = event.component[0].label

                if label == "Image Manipulation":
                    await event.send(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True, # we dont want to spam someone
                        embed=e1
                    )

                elif label == "Utilities":
                    await event.send(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True, # we dont want to spam someone
                        embed=e2
                    )

                elif label == "Learning":
                    await event.send(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True, # we dont want to spam someone
                        embed=e3
                    )

            except discord.NotFound:
                print("error.")'''

    """@commands.group(pass_context=True, invoke_without_command=True)
    async def help(self, ctx):
        user = ctx.author
        embed = discord.Embed(
            description="Some Commands may not work properly as the bot is under development",
            colour=0x7170f0)

        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="©Wissen 2021")

        embed.add_field(
            name='<:SW_math:872117890239840318> __Mathematics__',
            value=" `w?calc` `w?formula` `w?convert` `w?thm` `w?qaudr` `w?mean` `w?mod` `w?median`",
            inline=False)

        embed.add_field(
            name='<:SW_phy:871974515066949692> __Physics__',
            value=" `w?acc` `w?f_vel` `w?i_vel` `w?disp` `w?dist` `w?work` `w?power` `w?energy` ",
            inline=False)

        embed.add_field(
            name='<:SW_chem:871612680937566288> __Chemistry__',
            value="`w?elem` `w?molality` `w?molarity` `w?`",
            inline=False)

        embed.add_field(
            name='<:SW_bio:871994645033418782> __Biology__',
            value="`w?classify` `w?disease`",
            inline=False)

        embed.add_field(
            name='<:SW_sst:871995926523297812> __Social Science__ ',
            value=" `w?whois` ",
            inline=False
        )

        embed.add_field(
            name='<:SW_eng:872126581370421318> __English__',
            value="HEllo"
        )

        await ctx.send(embed=embed)

    @help.command()
    async def calc(self, ctx):
        user = ctx.author
        embed = discord.Embed(
            title="`w?calc` command info",
            colour=0x202225
        )
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/872700901901627452/872733415189938226/Untitled_design_9_1.png')
        embed.set_footer(text="Usage Syntax: <required> [optional]")

        embed.add_field(
            name="Description:",
            value="Lazy to open calculator on your device? Use `w?calc`, to open up an interactive calculator and use that!",
            inline=False
        )

        embed.add_field(
            name="Aliases:",
            value="`calc` , `lator` , `cula`",
            inline=False
        )

        embed.add_field(
            name="Permissions Needed",
            value='`sendMessages`, `readMessageHistory`, `embedLinks`'

        )
        await ctx.send(embed=embed)"""

  
    @tasks.loop(seconds=1)
    async def uptimeCounter():
        global ts, tm, th, td
        ts += 2
        if ts == 60:
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


    @commands.command()
    async def stats(ctx):
        latency = round(client.latency, 2)
        guild = len(client.guilds)
        users = sum([len(guild.members) for guild in client.guilds])
        global ts, tm, th, td
        embed = discord.Embed(title='Stats from `Wissen`', color=0x4b33d3)
        embed.add_field(name='General Stats',
                        value=f"```yaml\n Servers: {guild}\n Users: {users}\n Latency: {latency}\n Prefix: w? \n Client Version: v1.2.5\n Pycord Version: v1.7.3\n```", inline=False)
        embed.add_field(name="Server Stats",
                        value=f"```yaml\n OS: Windows\n CPU Usage: {psutil.cpu_percent()}%\n RAM Usage: {psutil.virtual_memory()[2]}%\n```")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Technical(client))
