from interactions import slash_command, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension
import os
import files.functions as functions

class Randomquote(Extension):
        @slash_command("randomquote", description="This will send a random lotr quote", scopes=[476830081872822273])
        async def character(self, ctx: SlashContext):
                result = functions.getRandomQuote()
                if result.error != -1:
                        await ctx.send(result.data)
                else:
                        await ctx.send('"' + result.data + '" - '+ result.name)
def setup(bot):
       Randomquote(bot)

# class SimpleViewRandomQuote(discord.ui.View):
#         import files.functions as functions

#         @discord.ui.button(label="New random quote", style=discord.ButtonStyle.success)
#         async def RandomQuote(self, interaction: discord.Interaction, button: discord.ui.Button):
#                 button.disabled = True
#                 button.label = "No more pressing!"
#                 await interaction.response.edit_message(view=self)