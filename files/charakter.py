import math
import random
import discord
import requests
import json
from discord.ext import commands

class charakter(commands.Cog):
        def __init__(self, bot):
                self.header = {'Accept': 'application/json','Authorization': 'Bearer -qLuFGgj_iTqLXdZBHg9'}
                self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
                print("Charakter command loaded")

        @commands.command()
        async def character (self, ctx, arg):
                lines = [];
                response = requests.get("https://the-one-api.dev/v2/character", headers=self.header)
                #response.status_code response code variable
                records = response.json()
                returnText = ""

                if response.ok:
                        # Choose a random record
                        found_record = next((record for record in records.get('docs', []) if (record.get('name').lower().find(arg.lower())) != -1), None)
                        print(found_record)
                        if found_record != None:
                                 #Defining every line
                                lines.append("Name: " + found_record.get('name')) 
                                lines.append("Race: " + found_record.get('race')) 
                                if found_record.get('gender') != "": lines.append("Gender: " + found_record.get('gender')) 
                                if found_record.get('birth') != "": lines.append("Birth: " + found_record.get('birth')) 
                                if found_record.get('death') != "": lines.append("Death: " + found_record.get('death')) 
                                if found_record.get('realm') != "": lines.append("Realm: " + found_record.get('realm')) 
                                if found_record.get('hair') != "": lines.append("Hair: " + found_record.get('hair')) 
                                if found_record.get('height') != "": lines.append("Height: " + found_record.get('height')) 
                                lines.append("Wikipage: " + found_record.get('wikiUrl')) 
                                #Including all the lines in one single string
                                for line in lines:
                                        returnText = returnText + line + "\n"
                        else:
                                returnText = "I could not find such a being"
                else:
                        returnText = "Something went wrong"
                        print(response.status_code)
                
               
                #Returning said string
                await ctx.send(returnText)

def getCharakterByID(id, self):
        response = requests.get("https://the-one-api.dev/v2/character?_id=" + id, headers=self.header)
        returnText = ""
        if response.ok:
                record = response.json()
                print(record)
                returnText = record.get('docs', [])[0].get('name')
        else:
                returnText = "No charakters has been found"
        return returnText


async def setup(bot):
       await bot.add_cog(charakter(bot))