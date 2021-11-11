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
        if member == None and ctx.message.attachments == None:
            member = ctx.author
            asset = member.avatar_url_as()
        if ctx.message.attachments != None:
            asset = ctx.message.attachments
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)
        inverted = ImageOps.invert(profilepic)
        inverted.save('invert.jpg', quality=100)

        await ctx.channel.send(file = discord.File('invert.jpg'))
        os.remove('invert.jpg')

def setup(client):
    client.add_cog(Filters(client))
