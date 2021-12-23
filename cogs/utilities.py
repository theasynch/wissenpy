import discord
from discord import Spotify
from PIL import Image, ImageFont, ImageDraw
import requests
from discord.ext import commands
import asyncio
import string

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client





    @commands.command()
    async def afk(self,ctx, *, reason='No reason Provided'):
        member = ctx.author
        if member.id in afks.keys():
            afks[member.id] = "afk"

        else:
            try:
                member.edit(nick = f'[AFK]{member.display_name}')
            except:
                pass
        afks[member.id] =reason
        embed = discord.Embed(title = "Member is AFK", description = f'{member.mention} has gone AFK', color = member.color)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_author(name = self.client.name, icon_url = self.client.avatar_url)
        embed.add_field(name = 'AFK Note', value = reason)
        await ctx.send(embed=embed)

    @commands.command(name = 'remind', aliases = ['rm', 'remindme', 'timer'])
    async def remind(self, ctx, time, *, task = None,):
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
    async def caeser_cipher(self, ctx, text, shift, alphabets):
        def shift_alphabet(alphabet):
            return alphabet[shift:] + alphabet[:shift]

        shifted_alphabet = tuple(map(shift_alphabet, alphabets))
        final_alphabet = ''.join(alphabets)
        final_shifted_alphabet = ''.join(shifted_alphabet)
        table = str.maketrans(final_alphabet, final_shifted_alphabet)
        return text.translate(table)


    @commands.command()
    async def ss(self, ctx, link):
        embed = discord.Embed(title = "Website Screenshot for: {}".format(link))
        embed.set_image(
            url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{link}")

        await ctx.send(embed=embed)

    @commands.command()
    async def embed(self, ctx, title, description, color, image:None):
        embed  = discord.Embed(title = title, description = description, color = color)
        if image == None:
            pass
        for i in image:
            embed.set_image(url= image)
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Utilities(client))
