import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

"""@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )"""

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif "report" in message.content:
        await client.send_message(message.channel, "I'm trying!")
        for member in message.mentions:
            if client.user != member:
                await client.send_message(message.channel, "%s has been reported to HR." % member.mention)
            else:
                continue

client.run(token)