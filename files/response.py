from interactions import slash_command, OptionType, SlashCommandChoice, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import requests
import random
import functions as functions

class Response(Extension):
        @slash_command("response", description="This will send a random response based on the given type")
        @slash_option(
            name="type",
            description="String Option",
            choices=[
                    SlashCommandChoice(name="insult", value="insult"),
                    SlashCommandChoice(name="happy", value="happy"),
                    SlashCommandChoice(name="sorry", value="sorry"),
                    SlashCommandChoice(name="forgive", value="forgive")
            ],
            required=True,
            opt_type=OptionType.STRING
        )
        async def response(self, ctx: SlashContext, *kwargs):
            result =  functions.selectRandomTypeQoute(self, kwargs[0])
            if result.error != -1:
                await ctx.send(result.data)
            else:
                await ctx.send(result.data)

def setup(bot):
       Response(bot)