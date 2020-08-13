# imports discord commands
import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['Test bot', 'Check me', 'Look here'])

class demo(commands.Cog):
    def __init__(self, client):
        self.client = client

    # loops the status for 15 seconds
    @tasks.loop(seconds=15)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))
    
    # used for cog events
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print('Bot is ready to roll!')
    
    # used for cog commands
    @commands.command()  
    async def ping(self, context):
        await context.send(f"Bot's ping is {round(self.client.latency * 1000)}ms!")

    # toss
    @commands.command()
    async def toss(self, context):
        toss_res = random.choice(['Heads', 'Tails'])
        await context.send(f'{toss_res}')

def setup(client):
    client.add_cog(demo(client))