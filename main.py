# ###TODO
# #ADDED Connecting to API with lotr database
# #ADDED Random quote command
# #ADDED Random country command
# #Adding trivia questions command/every day new question?
# #Adding quiz to link role to someone

import os
import logging
import json
from interactions import Client, Intents, listen
from interactions.api.events import Component, MemberAdd
from interactions.ext import prefixed_commands
import pkgutil
import functions

from interactions import slash_command, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension

# define your own logger with custom logging settings
logging.basicConfig()
cls_log = logging.getLogger("MyLogger")
cls_log.setLevel(logging.DEBUG)

bot = Client(
    intents=Intents.ALL,
    sync_interactions=True,
    asyncio_debug=True,
    delete_unused_application_cmds=True,
    logger=cls_log,
    debug_scope= 476830081872822273
)

@listen()
async def on_startup():
    print("Ready")
    print(f"This bot is owned by {bot.owner}")
    prefixed_commands.setup(bot)

# You are the {member.memberCount} member to join.
@listen
async def on_member_join(member):
    print("Ready")
    await bot.get_channel(os.getenv('CHANNEL_ID')).send(f"Hello, , welcome to the discord server! You are the member to join")
#    true_member_count = len([m for m in bot.get_guild(os.getenv('CHANNEL_ID')).members if not m.bot]) # doesn't include bots 
#    await bot.get_channel(os.getenv('CHANNEL_ID')).send(f"Hello, {member.mention}, welcome to the discord server! You are the {true_member_count} member to join")

@listen()
async def on_guild_join(event: MemberAdd):
   true_member_count = len([m for m in event.guild.members if not m.bot]) # doesn't include bots 
   random_quote = functions.getRandomQuote()
   await bot.get_channel(os.getenv('CHANNEL_ID')).send(f"Hello, {event.member.mention}, welcome to the discord server! You are the {true_member_count} member to join\n'" + random_quote.data + "' - " + random_quote.name)

@listen()
async def on_guild_create(event):
    print(f"guild created : {event.guild.name}")


# Message content is a privileged intent.
# Ensure you have message content enabled in the Developer Portal for this to work.
@listen()
async def on_message_create(event):
    print(f"message received: {event.message.content}")


@listen()
async def on_component(event: Component):
    ctx = event.ctx
    await ctx.edit_origin("test")

# Loading all the extension files in the folder 'files'
# Note: might break if other kind of files/folders exist in folder
extension_names = [m.name for m in pkgutil.iter_modules(["files"], prefix="files.")]
for extension in extension_names:
    bot.load_extension(extension)

bot.start(os.getenv('DISCORD_BOT_TOKEN'))