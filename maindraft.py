import discord
from aiocron import crontab
import asyncio
import datetime
import google 
from google import genai
import random
from discord.ext import commands, tasks
intents=discord.Intents.default()
intents.members=True
intents.message_content=True
bot=commands.Bot(command_prefix="$", intents=intents)
TOKEN=("")
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
wmessages=[
    "Welcome {member}! Hope you enjoy your stay here in {member.guild.name}!",
    "Hey {member}, glad you could join us!",
    "Look who just joined! Welcome, {member}!",
    "Welcome aboard {member.guild.name}, {member}! We were expecting you!",
    "A new challenger approaches! Welcome, {member}!",
    "It's party time! {member} just joined {member.guild.name}!"]
@bot.event
async def memwelcome(member):
    channel=discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        w_message=random.choice(wmessages).format(member=member.mention)
        await channel.send(w_message)
bot.run(TOKEN)
