#*******************************************
#***************LIBRARIES*******************
#******************************************* 
import discord
from discord.ext import commands
from BOTTOKEN import token
import requests

# discord client connection and define command prefix
client = commands.Bot(command_prefix = "!")


#*******************************************
#************HELPER FUNCTIONS***************
#******************************************* 
def openLink(link) :
  requests.get(link)
  if reponse.status_code == 200:
    print("SUccessfully opened the link.")
  if response.status_code == 400 :
    print("Failed to open link.")

#*******************************************
#*************CLIENT EVENTS*****************
#******************************************* 
@client.event
async def on_message(message) :
  msg = message.content
  msgch = message.channel

  if message.channel.name == 'music' :
    # terminal logging
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # bot commands
    if msg.startswith("!add") :
      link = msg.split("!add ", 1)[1]
      await msgch.send(f'Requested by {username}, now searching for: ' + link)
      # have link do http request
    elif msg.startswith("!skip") :
      await msgch.send("No code has been written for this yet...")
      return
    elif msg.startswith("!clear") :
      await msgch.send("No code has been written for this yet...")
      return
    elif msg.startswith("!pause") :
      await msgch.send("No code has been written for this yet...")
      return
    elif msg.startswith("!play") :
      await msgch.send("No code has been written for this yet...")
      return
    elif msg.startswith("!commands") :
      await msgch.send("'!add' to add audio to the queue.\n"
                       "'!skip' to skip the current audio.\n"
                       "'!clear' to clear the queue.\n"
                       "'!pause' to pause the audio.\n"
                       "'!play' to play the audio.")
  
  await client.process_commands(message)

      
#*******************************************
#************CLIENT COMMANDS****************
#******************************************* 
@client.command()
# pass_context used for voice communication with bot
async def join(ctx) :
# ctx variable used to communicate with discord -> send/receive
  if ctx.channel.name == 'music' :
    if (ctx.author.voice) : 
      voiceChannel = ctx.message.author.voice.channel
      # this line used to detect vc
      await voiceChannel.connect()
    else :
      await ctx.send("Please join a Voice Channel, then run this command!")

@client.command(pass_context = True)
async def leave(ctx) :
  if ctx.channel.name == 'music' :
    await ctx.guild.voice_client.disconnect()
    # guild (server) -> vc -> disconnect bot)
    await ctx.send("I left the Voice Channel!")

@client.command(name = "ping")
async def ping(ctx) :
  await ctx.send("pong")

  
#*******************************************
#**************ACTIVATION*******************
#*******************************************
@client.event
async def on_ready() :
  print("{0.user} is now logged in!".format(client))
  print("--------------------------------")
  # enables bot and prints message to terminal  
  
# public bot token
client.run(token)

"""
discord.py
discord.py[voice]
"""