
import discord
import os
import requests
import json

client = discord.Client()

# def get_dog():
#   response = requests.get("https://dog.ceo/api/breeds/image/random")
#   json_data = json.loads(response.text)
#   dog = json_data[0]
#   return(dog)

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('Hello'):
    # dog = get_dog()
    await message.channel.send('Hey there!')

my_secret = os.environ['LIC']
client.run(os.getenv('LIC'))