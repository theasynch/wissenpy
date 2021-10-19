import discord
import random
import asyncio
from discord.ext.commands.core import check
from discord.ext import tasks, commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def say(self, ctx, *, args):
        quote = ctx.message.content
        quote = quote[6:len(quote)]
        user = ctx.author.display_name
        return await ctx.send(f'{quote}\n\n **- {user}**')


    @commands.command()
    async def clap(self, ctx):
        text = ctx.message.content
        text = text[7:len(text)]
        text = text.replace(' ', ' \👏🏻 ')
        await ctx.send(text)

    @commands.command()
    async def beeboo(self, ctx):
        text = ctx.message.content
        text = text[9:len(text)]
        text = text.replace(' ', " \💀\🎺 ")
        await ctx.send(text)

    @commands.command()
    async def leetify(self, ctx):
        text = ctx.message.content
        text = text[10:len(text)]
        text = text.lower()
        text = text.replace('a', "4")
        text = text.replace('b', "8")
        text = text.replace('e', "3")
        text = text.replace('g', "9")
        text = text.replace('i', "1")
        text = text.replace('s', "5")
        text = text.replace('t', "7")
        text = text.replace('z', "2")
        await ctx.send(text)

    @commands.command()
    async def greentext(self, ctx):
        text = ctx.message.content
        text = text[12:len(text)]
        text = f'```json\n"{text}"\n```'
        await ctx.send(text)


    @commands.command()
    async def kill(self, ctx, member: discord.Member = None):
        print("command logged")
        user = ctx.author
        if member == None or member == user:
            kill = ["Alright you commited suicide! Lets partyyy. Now choose someone else to kill...", 
                    f"BREAKING NEWS! We found {user.display_name} hanging itself on the fan. ||Choose someone else to kill 😒||",
                    f"{user.display_name} tried to shoot someone but ALAS! the bullet rebounded and pierced {user.display_name}'s heart...",
                    "Ok you are ded. Now choose someone else to kill",
                    "Do that again, but this time try to mention someone else. DUMBO!",
                    "You did not mention anyone to kill. wyd?",
                    "You did not choose anyone to kill, Are you ok?",
                    "Why did you even pick the gun, if you did not want to kill anyone??",
                    "You picked you the sword, but it was so heavy that you tripped and cut yourself in half, R.I.P",
                    "You were almost going to snipe, when a bullet went through you own head.",
                    "You made an action plan to kill someone, but, they saw it and used it upon you. Next time, pull your curtains.",
                    "Atleast tell me whom to kill! . _.",
                    "Pick a guy to kill, sweetie",
                    "Sorry but you did not mention to kill anyone.",
                    "You did not mention to kill anyone, what a waste typing.",]

            await ctx.reply(random.choice(kill))
        else:
            n = member.display_name
            kill = [f"{n} went on a ride with a lead balloon and eventually fell in the valley.",
                    f"{n} ate an apple but it turned out to be made of wax. Someone died of food poisoning later that day.",
                    f"{n} was squashed by a storm of cooked chicken.",
                    f"{user.display_name} threw a beam of frozen turkey at {n} killing them instantly.",
                    f"{user.display_name} tickled {n} to death :skull:",
                    f"{n} has a stroke after a sad miserable existence. They are then devoured by their ample cats.",
                    f"{user.display_name} cleaves the head of {n} with their keyboard.",
                    f"{n} died from doing the icebucket challenge.",
                    f"{n} filled up their humidifier with vodka and died of alcohol poisoning",
                    f"{user.display_name} turns on Goosebumps [2015] on the T.V, {n} being a scardy cat dies of an heart attack.",
                    f"{n} tried to get famous on YouTube by live-streaming something dumb. Skydiving while chained to a fridge.",
                    f"{user.display_name} murders {n} with `minecraft.stick` .",
                    f"{n} gets trampled under the feet of a baby elephant.",
                    f"{user.display_name} bamboozled {n} by killing them with a sharp card."
                    f"{user.display_name} made their dog chase behind {n}. {n} died of running for too long. SAD!",
                    f"{n} were trying to solve a rubik cube, but their fingers got chiseled... They died of shock.",
                    f"{n} were vaporised by an alien that came out from no-where.",
                    f"{n} stubbed thier pinky toe finger.",
                    f"{n} choked themselves with water. WHAT A SHAME!",
                    f"{n}'s brain was hacked by Neuralink.",
                    f"{n} listened to thier own recorded voice.",
                    f"{n} ate a lego by mistake.",
                    f"{n} picked up a grenade, thinking that it was a rotten apple.",
                    f"{n} tried to kick a dog, but fell down due to slippery ice, they died instantly. KARMA! Bitch",
                    f"{n} were slapped bruttally until they were roasted to death."]



            await ctx.send(random.choice(kill))

    @commands.command()
    async def toss(self, ctx):
        sides = ["+heads", "-tails"]
        side = random.choice(sides)
        await ctx.send(f"```diff\n{side}\n```")


    @commands.command()
    async def roll(self, ctx, num:int = None):
        try:
            if num == None:
                roll = random.randrange(1, 6)
                await ctx.send(f"Wissen rolls a die, and it is **{roll}**")
            else:
                roll = random.randrange(1, num)
                await ctx.send(f"Wissen rolls **{roll}**!")

        except:
            await ctx.send("Error, check if the number is an integer or not!")


    @commands . command()
    async def emojify(self, ctx, *, text):
        emojis = []
        for s in text. lower():
            if s. isdecimal():
                num2emo = {'0': 'zero', '1': 'one', '2': 'two',
                       '3': 'three', '4': 'four', '5': 'five',
                       '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

                emojis . append(f' :{num2emo . get (s)}: ')
            elif s. isalpha():
                emojis . append(f' :regional_indicator_{s}: ')
            else:
                emojis . append(s)
   
        await ctx . send(' '  . join(emojis))

    @commands.command()
    async def spin(self, ctx, color=None):
        time = random.randrange(1, 180)
        colors = ["blue", "green", "yellow", "orange", "stone", "cosmic", "glass", "mint", "pink", "purple", "red"]
        if color == None:
            embed = discord.Embed(
                name="Error", description="Please choose your desired color of fidget spinner. \n Type `w?help spin` for more.", color=0x2F3136)
            await ctx.send(embed=embed)
        if color not in colors:
            embed = discord.Embed(
                name="Error", description="Sorry but you have chosen a color that I dont like and it is not in my pallete try again.\n Type `w?help spin` for more.", color=0x2F3136)
            await ctx.send(embed=embed)
        if color == "red":
            await ctx.send(f"<:fidgetspinner48321:892655255437848656> You have spun the {color} spinner. Let us see for how long it spins! <:fidgetspinner48321:892655255437848656> ")
            await asyncio.sleep(time)
            await ctx.send(f"<:fidgetspinner48321:892655255437848656> {ctx.author.mention} Your {color} spinner spun for {time} seconds! <:fidgetspinner48321:892655255437848656>")
        if color == "blue":
            await ctx.send(f"<:fidgetspinner48321:892655255437848656> You have spun the {color} spinner. Let us see for how long it spins! <:fidgetspinner48321:892655255437848656> ")
            await asyncio.sleep(time)
            await ctx.send(f"<:fidgetspinner48321:892655255437848656> {ctx.author.mention} Your {color} spinner spun for {time} seconds! <:fidgetspinner48321:892655255437848656>")
    
    
    @commands.command()
    async def reverse(self, ctx, *, text):
        text = text[::-1]
        await ctx.send(text)


    @commands.command()
    async def mocker(self, ctx, *, text):
        test_str = text
        res = ""
        for idx in range(len(test_str)):
            if not idx % 2 :
                res = res + test_str[idx].upper()
            else:
                res = res + test_str[idx].lower()
        await ctx.send(res)

    @commands.command()
    async def strikethrough(self, ctx, *, text):
        text = f"~~{text}~~"
        await ctx.send(text)

    @commands.command()
    async def bold(self, ctx, *, text):
        text = f"**{text}**"
        await ctx.send(text)

    @commands.command()
    async def italic(self, ctx, *, text):
        text = f"*{text}*"
        await ctx.send(text)

    @commands.command()
    async def underline(self, ctx, *, text):
        text = f"__{text}__"
        await ctx.send(text)

    @commands.command()
    async def codeline(self,ctx, *, text):
        text = f"`{text}`"
        await ctx.send(text)

    @commands.command()
    async def snippet(self, ctx, *, text):
        text = f"```\n{text}\n```"
        await ctx.send(text)

    @commands.command()
    async def spoiler(self, ctx, *, text):
        text = text.replace('', "||")
        await ctx.send(text)




def setup(client):
    client.add_cog(Fun(client))
