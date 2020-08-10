# imports discord commands
import discord
from discord.ext import commands

class demo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() # used for cog events
    async def on_ready(self):
        print('Bot is ready to roll!')
    
    @commands.command()  # used for cog commands
    async def ping(self, context):
        await context.send(f'Bot ping is {round(self.client.latency * 1000)}ms!. Send from the cog')


def setup(client):
    client.add_cog(demo(client))
    