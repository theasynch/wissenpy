import discord
from discord.ext import tasks, commands
from afks import afks


def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class OnEvent(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick= remove(message.author.display_name))
            except:
                pass
            embed = discord.Embed(title = f"Welcome back{message.author.display_name}!", description = f"> Your [AFK] has been removed.")
            await message.channel.send(embed = embed)
        for id, reason in afks.items():
            member = discord.get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message.id)).author) or member.id in message.raw_mentions:
                embed = discord.Embed(title = "Member AFK", description = f"{member.name} is AFK \n `Note:` {reason}")
                await message.reply(embed = embed)

def setup(client):
    client.add_cog(OnEvent(client))
