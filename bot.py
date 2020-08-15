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


# terminal message on member join
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    channel = discord.utils.get(member.guild.channels, name="general")
    await channel.send(f'Welcome to the server, {member.mention}')

# terminal message on member remove
@client.event
async def on_member_remove(member):
    print(f'{member} got yeeted!')
    channel = discord.utils.get(member.guild.channels, name="general")
    await channel.send(f'I thought we were friends, {member.mention}?')

# kicks a member
@client.command()
async def kick(context, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await context.send(f'{member.mention} has been kicked from the server')

# bans a member
@client.command()
async def ban(context, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await context.send(f'{member.mention} has been banned from the server')


# simple message replies
@client.command()
async def ding(context):
    await context.send('Dong!')
    await botlog(context, 'ding')

@client.command()
async def king(context):
    await context.send('Kong!')


async def botlog(context, command):
    log_channel = discord.utils.get(context.guild.channels, name="bot-log")
    await log_channel.send(f'{context.message.author.mention} used {command}')


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
async def purge(context, amount=1, *, reason='chuma'):
    deleted = await context.channel.purge(limit=amount+1)
    await context.send(f'Deleted {amount} message(s)\nReason: {reason}')


# cogs demo
@client.command()
async def load(context, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} cog has been loaded')
    await context.send(f'{extension} cog has been loaded')

@client.command()
async def unload(context, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'{extension} cog has been unloaded')
    await context.send(f'{extension} cog has been unloaded')

@client.command()
async def reload(context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} cog has been reloaded')
    await context.send(f'{extension} cog has been reloaded')


# random message replies. Works when the keyword is present in any message
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
    await client.process_commands(message)


@client.command()
async def users(context):
    # send members count
    await context.send(f'No of members: {context.guild.member_count}\n')
    # send members count excluding bots
    await context.send(f'No of true members: {len([m for m in context.guild.members if not m.bot])}')

@client.command()
async def update(context):
    categories = discord.utils.get(context.guild.categories, name="server stat")
    voice = discord.utils.get(context.guild.voice_channels, name=str(categories.voice_channels[0])) # Get the first voice_channel in this category
    update = "Member count: " + str(context.guild.member_count) 
    await voice.edit(name=update) # Edit voice channel


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)