import discord
import asyncio
import datetime
import google.generativeai as genai
from discord.ext import commands, tasks
client=discord.Client()
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
          