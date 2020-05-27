import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '')

# runs when the bot is running
@bot.event
async def on_ready():
    print('I am ready!')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined')

@bot.event
async def on_member_remove(member):
    print(f'{member} has been yeeted')

@bot.command()
async def ping(context):
    await context.send('Pong!')

@bot.command()
async def ding(context):
    await context.send('Dong!')

@bot.command()
async def king(context):
    await context.send('Kong!')

bot.run('NzEyNTY3MjEzMjIzMDUxMzM1.XsTcWg.1BKJ23Xq0us_FPLPQUVnrfjpOK4')