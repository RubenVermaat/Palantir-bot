import math
import random
import discord
import requests
import json
from discord.ext import commands

class Response(commands.Cog):
        def __init__(self, bot, data, header):
                self.header = header
                self.bot = bot
                self.data = data

        @commands.Cog.listener()
        async def on_ready(self):
                print("Response command loaded")

        @commands.command()
        async def response(self, ctx, arg):
            returnText = ""
            if selectRandomTypeQoute(self, arg) != "error":
                returnText = selectRandomTypeQoute(self, arg)
            else:
                returnText = "Type not reconized. Are you having a strook?"
            await ctx.send(returnText)  

def selectRandomTypeQoute(self, type):
    type_records = [quote for quote in self.data if quote['type'].lower() == type.lower()]
    if len(type_records) > 0:
        random_record = random.choice(type_records)
        return random_record.get('dialog')
    else:
        return "error"

async def setup(bot):
       await bot.add_cog(Response(bot))