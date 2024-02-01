from interactions import slash_command, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import requests
import random
import files.functions as functions

class Country(Extension):
        @slash_command("randomcountry", description="This will pick a random country to play", scopes=[476830081872822273])
        @slash_option("name", "str option", 3, required=True)
        async def country(self, ctx: SlashContext, *kwargs):
                result = ""
                result = functions.getRandomCountry()
                if result.error != -1:
                        await ctx.send("Name: " + result.get('name') + "\n" + "Focus tree status: " + result.get('focus_tree_status'))  
                else:
                        await ctx.send(result.data)

        @slash_command("countries", description="This will send information about the character including a link to the wiki page", scopes=[476830081872822273])
        async def countries(self, ctx: SlashContext):
                await ctx.send("List of all the countries")

def setup(bot):
       Country(bot)