from interactions import slash_command, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import requests
import random
import files.functions as functions

class Response(Extension):
        @slash_command("response", description="This will send a random response based on the given type", scopes=[476830081872822273])
        @slash_option("type", "str option", 3, choices=["insult", "happy", "sorry", "forgive"], required=True)
        async def response(self, ctx: SlashContext, *kwargs):
            result =  functions.selectRandomTypeQoute(self, kwargs[0])
            if result.error != -1:
                await ctx.send(result.data)
            else:
                await ctx.send(result.data)

def setup(bot):
       Response(bot)