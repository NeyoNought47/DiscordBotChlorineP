# Bot Chlorine (Bot Oni 1.0 legacy)
# Application ID: 
# Public Key: 
# https://discord.com/oauth2/authorize?client_id=1371685857177632848&permissions=8&integration_type=0&scope=bot
# May 12 2025 (Oni Feb/8/2021)
# @author: NeoNought47

import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print('✅ Bot Chlorine is currently running. \n⚠️  Do not close this terminal / window.')

@client.command()
async def cMan(ctx):
    embed0 = discord.Embed(
        title="Command Manual",
        description="List of available commands",
        color=discord.Color.blue()
    )

    embed1 = discord.Embed(
        color=discord.Color.green()
    )

    embed1.add_field(name="Normal Commands", value="""
        `.cMan` - Show command manual.
        `.cHi` - Say hi.
        `.cRules` - Server rules.
        `.cAbout` - About the bot.
        `.cPing` - Network latency.
        `.cRps [name]` - Rock-paper-scissors.
        `.cRandomText` - Random quote.
        `.cRandomStory` - Random story.
        """, inline=False)

    embed2 = discord.Embed(
        color=discord.Color.red()
    )
    embed2.add_field(name="Admin Utils", value="""
                     `.cClean10` - Clean 10 messages.
                    `.cClean100` - Clean 100 messages.
                    `.cKick [@member]` - Kick a member.
                     """, inline=False)

    await ctx.send(embed=embed0)
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)

# command - cHi
@client.command()
async def cHi(ctx):
    embedCHi = discord.Embed(
        title="",
        description="Hiii",
        color=discord.Color.blue())
    await ctx.send(embed=embedCHi)

# command - cPing
@client.command()
async def cPing(ctx):
    currentLatency = (client.latency * 1000)
    if currentLatency < 100:
        embed3 = discord.Embed(color=discord.Color.green())
        embed3.add_field(name = "", value = "Low latency \n Chlorine's ping is {} ms".format(currentLatency))
        await ctx.send(embed=embed3)
    elif 100 < currentLatency < 250:
        embed4 = discord.Embed(color=discord.Color.yellow())
        embed4.add_field(name = "", value = "Medium latency \n Chlorine's ping is {} ms".format(currentLatency))
        await ctx.send(embed=embed4)
    else:
        embed5 = discord.Embed(color=discord.Color.red())
        embed5.add_field(name = "", value = "High latency \n Chlorine's ping is {} ms".format(currentLatency))
        await ctx.send(embed=embed5)
    
# command - cRules
@client.command()
async def cRules(ctx):
    embedRules = discord.Embed(
        title="",
        description="啥也没有 :/",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embedRules)

# command - cAbout
@client.command()
async def cAbout(ctx):
    embedAbout = discord.Embed(
        title="",
        description='Neo 2025 \nVersion: 1.0 \nNew version of Bot Oni (2021)',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embedAbout)

@client.command()







# command - cRandomText
@client.command()
async def cRandomText(ctx):
    randomList = [
        'Th-th-th-th-th-the route, Sydney.',
        'What a lovely day, right? ...Aus wie ein scheiss Autounfall.',
        'We are expecting visitors. Che lo spettacolo abbia inizio.',
        'Courez comme si le magasin de cigarettes allait fermer.',
        'If you would like to make a call, please hang up and dial again. If you need help, please hang up and dial your operator.',
    ]
    await ctx.send(random.choice(randomList))

# command - cRps
@client.command()
async def cRps(ctx, *, yourName):
    posi = ['rock', 'scissors', 'paper']
    await ctx.send(f'The user {yourName} sent a {random.choice(posi)}')

# Admin Utils - cClean10
@client.command()
@commands.has_role('mega-admin')
async def cClean10(ctx):
    await ctx.channel.purge(limit=11)
    await ctx.send('**[10 lines of messages have been deleted.]**')

# Admin Utils - cClean100
@client.command()
@commands.has_role('mega-admin')
async def cClean100(ctx):
    await ctx.channel.purge(limit=101)
    await ctx.send('**[100 lines of messages have been deleted.]**')

# Admin Utils - cKick
@client.command()
@commands.has_role('mega-admin')
async def cKick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} was kicked, R.I.P.')

# .env 文件读取
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN_ENV')

client.run(TOKEN)