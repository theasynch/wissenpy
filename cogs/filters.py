import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
import os


class Filters(commands.Cog):

    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Filters(client))
