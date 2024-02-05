from interactions import slash_command, OptionType, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import requests
class Wiki(Extension):
        @slash_command("wiki", description="This will send information about the character including a link to the wiki page")
        @slash_option(
            name="page",
            description="String Option",
            required=True,
            opt_type=OptionType.STRING
        )
        async def wiki(self, ctx: SlashContext, *kwargs):
            #test
            await ctx.send("Work in progress")


def setup(bot):
       Wiki(bot)