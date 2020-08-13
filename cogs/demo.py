# imports discord commands
import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['Test bot', 'Check me', 'Look here'])

class demo(commands.Cog):
    def __init__(self, client):
        self.client = client

    #loops the status for 15 seconds
    @tasks.loop(seconds=15)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))
    
    @commands.Cog.listener() # used for cog events
    async def on_ready(self):
        self.change_status.start()
        print('Bot is ready to roll!')
    
    @commands.command()  # used for cog commands
    async def ping(self, context):
        await context.send(f'Bot ping is {round(self.client.latency * 1000)}ms!. Send from the cog')

    # toss
    @commands.command()
    async def toss(self, context):
        response_data = [
            'Heads',
            'Tails'
        ]
        response = random.choice(response_data)
        await context.send(f'{response}')

def setup(client):
    client.add_cog(demo(client))