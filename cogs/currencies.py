import discord
import json
import datetime
import random
import matplotlib.pyplot as plt
from matplotlib import style
from discord.ext import commands
import requests
from datetime import date, timedelta
import numpy as np

class Currencies(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='exchangerate', aliases=['exchange', 'ex'])
    async def exchangerate(self, ctx, base: str, *  symbol: str):


        today = date.today()

        api_end_date = today.strftime("%Y-%m-%d")	
        back_dates = date.today() + timedelta(days = -10)
        api_start_date = back_dates.strftime("%Y-%m-%d")


        url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={api_start_date}&end_date={api_end_date}&symbols={symbol}&base={base}"

        payload = {}
        headers = {
            "apikey": "8Vie58HFeLvuDBXoPxOIO4gEprAFTy0m"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.text
        exdata = json.loads(result)

        dates = exdata['rates']

        x = []
        for i in dates:
            x.append(i)
            
        y=[]
        for i in dates:
            y.append(dates[i]['INR'])

        plt.style.use('dark_background')
        plt.plot(x,y)
        plt.grid(axis = 'y')
        plt.ylabel('← Value →')
        plt.xlabel('← Time Line →')
        plt.savefig('sample.png')
        plt.close()

        embed = discord.Embed(title="Exchange Rate", description=f"Timeseries for excangerates between {base} and {symbol}", color=0x00ff00)
        embed.set_image(url = './sample.png')

        await ctx.send(embed=embed)


        

def setup(client):
    client.add_cog(Currencies(client))
