import discord
import asyncio
import datetime
import google.generativeai as genai
from discord.ext import commands, tasks
intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix="$", intents=intents)
TOKEN=os.getenv("MTM0NjEyMDE0NjIwNDM2MDgwNQ.GU6VEg.ETp7fvNJvQ53uINslvAgCiEqcKGVk7qY10mBhw")
