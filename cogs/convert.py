import discord
import datetime
import random
from discord.ext import commands

from discord_components import *

# A whole seperate COG for the mathematical command of convert.


class Convert(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def convert(self, ctx, num: int, unit: str):
        user = ctx.author
        if unit == "mm":
            cm = num/10
            decim = num/100
            mtr = num/1000
            decam = num/10000
            hectom = num/100000
            km = num/1000000
            mile = round(km/1.6, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Millimeters__**\n**{num} {unit}** `⇌`**{cm} cm**\n**{num} {unit}** `⇌`**{decim} deci.m**\n **{num} {unit}** `⇌`**{mtr} m**\n**{num} {unit}** `⇌`**{decam} deca.m**\n**{num} {unit}** `⇌`**{hectom} hecto.m**\n**{num} {unit}** `⇌`**{km} km**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{km} km** `⇌`**{mile} miles**',
                inline=False
            )
            await ctx.send(embed=embed)
        elif unit == "cm":
            mm = num*10
            decim = num/10
            mtr = num / 100
            decam = num/1000
            hectom = num/10000
            km = num / 100000
            mile = round(km/1.6, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Centimeters__**\n**{num} {unit}** `⇌`**{mm} mm**\n**{num} {unit}** `⇌`**{decim} deci.m**\n **{num} {unit}** `⇌`**{mtr} m**\n**{num} {unit}** `⇌`**{decam} deca.m**\n**{num} {unit}** `⇌`**{hectom} hecto.m**\n**{num} {unit}** `⇌`**{km} km**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{km} km** `⇌`**{mile} miles**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "decim":
            mm = num*100
            cm = num*10
            mtr = num/10
            decam = num/100
            hectom = num/1000
            km = num/10000
            mile = round(km/1.6, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Decimeters__**\n**{num} {unit}** `⇌`**{mm} mm**\n**{num} {unit}** `⇌`**{cm} cm**\n **{num} {unit}** `⇌`**{mtr} m**\n**{num} {unit}** `⇌`**{decam} deca.m**\n**{num} {unit}** `⇌`**{hectom} hecto.m**\n**{num} {unit}** `⇌`**{km} km**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{km} km** `⇌`**{mile} miles**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "m":
            mm = num*1000
            cm = num*100
            decim = num*10
            decam = num/10
            hectom = num/100
            km = num/1000
            mile = round(km/1.6, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Meters__**\n**{num} {unit}** `⇌`**{mm} mm**\n**{num} {unit}** `⇌`**{cm} cm**\n **{num} {unit}** `⇌`**{decim} deci.m**\n**{num} {unit}** `⇌`**{decam} deca.m**\n**{num} {unit}** `⇌`**{hectom} hecto.m**\n**{num} {unit}** `⇌`**{km} km**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{km} km** `⇌`**{mile} miles**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "decam":
            mm = num*10000
            cm = num*1000
            decim = num*100
            mtr = num*10
            hectom = num/10
            km = num/100
            mile = round(km/1.6, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Decameters__**\n**{num} {unit}** `⇌`**{mm} mm**\n**{num} {unit}** `⇌`**{cm} cm**\n **{num} {unit}** `⇌`**{decim} deci.m**\n**{num} {unit}** `⇌`**{mtr} m**\n**{num} {unit}** `⇌`**{hectom} hecto.m**\n**{num} {unit}** `⇌`**{km} km',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{km} km** `⇌`**{mile} miles**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "hectom":
            mm = num*100000
            cm = num*10000
            decim = num*1000
            mtr = num*100
            decam = num*10
            km = num/10
            mile = round(km/1.6, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Hectometeres__**\n**{num} {unit}** `⇌`**{mm} mm**\n**{num} {unit}** `⇌`**{cm} cm**\n **{num} {unit}** `⇌`**{decim} deci.m**\n**{num} {unit}** `⇌`**{mtr} m**\n**{num} {unit}** `⇌`**{decam} deca.m**\n**{num} {unit}** `⇌`**{km} km**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{km} km** `⇌`**{mile} miles**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "km":
            mm = num*1000000
            cm = num*100000
            decim = num*10000
            mtr = num*1000
            decam = num*100
            hectom = num*10
            mile = round(num/1.6, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Kilometers__**\n**{num} {unit}** `⇌`**{mm} mm**\n**{num} {unit}** `⇌`**{cm} cm**\n **{num} {unit}** `⇌`**{decim} deci.m**\n**{num} {unit}** `⇌`**{mtr} m**\n**{num} {unit}** `⇌`**{decam} deca.m**\n**{num} {unit}** `⇌`**{hectom} hecto.m**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{mile} miles**',
                inline=False
            )
            await ctx.send(embed=embed)

    # ----------------------------------------------------------------------------------------
        elif unit == "mg":
            cg = num/10
            decig = num/100
            gram = num/1000
            decag = num/10000
            hectog = num/100000
            kg = num/1000000
            pound = round(kg*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Milligrams__**\n**{num} {unit}** `⇌`**{cg} cg**\n**{num} {unit}** `⇌`**{decig} deci.g**\n **{num} {unit}** `⇌`**{gram} g**\n**{num} {unit}** `⇌`**{decag} deca.g**\n**{num} {unit}** `⇌`**{hectog} hecto.g**\n**{num} {unit}** `⇌`**{kg} kg**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kg} kg** `⇌`**{pound} lbs(pounds)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "cg":
            mg = num*10
            decig = num/10
            gram = num/100
            decag = num/1000
            hectog = num/10000
            kg = num/100000
            pound = round(kg*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Centigrams__**\n**{num} {unit}** `⇌`**{mg} mg**\n**{num} {unit}** `⇌`**{decig} deci.g**\n **{num} {unit}** `⇌`**{gram} g**\n**{num} {unit}** `⇌`**{decag} deca.g**\n**{num} {unit}** `⇌`**{hectog} hecto.g**\n**{num} {unit}** `⇌`**{kg} kg**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kg} kg** `⇌`**{pound} lbs(pounds)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "decig":
            mg = num*100
            cg = num*10
            gram = num/10
            decag = num/100
            hectog = num/1000
            kg = num/10000
            pound = round(kg*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Decigrams__**\n**{num} {unit}** `⇌`**{mg} mg**\n**{num} {unit}** `⇌`**{cg} cg**\n **{num} {unit}** `⇌`**{gram} g**\n**{num} {unit}** `⇌`**{decag} deca.g**\n**{num} {unit}** `⇌`**{hectog} hecto.g**\n**{num} {unit}** `⇌`**{kg} kg**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kg} kg** `⇌`**{pound} lbs(pounds)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "g" or unit == "gm":
            mg = num*1000
            cg = num*100
            decig = num*10
            decag = num/10
            hectog = num/100
            kg = num/1000
            pound = round(kg*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Grams__**\n**{num} {unit}** `⇌`**{mg} mg**\n**{num} {unit}** `⇌`**{cg} cg**\n **{num} {unit}** `⇌`**{decig} deci.g**\n**{num} {unit}** `⇌`**{decag} deca.g**\n**{num} {unit}** `⇌`**{hectog} hecto.g**\n**{num} {unit}** `⇌`**{kg} kg**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kg} kg** `⇌`**{pound} lbs(pounds)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "decag":
            mg = num*10000
            cg = num*1000
            decig = num*100
            g = num*10
            hectog = num/100
            kg = num/1000
            pound = round(kg*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Grams__**\n**{num} {unit}** `⇌`**{mg} mg**\n**{num} {unit}** `⇌`**{cg} cg**\n **{num} {unit}** `⇌`**{decig} deci.g**\n**{num} {unit}** `⇌`**{g} g**\n**{num} {unit}** `⇌`**{hectog} hecto.g**\n**{num} {unit}** `⇌`**{kg} kg**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kg} kg** `⇌`**{pound} lbs(pounds)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "hectog":
            mg = num*100000
            cg = num*10000
            decig = num*1000
            g = num*100
            decag = num*10
            kg = num/10
            pound = round(kg*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Grams__**\n**{num} {unit}** `⇌`**{mg} mg**\n**{num} {unit}** `⇌`**{cg} cg**\n **{num} {unit}** `⇌`**{decig} deci.g**\n**{num} {unit}** `⇌`**{g} g**\n**{num} {unit}** `⇌`**{decag} decag**\n**{num} {unit}** `⇌`**{kg} kg**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kg} kg** `⇌`**{pound} lbs(pounds)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "kg":
            mg = num*1000000
            cg = num*100000
            decig = num*10000
            g = num*1000
            decag = num*100
            hectog = num/10
            pound = round(num*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Grams__**\n**{num} {unit}** `⇌`**{mg} mg**\n**{num} {unit}** `⇌`**{cg} cg**\n **{num} {unit}** `⇌`**{decig} deci.g**\n**{num} {unit}** `⇌`**{g} g**\n**{num} {unit}** `⇌`**{decag} decag**\n**{num} {unit}** `⇌`**{hectog} hecto.g**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{pound} lbs(pounds)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "ml":
            cl = num/10
            decil = num/100
            litre = num/1000
            decal = num/10000
            hectol = num/100000
            kl = num/1000000
            pound = round(kl*2.2046, 10)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Millilitres__**\n**{num} {unit}** `⇌`**{cl} cl**\n**{num} {unit}** `⇌`**{decil} deci.l**\n **{num} {unit}** `⇌`**{litre} l**\n**{num} {unit}** `⇌`**{decal} deca.l**\n**{num} {unit}** `⇌`**{hectol} hecto.l**\n**{num} {unit}** `⇌`**{kl} kl**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kl} kl** `⇌`**{pound} oz(ounces)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "cl":
            ml = num*10
            decil = num/10
            litre = num/100
            decal = num/1000
            hectol = num/10000
            kl = num/100000
            pound = round(kl*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Centilitres__**\n**{num} {unit}** `⇌`**{ml} ml**\n**{num} {unit}** `⇌`**{decil} deci.l**\n **{num} {unit}** `⇌`**{litre} l**\n**{num} {unit}** `⇌`**{decal} deca.l**\n**{num} {unit}** `⇌`**{hectol} hecto.l**\n**{num} {unit}** `⇌`**{kl} kl**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kl} kl** `⇌`**{pound} oz(ounces)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "decil":
            ml = num*100
            cl = num*10
            litre = num/10
            decal = num/100
            hectol = num/1000
            kl = num/10000
            pound = round(kl*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Decilitres__**\n**{num} {unit}** `⇌`**{ml} ml**\n**{num} {unit}** `⇌`**{cl} cl**\n **{num} {unit}** `⇌`**{litre} l**\n**{num} {unit}** `⇌`**{decal} deca.l**\n**{num} {unit}** `⇌`**{hectol} hecto.l**\n**{num} {unit}** `⇌`**{kl} kl**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kl} kl** `⇌`**{pound} oz(ounces)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "l":
            ml = num*1000
            cl = num*100
            decil = num*10
            decal = num/10
            hectol = num/100
            kl = num/1000
            pound = round(kl*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from Litres__**\n**{num} {unit}** `⇌`**{ml} ml**\n**{num} {unit}** `⇌`**{cl} cl**\n **{num} {unit}** `⇌`**{decil} deci.l**\n**{num} {unit}** `⇌`**{decal} deca.l**\n**{num} {unit}** `⇌`**{hectol} hecto.l**\n**{num} {unit}** `⇌`**{kl} kl**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kl} kl** `⇌`**{pound} oz(ounces)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "decal":
            ml = num*10000
            cl = num*1000
            decil = num*100
            g = num*10
            hectol = num/100
            kl = num/1000
            pound = round(kl*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from decalitres__**\n**{num} {unit}** `⇌`**{ml} ml**\n**{num} {unit}** `⇌`**{cl} cl**\n **{num} {unit}** `⇌`**{decil} deci.l**\n**{num} {unit}** `⇌`**{g} g**\n**{num} {unit}** `⇌`**{hectol} hecto.l**\n**{num} {unit}** `⇌`**{kl} kl**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kl} kl** `⇌`**{pound} oz(ounces)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "hectol":
            ml = num*100000
            cl = num*10000
            decil = num*1000
            g = num*100
            decal = num*10
            kl = num/10
            pound = round(kl*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from hectolitres__**\n**{num} {unit}** `⇌`**{ml} ml**\n**{num} {unit}** `⇌`**{cl} cl**\n **{num} {unit}** `⇌`**{decil} deci.l**\n**{num} {unit}** `⇌`**{g} g**\n**{num} {unit}** `⇌`**{decal} decal**\n**{num} {unit}** `⇌`**{kl} kl**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{kl} kl** `⇌`**{pound} oz(ounces)**',
                inline=False
            )
            await ctx.send(embed=embed)

        elif unit == "kl":
            ml = num*1000000
            cl = num*100000
            decil = num*10000
            l = num*1000
            decal = num*100
            hectol = num/10
            pound = round(num*2.2046, 2)
            embed = discord.Embed(
                title="Conversion Result",
                description=f'**__Conversion from kilolitres__**\n**{num} {unit}** `⇌`**{ml} ml**\n**{num} {unit}** `⇌`**{cl} cl**\n **{num} {unit}** `⇌`**{decil} deci.l**\n**{num} {unit}** `⇌`**{l} l**\n**{num} {unit}** `⇌`**{decal} decal**\n**{num} {unit}** `⇌`**{hectol} hecto.l**',
                color=0x3ec9c1
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/871586814694146109/872699471144833064/pixel_rev.png')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="__Others:__",
                value=f'**{num} {unit}** `⇌`**{pound} oz(ounces)**',
                inline=False
            )
            await ctx.send(embed=embed)

        else:
            cant_convert = ["Hmmmm... Cant Convert",
                            "Sorry kiddo I cant convert it for ye",
                            "Looks like you are lost...",
                            "This is embarrassing but I guess I cant convert it ψ(._. )>",
                            "Woah! That is something I cant convert \🤔",
                            "The converter just crashed \😐",
                            "Error 404, No conversion possible :|",
                            "Beats the hell out of me, but something went wround 🥵",
                            "Waaiiiiittt a minute! What isss that? 👀",
                            "This is a completely armed and functional error ❌",
                            "Is it only me or is this error kinda **THICCCC**?"]

            embed = discord.Embed(
                title=random.choice(cant_convert),
                color=0xeb4034
            )
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/873239041716400128/873958217363914792/Pixel_Errir.png?width=499&height=499')
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="©Wissen 2021")
            embed.add_field(
                name="Try again by checking the following things:",
                value=f"`1.` Please check if the unit is correct.\n `2.`Make sure the magnitude is an integer (it should only contain numbers)",
                inline=False,
            )

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Convert(client))
