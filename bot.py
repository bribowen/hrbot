import os
import discord
import random
from dotenv import load_dotenv, find_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
print("Discord token is %s" % token)

client = discord.Client()
channelname = 'human-resources'

def GetReportMessage(member):
    messages = [
        "%s has been reported to HR." % member.mention,
        "%s, I've set up a meeting with Jason Penn to discuss your recent behavior." % member.mention,
        "Thank you for bringing %s to my attention." % member.mention,
        "%s, you are FIRED!" % member.mention,
        "I'll let it slide this time.",
        "%s, you are not allowed to make other co-workers cry. You have been automatically enrolled in sensitivity training." % member.mention,
        "Snitch"
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
    elif "report" in message.content or "Report" in message.content or "reporting" in message.content or "Reporting" in message.content:
#        await message.channel.send("I'm trying!")
        for member in message.mentions:
            if client.user != member:
                await message.channel.send(GetReportMessage(member))
            else:
                continue
    #this is code to kick a member that gets fired!
    elif "fire" in message.content.lower() or "fired" in message.content.lower():
    	for role in message.author.roles:
    		print("The role is: %s" % role)
    		print("The permission to kick members is: %s" % role.permissions.kick_members)
    		if role.permissions.kick_members:
    			for member in message.mentions:
    				if client.user != member:
    					await message.channel.send("%s has been fired. Buh bye!" % member.mention)
    					await member.kick(reason="You have been fired!")
    				else:
    					await message.channel.send("%s, you are not high enough in this organization to fire someone!" % message.author)
    					continue 
    		else:
    			continue
         
client.run(token)
