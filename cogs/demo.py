# imports discord commands
import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['Test bot', 'Check me', 'Look here'])

class demo(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.change_status.stop()
        self.change_status.start()

    #loops the status for 15 seconds
    @tasks.loop(seconds=15)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))
    
    @commands.Cog.listener() # used for cog events
    async def on_ready(self):
        print('Bot is ready to roll!')
    
    @commands.command()  # used for cog commands
    async def ping(self, context):
        await context.send(f'Bot ping is {round(self.client.latency * 1000)}ms!. Send from the cog')

def setup(client):
    client.add_cog(demo(client))