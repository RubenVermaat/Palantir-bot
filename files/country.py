from interactions import slash_command, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import requests
import random
import files.functions as functions

class Country(Extension):
        @slash_command("country", description="This will pick a random country to play", scopes=[476830081872822273])
        @slash_option("name", "str option", 3, required=True)
        async def country(self, ctx: SlashContext, *kwargs):
                result = ""
                # if kwargs[0] != None:
                #         result = functions.getCountry(kwargs[0])
                #         if result.error != -1:
                #                 await ctx.send("Name: " + result.data.get('name') + "\n" + "Focus tree status: " + result.data.get('focus_tree_status'))  
                #         else:
                #                 await ctx.send(result.data)
                # else:
                #         result = functions.getRandomCountry()
                #         if result.error != -1:
                #                 await ctx.send("Name: " + result.data.get('name') + "\n" + "Focus tree status: " + result.data.get('focus_tree_status'))  
                #         else:
                #                 await ctx.send(result.data)

        @slash_command("countries", description="This will send information about the character including a link to the wiki page", scopes=[476830081872822273])
        async def countries(self, ctx: SlashContext):
                countries_json = functions.GetAllCountries()
                lines = []
                result = ""
                for country in countries_json.data:
                        lines.append(country.get('country_id') + " - " + country.get('name') + "- Focus tree status: " + country.get('focus_tree_status')) 
                #Including all the lines in one single string
                for line in lines:
                        result = result + line + "\n"
                if len(lines) > 0:
                        await ctx.send(result)
                else:
                        await ctx.send("Something went wrong")
                

def setup(bot):
       Country(bot)