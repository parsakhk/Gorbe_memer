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
    activity = discord.Game(name="| Hi, I'm Goorbay | *Gorbay | *invite |")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is online")

client.remove_command('help')




@client.command()
async def gorbay(ctx):
    print("gorbay Entered")
    
    help_em = discord.Embed(title="منو کامند ها", color=0xFFD700)
    help_em.add_field(name="کامند ها اصلی", value="*gorbay : `منو کامندها`\n*invite : `اینوایت دادن بات`\n*ping : `نمایش پینگ`", inline=False)
    await ctx.send(embed=help_em)
    
    
@client.command()
async def invite(ctx):
    ctx.reply("لینک اینوایت خدمت شما\nhttps://discord.com/api/oauth2/authorize?client_id=856125931865505812&permissions=0&scope=bot")

@client.command()
async def ping(ctx, bot):
    if message.content.startswith('*ping'):
        embedVar = discord.Embed(title="پینگ شما!", description=(f'your ping is {bot.latency}'), color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await ctx.channel.send(embed=embedVar)




client.run('ODU2MTI1OTMxODY1NTA1ODEy.YM8faA.G9l7X8Wp-smN6TyY67Hbnsej5BE')
