import discord
import os
import asyncio
import datetime
import google.generativeai as genai
from discord.ext import commands, tasks
intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix="$", intents=intents)
TOKEN=("")
