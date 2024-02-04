from interactions import slash_command, SlashCommandChoice, OptionType, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import requests
import random
import functions as functions

class Country(Extension):
        @slash_command("country", description="This will send information about the character including a link to the wiki page")
        @slash_option(
                name="command", 
                description="String Option", 
                required=True, 
                choices=[
                        SlashCommandChoice(name="all", value="all"),
                        SlashCommandChoice(name="name", value="name"),
                        SlashCommandChoice(name="code", value="code"),
                        SlashCommandChoice(name="random", value="random")
                ],
                opt_type=OptionType.STRING
        )
        @slash_option(
                name="input", 
                description="String Option", 
                opt_type=OptionType.STRING
        )
        async def country(self, ctx: SlashContext, *kwargs):
                if kwargs[0] == "all":
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
                elif kwargs[0] == "name":
                        if len(kwargs) <= 1:
                                await ctx.send("No input given")
                        else:
                                result = functions.getCountry(kwargs[1])
                                if result.error != -1:
                                        await ctx.send(result.data)
                                else:
                                        await ctx.send(GetCountryInfoString(result))  
                                
                elif kwargs[0] == "code":
                        if len(kwargs) <= 1:
                                await ctx.send("No input given")        
                        else:
                                result = functions.getCountryByCode(kwargs[1])
                                if result.error != -1:
                                        await ctx.send(result.data)
                                else:
                                        await ctx.send(GetCountryInfoString(result))  
                elif kwargs[0] == "random":
                        result = functions.getRandomCountry()
                        if result.error != -1:
                                await ctx.send(result.data)
                        else:
                                await ctx.send("Random selected country:\n" + GetCountryInfoString(result))  
                else:
                        await ctx.send("Something went wrong")
                
def GetCountryInfoString(result):
        return "Name: " + result.data.get('name') + "\n" + "Focus tree status: " + result.data.get('focus_tree_status') + "\nRace: " + result.data.get('race')

def setup(bot):
       Country(bot)