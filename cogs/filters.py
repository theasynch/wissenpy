import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
import random
import os


class Filters(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invert(self, ctx, member: discord.Member = None):
        for img in ctx.message.attachments:
            image = img
        if member == None:
            member = ctx.author
            image = member.avatar_url_as()
        asset = image
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)
        inverted = ImageOps.invert(profilepic)
        inverted.save('invert.jpg', quality=100)

        await ctx.channel.send(file=discord.File('invert.jpg'))
        os.remove('invert.jpg')


    @commands.command()
    async def gay(self, ctx, member: discord.Member = None):
        mask_img = Image.open('lgbtq.png')
        mask_img.putalpha(0.5)
        if member == None:
            member = ctx.author
            bg_img = member.avatar_url_as()
        asset = bg_img
        data = BytesIO(await asset.read())
        bg_img = Image.open(data)

def setup(client):
    client.add_cog(Filters(client))
