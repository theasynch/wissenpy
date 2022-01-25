import discord
import random
from discord import Spotify
from PIL import Image, ImageFont, ImageDraw
import io
from discord.ext import commands
import asyncio
import textwrap
from util import clean_code, Pag
from traceback import format_exception
import contextlib

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name = 'remind', aliases = ['rm', 'remindme', 'timer'])
    async def remind(self, ctx, time, *, task = None,):
        x = random.randrange(2)
        if x == 1:
            await ctx.send("Pro tip!!: \n> Invite my brother to your server!! He is very cool and you surely be impressed https://bit.ly/callistobot")
        if task == None:
            task = "something"
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2

            return val * time_dict[unit]

        converted_time = convert(time)

        if converted_time == -1:
            embed = discord.Embed(
                name="Error",
                description="> You did not enter the time correctly",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        if converted_time == -2:
            embed = discord.Embed(
                name="Error",
                description="> The time must be an integer",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        
        reminder_em = discord.Embed(
            name="Reminder Turned On",
            description=f"> Alright! I will remind you regarding `{task}` in **{time}**",
            color=0x00ff00,
        )
        await ctx.send(embed=reminder_em)
        await asyncio.sleep(converted_time)
        time_over = discord.Embed(
            title="__Reminder Notif__",
            description=f">>> Hey, you had asked me to remind about `{task}` {time} ago\n[Message link]({ctx.message.jump_url})",
            color = 0x00ff00,
        )

        await ctx.author.send(embed=time_over)


    @commands.command()
    async def ss(self, ctx, link):
        x = random.randrange(2)
        if x == 1:
            await ctx.send("Pro tip!!: \n> Invite my brother to your server!! He is very cool and you surely be impressed https://bit.ly/callistobot")
        embed = discord.Embed(title = "Website Screenshot for: {}".format(link))
        embed.set_image(
            url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{link}")

        await ctx.send(embed=embed)

    @commands.command()
    async def embed(self, ctx, title, description, color, image=None):
        x = random.randrange(2)
        if x == 1:
            await ctx.send("Pro tip!!: \n> Invite my brother to your server!! He is very cool and you surely be impressed <https://bit.ly/callistobot>")
        embed  = discord.Embed(title = title, description = description, color = int(color, 16))
        if image == None:
            pass
        else:
            embed.set_image(url = image)
        await ctx.send(embed=embed)

    @commands.command()    
    async def simple_interest(self, ctx, amt:int, time:int, rate:int):
        si = (amt*time*rate)/100
        total = si+amt
        embed = discord.Embed(
            title = "Simple Interest Calculator", 
            description = f"> The principle amount was: `{amt}`\n> The rate of interest was: `{rate}`\n> The time period was: `{time}`\nThe simple interest will be: {si}\n Similarly the total amount with interest will be: {total}",
            color = 0x00ff00
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def ci(self, ctx, amt:int, time:int, rate:int):
        Amount = amt * (pow((1 + rate / 100), time))
        CI = Amount - amt

        embed = discord.Embed(title = "")

    @commands.command(name="eval", aliases=["exec"])
    @commands.is_owner()
    async def _eval(self, ctx, *, code):
        code = clean_code(code)

        local_variables = {
            "discord": discord,
            "commands": commands,
            "bot": commands,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}\n"
        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        pager = Pag(
            timeout=100,
            entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
            length=1,
            prefix="```py\n",
            suffix="```"
        )

        await pager.start(ctx)







def setup(client):
    client.add_cog(Utilities(client))
