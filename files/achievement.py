from interactions import slash_command, OptionType, SlashCommandChoice, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension, Embed, File
import os
import requests
import random
import functions as functions

class Achievement(Extension):
        @slash_command("achievement", description="This will send information about this achievement")
        @slash_option(
            name="command",
            description="String Option",
            required=True,
            choices=[
                SlashCommandChoice(name="random", value="random"),
                SlashCommandChoice(name="name", value="name")
            ],
            opt_type=OptionType.STRING
        )
        @slash_option(
            name="name",
            description="String Option",
            opt_type=OptionType.STRING
        )
        async def response(self, ctx: SlashContext, *kwargs):
            if kwargs[0] == "random":
                result =  functions.selectRandomAchievement(self)
            elif kwargs[0] == "name":
                result =  functions.selectAchievementByName(self, kwargs[1])
            lines = [];
            returnText = ""
            if result.error != -1:
                await ctx.send(result.data)
            else:
                lines.append("Name: " + result.data.get('name')) 
                lines.append("Description: " + result.data.get('description')) 
                #Including all the lines in one single string
                for line in lines:
                    returnText = returnText + line + "\n"
                #Returning said string
                file = File("./data/achievements/" + result.data.get('achievement_id') + ".png")
                embed = Embed()
                embed.set_image(url="attachment://" + result.data.get('achievement_id') + ".png")
                await ctx.send(content=returnText, embeds=embed, files=file)

def setup(bot):
       Achievement(bot)