import math
import random
import discord
import requests
import json
from discord.ext import commands

class Help(commands.Cog):
        def __init__(self, bot, header):
                self.header = header
                self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
                print("Help command loaded")

        @commands.command()
        async def help (self, ctx):
            lines = []
            returnText = ""
            #Defining every line
            lines.append("/p response [happy/insult/angry/forgive/sorry]") 
            lines.append("  This will give you a lotr themed response based on type") 
            lines.append("/p randomquote") 
            lines.append("  This will give you a random lotr quote") 
            lines.append("/p randomcountry") 
            lines.append("  This will give you a random country in the mod") 
            lines.append("/p character [name]") 
            lines.append("  This will give you some general information about the character")
            lines.append("  Aswell as a link to the wiki page of said character")  
            #Including all the lines in one single string
            for line in lines:
                    returnText = returnText + line + "\n"
            await ctx.send(returnText)

async def setup(bot):
       await bot.add_cog(Help(bot))