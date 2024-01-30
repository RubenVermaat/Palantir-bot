import random
import discord
import requests
from discord.ext import commands

class randomquote(commands.Cog):
        def __init__(self, bot):
                self.header = {'Accept': 'application/json','Authorization': 'Bearer -qLuFGgj_iTqLXdZBHg9'}
                self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
                print("Randomquote command loaded")

        @commands.command()
        async def randomquote(self, ctx):
                response = requests.get("https://the-one-api.dev/v2/quote", headers=self.header)
                #response.status_code response code variable
                records = response.json()
                returnText = ""

                if response.ok:
                        # Choose a random record
                        random_record = random.choice(records.get('docs', []))
                        returnText = random_record.get('dialog')
                        print(random_record)

                else:
                        returnText = "No quote has been found"
                        print("No records found.")
                name = getCharakterByID(random_record.get('character'), self)

                await ctx.send('"' + returnText + '" - '+ name, view=SimpleViewRandomQuote())
                
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
       await bot.add_cog(randomquote(bot))

class SimpleViewRandomQuote(discord.ui.View):
        @discord.ui.button(label="New random quote", style=discord.ButtonStyle.success)
        async def RandomQuote(self, interaction: discord.Interaction, button: discord.ui.Button):
                button.disabled = True
                button.label = "No more pressing!"
                await interaction.response.edit_message(view=self)