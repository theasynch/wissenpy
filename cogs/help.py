import discord
import datetime
import random
from discord.ext import commands
from discord_components import *


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online 🔥')

    # commands
    
    
    @commands.group(name='help')
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
        embed.set_author(name="Wissen Help Manual", icon_url=user.avatar_url)
        embed.add_field(name='<:gearssolid:944436311220162580> Utility',
                        value='<:terminalsolid:944436738967896064> `w?help utility`', inline=True)
        embed.add_field(name='<:facelaughbeamregular:944436311123689503> Fun',
                        value='<:terminalsolid:944436738967896064> `w?help fun`', inline=True)
        embed.add_field(name='<:wandmagicsparklessolid:944436311148855336> Filters',
                        value=' <:terminalsolid:944436738967896064> `w?help filters`', inline=True)
        embed.add_field(name='<:imagessolid:944436310876225546> Image',
                        value='<:terminalsolid:944436738967896064> `w?help image`', inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="©Wissen 2021")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Example(client))
