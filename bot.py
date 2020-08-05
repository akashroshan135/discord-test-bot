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
client = commands.Bot(command_prefix = '.')


# runs when the bot is running
@client.event
async def on_ready():
    print('Bot is ready to roll!')


# terminal message on member join
@client.event
async def on_member_join(member):
    print(f'{member} has joined')
    #await channel.send(f'{member} has entered hell!')

# terminal message on member remove
@client.event
async def on_member_remove(member):
    print(f'{member} got yeeted!')
    #await channel.send(f'{member} got yeeted!')


# simple message replies
@client.command()
async def ding(context):
    await context.send('Dong!')

@client.command()
async def king(context):
    await context.send('Kong!')

@client.command()
async def ping(context):
    await context.send(f'Bot ping is {round(client.latency * 1000)}ms!')


# random message replies (8ball)
@client.command(name='8ball')
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


# deletes messages
@client.command()
async def clear(context, amount=1):
    await context.channel.purge(limit=amount+1)


# random message replies. Works when the keyword is present in any message
# BUG: other commands stop working.
"""
@client.event
async def on_message(message):
    if message.author == client.user:
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

client.run(token)