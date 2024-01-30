import math
import random
import discord
import requests
import json
from discord.ext import commands

class Response(commands.Cog):
        def __init__(self, bot, data):
                self.header = {'Accept': 'application/json','Authorization': 'Bearer -qLuFGgj_iTqLXdZBHg9'}
                self.bot = bot
                self.data = data

        @commands.Cog.listener()
        async def on_ready(self):
                print("Response command loaded")

        @commands.command()
        async def response(self, ctx, arg):
            returnText = ""
            if arg.lower() == "angry":
                returnText = selectRandomTypeQoute(self, arg)
            elif arg.lower() == "happy":
                returnText = selectRandomTypeQoute(self, arg)
            else:
                returnText = "Type not reconized. Are you having a strook?"
            await ctx.send(returnText)  

def selectRandomTypeQoute(self, type):
    type_records = [quote for quote in self.data if quote['type'] == type]
    random_record = random.choice(type_records)
    return random_record.get('dialog')

async def setup(bot):
       await bot.add_cog(Response(bot))