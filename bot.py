# imports dotenv plugin to load environment variables
import os
from dotenv import load_dotenv
# loads the environment variables
load_dotenv()
token = os.getenv('discord_token')

# imports discord commands
import discord, random
from discord.ext import commands

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


# random message replies
@bot.command(name='test')
async def bot_msg(context):
    test_data = [
        'west',
        'east',
        'north',
        'boom',
        "Whomst'd've",
    ]
    response = random.choice(test_data)
    await context.send(response)

# random message replies. Works when the keyword is present in any message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    test_data = [
        'this server is crap',
        'thing BAD',
        '#hustleCulture',
        'wow such empty',
        "Whomst'd've have summoned me",
    ]
    if 'bot' in message.content.lower():
        response = random.choice(test_data)
        await message.channel.send(response)


bot.run(token)