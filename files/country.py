import math
import random
import discord
import requests
import json
import files.functions as functions
from discord.ext import commands

class Country(commands.Cog):
        def __init__(self, bot, countries, header):
                self.header = header
                self.bot = bot
                self.countries = countries

        @commands.Cog.listener()
        async def on_ready(self):
                print("Randomcountry command loaded")

        @commands.command()
        async def randomcountry(self, ctx):
                returnText = ""
                returnText = functions.getRandomItem(self.countries)
                await ctx.send("Name: " + returnText.get('name') + "\n" + "Focus tree status: " + returnText.get('focus_tree_status'))  

async def setup(bot):
       await bot.add_cog(Country(bot))