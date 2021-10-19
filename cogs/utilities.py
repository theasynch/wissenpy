import discord
from discord import Spotify
from PIL import Image, ImageFont, ImageDraw
import dateutil.parser
import requests
from discord.ext import commands
import asyncio

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
    async def spotify(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                await ctx.send(f"{user} is listening to {activity.title} by {activity.artist}")



    @commands.command()
    async def track(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.ActivityType.listening)), None)

        if spotify_result is None:
            await ctx.send(f'{user.name} is not listening to Spotify.')

        # Images
        track_background_image = Image.open('spotify_template.png')
        album_image = Image.open(requests.get(spotify_result.album_cover_url, stream=True).raw).convert('RGBA')

        # Fonts
        title_font = ImageFont.truetype('Spotify.ttf', 16)
        artist_font = ImageFont.truetype('Spotify.ttf', 14)
        album_font = ImageFont.truetype('Spotify.ttf', 14)
        start_duration_font = ImageFont.truetype('Spotify.ttf', 12)
        end_duration_font = ImageFont.truetype('Spotify.ttf', 12)

        # Positions
        title_text_position = 150, 30
        artist_text_position = 150, 60
        album_text_position = 150, 80
        start_duration_text_position = 150, 122
        end_duration_text_position = 515, 122

        # Draws
        draw_on_image = ImageDraw.Draw(track_background_image)
        draw_on_image.text(title_text_position,
                           spotify_result.title, 'white', font=title_font)
        draw_on_image.text(
            artist_text_position, f'by {spotify_result.artist}', 'white', font=artist_font)
        draw_on_image.text(album_text_position,
                           spotify_result.album, 'white', font=album_font)
        draw_on_image.text(start_duration_text_position,
                           '0:00', 'white', font=start_duration_font)
        draw_on_image.text(end_duration_text_position,
                           f"{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}",
                           'white', font=end_duration_font)

        # Background colour
        album_color = album_image.getpixel((250, 100))
        background_image_color = Image.new(
            'RGBA', track_background_image.size, album_color)
        background_image_color.paste(
            track_background_image, (0, 0), track_background_image)

        # Resize
        album_image_resize = album_image.resize((140, 160))
        background_image_color.paste(
            album_image_resize, (0, 0), album_image_resize)

        # Save image
        background_image_color.convert('RGB').save('spotify.jpg', 'JPEG')

        await ctx.send(file=discord.File('spotify.jpg'))






def setup(client):
    client.add_cog(Utilities(client))
