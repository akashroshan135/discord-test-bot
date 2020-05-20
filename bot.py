import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready')

client.run('NzEyNTY3MjEzMjIzMDUxMzM1.XsTcWg.1BKJ23Xq0us_FPLPQUVnrfjpOK4')