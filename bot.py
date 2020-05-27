# imports dotenv plugin to load environment variables
import os
from dotenv import load_dotenv

# imports discord commands
import discord
from discord.ext import commands

# loads the environment variables
load_dotenv()
token = os.getenv('discord_token')

# prefix to use the bot
bot = commands.Bot(command_prefix = '')

# runs when the bot is running
@bot.event
async def on_ready():
    print('I am ready!')

# terminal message on member join
@bot.event
async def on_member_join(member):
    print(f'{member} has joined')
    await member.create_dm()
    await member.dm_channel.send(
        f"Sup {member.name}, if you're seeing this message then it worked"
    )

# terminal message on member remove
@bot.event
async def on_member_remove(member):
    print(f'{member} has been yeeted')

# simple message replies
@bot.command()
async def ping(context):
    await context.send('Pong!')

@bot.command()
async def ding(context):
    await context.send('Dong!')

@bot.command()
async def king(context):
    await context.send('Kong!')

bot.run(token)