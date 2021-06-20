import discord 
from discord.ext import commands
from typing import Text
from discord import message
from discord import embeds
from discord.colour import Color
from discord.embeds import Embed
from discord.enums import TeamMembershipState
from discord.ext import commands
from discord.flags import Intents
from discord.message import Message
from random import randbytes, randint
import asyncio
import gzip

client = commands.Bot(command_prefix = "*")

@client.event
async def on_ready():
    activity = discord.Game(name="| Hi, I'm Goorbay | *Goorbay | *invite |")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is online")

client.remove_command('help')

client.run('ODU2MTI1OTMxODY1NTA1ODEy.YM8faA.G9l7X8Wp-smN6TyY67Hbnsej5BE')