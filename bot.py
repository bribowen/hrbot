import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
channelname = 'general'

def GetReportMessage(member):
    messages = [
        "%s has been reported to HR." % member.mention,
        "%s, I've set up a meeting with Jason Penn to discuss your recent behavior." % member.mention,
        "Thank you for bringing %s to my attention." % member.mention
    ]
    return random.choice(messages)

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
    """ print(str(channelname) + "\n")
    print(str(message.channel.name) + "\n")
    print(str(channelname == message.channel.name) + "\n")
    print(str(message.author) + "\n")
    print(str(client.user) + "\n")
    print(str(message.author == client.user) + "\n")
    print(str("report" in message.content or "Report" in message.content) + "\n")
    print(str(message.content) + "\n")
    for member in message.mentions:
        print("Mentioned: " + str(member.name) + "\n") """

    if message.author == client.user or message.channel.name != channelname:
        return
    elif "report" in message.content or "Report" in message.content:
#        await message.channel.send("I'm trying!")
        for member in message.mentions:
            if client.user != member:
                await message.channel.send(GetReportMessage(member))
            else:
                continue

client.run(token)