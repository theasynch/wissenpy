import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
import os

# Extenstion COG for image-manipulation commands.


class Manipulation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        wanted = Image.open("wantedtemplate.png")

        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((256, 256))

        wanted.paste(profilepic, (542, 866))

        wanted.save("wantedpic.png")

        await ctx.send(file=discord.File("wantedpic.png"))
        os.remove("wantedpic.png")

    @commands.command()
    async def rip(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        rip = Image.open("riptemplate.png")

        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        text = member.display_name


        profilepic = profilepic.resize((125, 125))

        rip.paste(profilepic, (120, 355))

        rip.save("rippic.png")

        await ctx.send(file=discord.File("rippic.png"))
        os.remove("rippic.png")

    @commands.command(name='acheive', aliases=['achieve'])
    async def achievement(self, ctx, *, args):
        image = random.choice(range(40))
        text = ctx.message.content
        text = text[10: len(text)]
        text=text.replace(' ', "+")
        link = f"https://minecraftskinstealer.com/achievement/{image}/Achievement+Get%21/{text}"

        embed = discord.Embed(
        )
        embed.set_image(url = link)
        await ctx.send(embed=embed)

    @commands.command()
    async def balloon(self, ctx, arg1, arg2):
        balloon = Image.open("balloon.png")
        font = ImageFont.truetype('arial.ttf', 36)
        draw=ImageDraw.Draw(balloon)
        draw.text((95, 195), arg1, (0, 0, 0), font=font)
        draw.text((85,645), arg1, (0,0,0), font=font)
        draw.text((772,182), arg2, (0,0,0), font=font)

        balloon.save("balloone.png")
        await ctx.send(file=discord.File("balloone.png"))
        os.remove("balloone.png")

    @commands.command()
    async def armor(self, ctx,):
        img = Image.open("armor.png")
        test = ctx.message.content
        test = test[8:len(test)]
        font = ImageFont.truetype('arial.ttf', 24)
        #35,365
        draw=ImageDraw.Draw(img)
        draw.text((35,365), test, (0,0,0), font=font)
        img.save("armore.png")
        await ctx.send(file = discord.File("armore.png"))
        os.remove("armore.png")

        
def setup(client):
    client.add_cog(Manipulation(client))
