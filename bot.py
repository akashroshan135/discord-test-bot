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
bot = commands.Bot(command_prefix = '.')

# runs when the bot is running
@bot.event
async def on_ready():
    print('Bot is ready to roll!')

# terminal message on member join
@bot.event
async def on_member_join(member):
    print(f'{member} has joined')

# terminal message on member remove
@bot.event
async def on_member_remove(member, context):
    print(f'{member} got yeeted!')
    await context.send(f'{member} got yeeted!')


# simple message replies
@bot.command()
async def ding(context):
    await context.send('Dong!')

@bot.command()
async def king(context):
    await context.send('Kong!')

@bot.command()
async def ping(context):
    await context.send(f'Bot ping is {round(bot.latency * 1000)}ms!')


# random message replies (8ball)
@bot.command(name='8ball')
async def _8ball(context, *, question):
    response_data = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't count on it.",
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.'
    ]
    response = random.choice(response_data)
    await context.send(f"Question: {question}\nAnswer: {response}")

# random message replies. Works when the keyword is present in any message
# BUG: other commands stop working.
"""
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
"""

bot.run(token)