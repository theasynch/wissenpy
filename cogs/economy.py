import discord
from discord.ext import commands
import json
import os
import datetime
import random

os.chdir("C:\\Users\\HP Demo Machine\\Documents\\GitHub\\wissenpy\\cogs")
class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @commands.command()
    async def balance(self,ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = get_bank_data()
        users[str(user.id)] = {}
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        embed = discord.Embed(
            title=f"{ctx.author.name}'s Balance", color=0x9b870c, description = f"**Wallet** : {wallet_amt} \n **Bank** : {bank_amt}")
            embed.set_footer(text="💵")
            embed.timestamp = datetime.datetime.utcnow()  

    await ctx.send(embed=embed)

async def open_account(self,user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False

    else:
        users[str(user.id)]["wallet"] = 500
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users,f)
    return True


async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)
    return users
        
def setup(client):
    client.add_cog(Economy(client))
