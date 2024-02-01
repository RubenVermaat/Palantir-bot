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
from interactions.api.events import Component
from interactions.ext import prefixed_commands

from interactions import slash_command, slash_option, SlashContext, context_menu, CommandType, Button, ActionRow,ButtonStyle, Extension

# define your own logger with custom logging settings
logging.basicConfig()
cls_log = logging.getLogger("MyLogger")
cls_log.setLevel(logging.DEBUG)

bot = Client(
    intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
    sync_interactions=True,
    asyncio_debug=True,
    logger=cls_log
)
prefixed_commands.setup(bot)

@listen()
async def on_ready():
    print("Ready")
    print(f"This bot is owned by {bot.owner}")

# You are the {member.memberCount} member to join.
@bot.event
async def on_member_join(member):
   true_member_count = len([m for m in bot.get_guild(os.getenv('CHANNEL_ID')).members if not m.bot]) # doesn't include bots 
   await bot.get_channel(os.getenv('CHANNEL_ID')).send(f"Hello, {member.mention}, welcome to the discord server! You are the {true_member_count} member to join")

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

bot.load_extension("test_components")
bot.load_extension("files.charakter")
bot.load_extension("files.randomquote")
bot.load_extension("files.response")
bot.load_extension("files.country")
bot.start(os.getenv('DISCORD_BOT_TOKEN'))