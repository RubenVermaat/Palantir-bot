import random
import discord
import requests
import files.functions as functions
from discord.ext import commands

class Randomquote(commands.Cog):
        def __init__(self, bot, header):
                self.header = header
                self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
                print("Randomquote command loaded")

        @commands.command()
        async def randomquote(self, ctx):
                result = functions.getrandomquote(self.header)
                if result[0] == -1:
                        await ctx.send(result[1])
                else:
                        await ctx.send('"' + result[1] + '" - '+ result[2])
                        # await ctx.send('"' + result[1] + '" - '+ result[2], view=SimpleViewRandomQuote())

async def setup(bot):
       await bot.add_cog(Randomquote(bot))

class SimpleViewRandomQuote(discord.ui.View):
        import files.functions as functions

        @discord.ui.button(label="New random quote", style=discord.ButtonStyle.success)
        async def RandomQuote(self, interaction: discord.Interaction, button: discord.ui.Button):
                button.disabled = True
                button.label = "No more pressing!"
                await interaction.response.edit_message(view=self)