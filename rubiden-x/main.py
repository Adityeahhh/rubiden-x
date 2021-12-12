
'''
rubiden production
'''

import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import base64
import json
import difflib
from difflib import get_close_matches
import os 
import random
import io 
import numpy as np
import requests
import asyncio
import aiohttp
import psutil
import datetime
from io import BytesIO
import time
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from keep_alive import keep_alive
import time
from aiohttp import request






intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True).all()
client = commands.Bot(command_prefix = 'rubi ', intents = intents)
client.remove_command("help")



scenerios = ["'s heart went afk",'got rickrolled and died after their eyes got blasted', 'died of starvation', 'successfully licked their elbow but disclocated their elbow bone in process', "hugged a creeper", 'got over their addiction of breathing', "licked too much chalk ", 'spitted on the ceiling, the ceiling spat back ', 'Got sniped by a camper', 'sacrificed themselves to Lord chungus', 'got eaten by the evil vampire mommy', 'said minecraft sucks and fortnite is good. Immediately got Assasinated', 'listened to Justin Bieber', 'went to nether without any armour', 'got cancelled by 14 year olds', 'said rubi bad. You know what happend next', "Ate glue instead of ice cream...Dumbass", "Said gibberish which apparently meant kill me in spanish...", "Got exchanged for the soul stone", 
"Watched jake paul ～(　TロT)σ.", "Got killed by dio: MUDA MUDA MUDA MUDA MUDA MUDA MUDA", "Got killed by jotaro: ORA ORA ORA ORA ORA ORA ORA ORA", "Changed their keyboard layout and because of that accidently texted their mom f*** off", 
"Got hacked and all the peppa pig episodes in their tablet were leaked", 'got bitten by a bat, they bit back and here we are now', 'died in the blip',
'Used windows in apple headquarters']

went = np.array(['cleared', 'disappeared', 'evanesced', 'evaporated', 'faded', 'fled', 'branched (out)', 'broke up', 'disbanded', 'diverged', 'divided', 'forked', 'separated', 'spilled', 'disassembled', 'dispersed', 'dissipated'])

colors = [discord.Color.from_rgb(7, 13, 23), discord.Color.from_rgb(14,14,15), discord.Color.from_rgb(55,55,55), discord.Color.from_rgb(0,0,0), discord.Color.from_rgb(70, 71, 77)]

joined = np.array([
'involved',
'merged',
'united',
'accompanying',
'affiliated',
'affixed',
'allied',
'amalgamated',
'associated',
'attached',
'banded',
'blended',
'bracketed',
'cemented',
'combined',
'confederated',
'conjoined',
])

tralala = 'rubi help '

@client.event
async def on_ready():
  members = 0
  for guild in client.guilds:
        members += guild.member_count - 1

  await client.change_presence(activity=discord.Game(status=discord.Status.idle, name =f"{tralala} || Watching {len(client.guilds)} servers and {members} members! ||  DEV: @BOLT"))

  print("we have logged in as {0.user}".format(client))


# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return



#help tab commands

@client.group(invoke_without_command=True)
async def help(ctx):
  em  = discord.Embed(title = 'Rubiden Help', description = 'use rubi help <command> for extended information on that command', color = ctx.author.color)

  em.add_field(name = 'Moderation :tools:', value = '`kick`, `ban`, `clear`, `ping`, `slowmode`, `mute`, `info`, `snipe`')
  em.add_field(name = 'Fun :laughing:', value = '`eightball`, `heart`, `quote`, `reddit`, `chance`, `dadjoke`, `meme`, `dankmeme`')
  em.add_field(name = 'Animal :dog:', value = '`catto`, `doggo`, `foxy`, `birb`, `shiba`, `panda`, `spit`')
  em.add_field(name = 'Utilities :gear:', value = '`pfp`, `cpustats`, `memstats`, `invite`')
  em.add_field(name = 'Leveling/Economy [BETA] :money_with_wings:', value = '`level`, `balance`, `beg`, `gamble`')
  em.add_field(name = 'Meme Generation :moyai:', value = '`power`, `winnie`, `average`, `drawuno`, `mimicpower`, `yellcat`, `buffdoge`')
  em.add_field(name = 'Expressions :wink:', value = '`pat`, `wink`, `hug`, `think`')
  await ctx.send(embed = em)



@help.command()
async def pat(ctx):
  em = discord.Embed(title = 'Pat', description = 'Go ahead and pat someone', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi pat <memberName>')
  
  await ctx.send(embed = em)

@help.command()
async def hug(ctx):
  em = discord.Embed(title = 'Hug', description = 'Go ahead and hug someone', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi pat <memberName>')
  
  await ctx.send(embed = em)

@help.command()
async def wink(ctx):
  em = discord.Embed(title = 'Wink', description = 'Wink at someone', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi wink <memberName>')
  
  await ctx.send(embed = em)

@help.command()
async def kick(ctx):
  em = discord.Embed(title = 'Kick', description = 'Kicks a given member and with a reason too (optional)', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi kick <memberName> [reason]')
  
  await ctx.send(embed = em)

@help.command()
async def invite(ctx):
  em = discord.Embed(title = 'Invite', description = 'Invite me to your server!', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi invite')
  
  await ctx.send(embed = em)

@help.command()
async def snipe(ctx):
  em = discord.Embed(title = 'Snipe', description = 'Returns the most recently deleted message', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi snipe')
  
  await ctx.send(embed = em)

@help.command()
async def info(ctx):
  em = discord.Embed(title = 'Information', description = "Get any user's information", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi info <memberName>')
  
  await ctx.send(embed = em)


@help.command()
async def spit(ctx):
  em = discord.Embed(title = 'spit', description = "Get any number of animal pictures (max 10)", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi spitAnimalNameHere {number of imgs}')

  em.add_field(name = 'Example', value = 'rubi spitcatto 4')

  em.add_field(name = '**Caution**',inline = False,  value = 'only these animals can be showed:- \n catto \n doggo \n panda \n birb \n foxy')

  em.add_field(name = 'animal commands', value = 'spitcatto {number} \n spitdoggo {number}\n spitpanda {number}\n spitbirb {number} \n spitfoxy {number}')

  
  await ctx.send(embed = em)

@help.command()
async def winnie(ctx):
  em = discord.Embed(title = 'Tuxedo Winnie Meme', description = "type any text you want and the bot will write it inside the tuxedo winnie meme", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi winnie <FirstWord> <SecondWord>')
  em.add_field(name = 'Notice', value = 'If you want the bot to type multiple words, please write each sentence in double Qutoes', inline = False)
  em.add_field(name = '**Example**', value = 'rubi winnie "Rick Roll" "Tunak Tunak Tun"', inline = False)
  
  await ctx.send(embed = em)

@help.command()
async def drawuno(ctx):
  em = discord.Embed(title = 'Draw 25 cards meme', description = "type any text you want and the bot will write it inside the Draw 25 uno cards meme", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi drawuno <FirstWord> <SecondWord>')
  em.add_field(name = 'Notice', value = 'If you want the bot to type multiple words, please write each sentence in double Qutoes', inline = False)
  em.add_field(name = '**Example**', value = 'rubi drawuno "Stop Swearing" "My Grandpa"', inline = False)
  
  await ctx.send(embed = em)

@help.command()
async def mimicpower(ctx):
  em = discord.Embed(title = 'Look what they need to mimic a fraction...', description = "type any text you want and the bot will write it inside the overused, Look what they need to mimic a fraction of our power meme", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi mimicpower "FirstSentence" <SecondSentence>')
  em.add_field(name = 'Notice', value = 'If you want the bot to type multiple words as a sentence, please write each sentence in double Qutoes', inline = False)
  em.add_field(name = '**Example**', value = 'rubi mimicpower "Tryhard Noobs" "Pro Players"', inline = False)
  
  await ctx.send(embed = em)

@help.command()
async def yellcat(ctx):
  em = discord.Embed(title = 'A women yelling at a cat meme', description = "type any text you want and the bot will write it inside the dead, A women yelling at a cat meme", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi yellcat "FirstSentence" "SecondSentence"')
  em.add_field(name = 'Notice', value = 'Please type each sentence inside double quotes otherwise the bot wouldnt understand them as a sentence', inline = False)
  em.add_field(name = '**Example**', value = 'rubi yellcat "14 year olds calling me racist" "me who made a joke on my own race"', inline = False)
  
  await ctx.send(embed = em)

@help.command()
async def buffdoge(ctx):
  em = discord.Embed(title = 'Buff doge vs cheems meme', description = "type any text you want and the bot will write it inside the dead, Buff doge vs cheems meme", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi buffdoge "FirstHeading" "BuffDogeText" "SecondHeading" "CheemsText"')
  em.add_field(name = 'Notice', value = 'Please type each sentence inside double quotes otherwise the bot wouldnt understand them as a sentence', inline = False)
  em.add_field(name = '**Example**', value = 'rubi buffdoge "Youtubers back in 2013:" "People watch me because of good vids" "youtubers now" "plzzz guys subscribe for giveaway"', inline = False)
  
  await ctx.send(embed = em)

@help.command()
async def think(ctx):
  em = discord.Embed(title = 'Think [blank] think!', description = "type any text you want and the bot will write it inside the omni man think meme", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi think <FirstWord>')
  em.add_field(name = 'Notice', value = 'If you want the bot to type multiple words, please write the sentence in double Qutoes', inline = False)
  em.add_field(name = '**Example**', value = 'rubi think "Pewds and jack"', inline = False)
  
  await ctx.send(embed = em)

@help.command()
async def average(ctx):
  em = discord.Embed(title = 'Average Fan vs average enjoyer meme', description = "Type any text you want and the bot will write it inside the average fan vs average enjoyer meme", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi average <FirstWord> <SecondWord>')
  em.add_field(name = 'Notice', value = 'If you want the bot to type multiple words, please write each sentence in double Qutoes', inline = False)
  em.add_field(name = '**Example**', value = 'rubi average "Rick Roll" "Tunak Tunak Tun"', inline = False)
  
  await ctx.send(embed = em)


@help.command()
async def balance(ctx):
  em = discord.Embed(title = 'Balance', description = 'Tells the money you have in your wallet and bank', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi balance')
  
  await ctx.send(embed = em)

@help.command()
async def beg(ctx):
  em = discord.Embed(title = 'Beg', description = 'Beg for money from people (please use the balance command so that you actually have a bank before using this command)', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi beg')
  
  await ctx.send(embed = em)

@help.command()
async def power(ctx):
  em = discord.Embed(title = 'POWER', description = 'type any text you want and the bot will write it inside the "what gives people feeling of power meme"', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi power [TEXT]')
  
  await ctx.send(embed = em)

@help.command()
async def ping(ctx):
  em = discord.Embed(title = 'Ping', description = 'Tells the ping of the bot in milli-seconds', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi ping')
  
  await ctx.send(embed = em)

@help.command()
async def ban(ctx):
  em = discord.Embed(title = 'Ban', description = 'Bans a given member and with a reason too (optional)', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi ban <memberName> [reason]')
  
  await ctx.send(embed = em)

@help.command()
async def mute(ctx):
  em = discord.Embed(title = 'Ban', description = 'mutes a given member and with a reason too (optional)', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi mute <memberName> [reason]')
  
  await ctx.send(embed = em)

@help.command()
async def clear(ctx):
  em = discord.Embed(title = 'Clear', description = 'Clears the amount of the server messages you want to be deleted', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi clear <amount>')
  
  await ctx.send(embed = em)

@help.command()
async def eightball(ctx, aliases = ['8ball']):
  em = discord.Embed(title = '8Ball', description = 'Asks a magical 8ball your fate', color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi 8ball [question]')
  
  await ctx.send(embed = em)

@help.command()
async def heart(ctx):
  em = discord.Embed(title = 'Heart', description = 'Add heart and sparkles to any text you want', color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi heart [text]')
  
  await ctx.send(embed = em)

@help.command()
async def quote(ctx):
  em = discord.Embed(title = 'Quote', description = 'make any text look like a quote', color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi quote [text]')
  
  await ctx.send(embed = em)

@help.command()
async def catto(ctx):
  em = discord.Embed(title = 'Catto', description = 'get a random cat picture UwU', color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi catto')
  
  await ctx.send(embed = em)

@help.command()
async def doggo(ctx):
  em = discord.Embed(title = 'doggo', description = 'get a random dog picture OwO', color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi doggo')
  
  await ctx.send(embed = em)

@help.command()
async def foxy(ctx):
  em = discord.Embed(title = 'foxy', description = 'get a random fox picture', color = discord.Color.orange())

  em.add_field(name = '**Syntax**', value = 'rubi foxy')
  
  await ctx.send(embed = em)


@help.command()
async def pfp(ctx):
  em = discord.Embed(title = 'pfp', description = "get another user's profile picture. Tip: mentioning no member will show your pfp", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi pfp {member}')
  
  await ctx.send(embed = em)

@help.command()
async def birb(ctx):
  em = discord.Embed(title = 'Birb', description = "get a random bird picture", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi birb')
  
  await ctx.send(embed = em)

@help.command()
async def shibe(ctx):
  em = discord.Embed(title = 'Shibe', description = "get a random Shiba Inu picture", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi shibe')
  
  await ctx.send(embed = em)

@help.command()
async def panda(ctx):
  em = discord.Embed(title = 'Panda', description = "get a random Panda picture", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi panda')
  
  await ctx.send(embed = em)

@help.command()
async def dadjoke(ctx):
  em = discord.Embed(title = 'Dadjoke', description = "get a random Dad joke", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi dadjoke')
  
  await ctx.send(embed = em)

@help.command()
async def meme(ctx):
  em = discord.Embed(title = 'Meme', description = "get a random meme from reddit", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi meme')
  
  await ctx.send(embed = em)

@help.command()
async def creepypasta(ctx):
  em = discord.Embed(title = 'CreepyPasta', description = "get a random creepypasta from reddit", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi creepypasta')
  
  await ctx.send(embed = em)

@help.command()
async def sum(ctx):
  em = discord.Embed(title = 'Sum', description = "add numbers (upto 5 numbers)", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi sum [num1] [num2]')
  
  await ctx.send(embed = em)

@help.command()
async def subtract(ctx):
  em = discord.Embed(title = 'Subtract', description = "subtract numbers (upto 5 numbers)", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi subtract [num1] [num2]')
  
  await ctx.send(embed = em)

@help.command()
async def multiply(ctx):
  em = discord.Embed(title = 'Multiply', description = "multiply numbers (upto 2 numbers at the moment)", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi multiply [num1] [num2]')
  
  await ctx.send(embed = em)

@help.command()
async def divide(ctx):
  em = discord.Embed(title = 'Divide', description = "divide numbers (upto 2 numbers at the moment)", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi divide [num1] [num2]')
  
  await ctx.send(embed = em)


@help.command()
async def square(ctx):
  em = discord.Embed(title = 'Square', description = "Square numbers ", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi square [number]')
  
  await ctx.send(embed = em)

@help.command()
async def pmsquare(ctx):
  em = discord.Embed(title = 'Pmsquare', description = "Calculate the perimetre of a square with a given side", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi pmsquare [side]')
  
  await ctx.send(embed = em)

@help.command()
async def areasquare(ctx):
  em = discord.Embed(title = 'Areasquare', description = "Calculate the Area of a square with a given side", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi areasquare [side]')
  
  await ctx.send(embed = em)

@help.command()
async def pmrect(ctx):
  em = discord.Embed(title = 'Pmsquare', description = "Calculate the perimetre of a rectangle with a given length and breadth", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi pmrect [l] [b]')
  
  await ctx.send(embed = em)

@help.command()
async def arearect(ctx):
  em = discord.Embed(title = 'Areasquare', description = "Calculate the Area of a rectangle with a given length and breadth", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi arearect [l] [b]')
  
  await ctx.send(embed = em)


@help.command()
async def circum(ctx):
  em = discord.Embed(title = 'Circum', description = "Calculate the Circumference of a circle with a given Radius", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi circum [radius]')
  
  await ctx.send(embed = em)

@help.command()
async def areacircle(ctx):
  em = discord.Embed(title = 'Areacircle', description = "Calculate the Area of a circle with a given Radius", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi areacircle [radius]')
  
  await ctx.send(embed = em)

@help.command()
async def dankmeme(ctx):
  em = discord.Embed(title = 'DankMeme', description = "Get a random dank meme from r/dankmemes", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi dankmeme')
  
  await ctx.send(embed = em)

@help.command()
async def reddit(ctx):
  em = discord.Embed(title = 'Reddit', description = "Get a random post from any subreddit you desire (you must not write r/before the subreddit name)", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi reddit {subredditName}')
  
  await ctx.send(embed = em)

@help.command()
async def slowmode(ctx):
  em = discord.Embed(title = 'SlowMode', description = "Set a time interval for posts to stop spam", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi slowmode {secondsInNumber}')
  
  await ctx.send(embed = em)

@help.command()
async def chance(ctx):
  em = discord.Embed(title = 'Chance', description = "ask the bot a question and it will reveal the chance of it being true (not really)", color = discord.Color.purple())

  em.add_field(name = '**Syntax**', value = 'rubi chance [question]')
  
  await ctx.send(embed = em)

@help.command()
async def level(ctx):
  em = discord.Embed(title = 'level', description = "Shows you your level and xp", color = discord.Color.green())

  em.add_field(name = '**Syntax**', value = 'rubi level')
  
  await ctx.send(embed = em)


@help.command()
async def cpustats(ctx):
  em = discord.Embed(title = 'CPU Stats', description = "tells the information about the bot's cpu", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi cpustats')
  
  await ctx.send(embed = em)

@help.command()
async def memstats(ctx):
  em = discord.Embed(title = 'Memory Stats', description = "tells the information about the bot's memory", color = discord.Color.blue())

  em.add_field(name = '**Syntax**', value = 'rubi memstats')
  
  await ctx.send(embed = em)

# events start here

# @client.event
# async def on_member_join(member):
#   print(f'{member} joined')
#   guild = client.get_guild(816723738363428864)
#   channel = guild.get_channel(816723739344371723)
#   await channel.send(f'{member} {random.choice(joined)}')

# @client.event
# async def on_member_remove(member):
#   print(f'{member} {random.choice(went)}')
#   guild = client.get_guild(816723738363428864)
#   channel = guild.get_channel(816723739344371723)
#   await channel.send(f'{member} {random.choice(went)}')




#commands here !!


#cat img command
@client.command()
async def catto(ctx):
  response = requests.get('https://aws.random.cat/meow')
  data = response.json()
  await ctx.send(data['file'])

  embed = discord.Embed(title="Catto!")
  embed.set_image(url=data)
  await ctx.send(embed=embed)


#dog img command
@client.command()
async def doggo(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = discord.Embed(title="Doggo!", color=random.choice(colors))
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)



#latency command
@client.command()
async def ping(ctx):
  await ctx.send(f'time being taken to transfer data packets is {round(client.latency * 1000)}ms')


#bird image command
@client.command()
async def birb(ctx):
  response_birb = requests.get('https://some-random-api.ml/img/birb')
  birb = response_birb.json()
  birbpic = birb['link']
  embed = discord.Embed(title = 'Birb!!', color = random.choice(colors))
  embed.set_image(url = birbpic)
  embed.set_footer(text = 'api: https://some-random-api.ml/img/birb')
  await ctx.send(embed = embed)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def spitfoxy(ctx, num = 2):
  if num <= 10:
    for number in range(num):
      response_foxy = requests.get('https://randomfox.ca/floof')
      fox = response_foxy.json()
      foxurl = fox['image']
      embed = discord.Embed(title = 'FOXY!!', color = random.choice(colors))
      embed.set_image(url = foxurl)
      embed.set_footer(text = 'api: https://randomfox.ca/floof')
      await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = 'I cant spit more than 10 images at once!', color = random.choice(colors))
    await ctx.send(embed = embed)

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def spitcatto(ctx, num = 2):
  if num <= 10:
    for number in range(num):
      response = requests.get('https://aws.random.cat/meow')
      data = response.json()
      await ctx.send(data['file'])

  else:
    embed = discord.Embed(title = 'I cant spit more than 10 images at once!', color = random.choice(colors))
    await ctx.send(embed = embed)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def spitdoggo(ctx, num = 2):
  if num <= 10:
    for number in range(num):
      async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()
        request2 = await session.get('https://some-random-api.ml/facts/dog')
        factjson = await request2.json()

      embed = discord.Embed(title="Doggo!", color=random.choice(colors))
      embed.set_image(url=dogjson['link'])
      embed.set_footer(text=factjson['fact'])
      await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title = 'I cant spit more than 10 images at once!', color = random.choice(colors))
    await ctx.send(embed = embed)



@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def spitbirb(ctx, num = 2):
  if num <= 10:
    for number in range(num):
      response_birb = requests.get('https://some-random-api.ml/img/birb')
      birb = response_birb.json()
      birbpic = birb['link']
      embed = discord.Embed(title = 'Birb!!', color = random.choice(colors))
      embed.set_image(url = birbpic)
      embed.set_footer(text = 'api: https://some-random-api.ml/img/birb')
      await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = 'I cant spit more than 10 images at once!', color = random.choice(colors))
    await ctx.send(embed = embed)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def spitpanda(ctx, num = 2):
  if num <= 10:
    for number in range(num):
      res = requests.get('https://some-random-api.ml/img/panda')
  
      panda = res.json()
      pandapic = panda['link']
      embed = discord.Embed(title = 'Panda!!', color = random.choice(colors))
      embed.set_image(url = pandapic)
      embed.set_footer(text = 'api: https://some-random-api.ml/img/panda')
      await ctx.send(embed = embed)
  else:
      embed = discord.Embed(title = 'I cant spit more than 10 images at once!', color = random.choice(colors))
      await ctx.send(embed = embed)



  
      
      

#shibe img command
@client.command(aliases = ["shiba", "doge"])
async def shibe(ctx):
  response = requests.get('http://shibe.online/api/shibes')
  data = response.json()

  def listToString(s): 
    
    str1 = "" 
      
    for ele in s: 
        str1 += ele  
     
    return str1 

  embed = discord.Embed(title = 'Shiba!!', color = random.choice(colors))
  embed.set_image(url = listToString(data))
  embed.set_footer(text = 'api: http://shibe.online/api/shibes')
  await ctx.send(embed = embed)


#foxy image command
@client.command()
async def foxy(ctx):
  response_foxy = requests.get('https://randomfox.ca/floof')
  fox = response_foxy.json()
  foxurl = fox['image']
  embed = discord.Embed(title = 'FOXY!!', color = random.choice(colors))
  embed.set_image(url = foxurl)
  embed.set_footer(text = 'api: https://randomfox.ca/floof')
  await ctx.send(embed = embed)


#panda image command
@client.command()
async def panda(ctx):
  res = requests.get('https://some-random-api.ml/img/panda')
  
  panda = res.json()
  pandapic = panda['link']
  embed = discord.Embed(title = 'Panda!!', color = random.choice(colors))
  embed.set_image(url = pandapic)
  embed.set_footer(text = 'api: https://some-random-api.ml/img/panda')
  await ctx.send(embed = embed)
  
  

@client.command()
async def pfp(ctx, member : discord.Member = None):
  if member != None:
    pfp = member.avatar_url
    embed = discord.Embed(title = f"{member}s pfp", value = '1F1F1F')
    embed.set_image(url = pfp)
    await ctx.send(embed = embed)
  else:
    pfp = ctx.author.avatar_url
    embed = discord.Embed(title = f"{ctx.author}s pfp", value = '1F1F1F')
    embed.set_image(url = pfp)
    await ctx.send(embed = embed)




#8ball answer command
@client.command(aliases = ['eightball', '8ball'])
async def _8ball(ctx, *, question):
  response = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
  await ctx.send(f'Question: {question}\n Answer: {random.choice(response)}')


#text modifiers
@client.command()
async def heart(ctx, *, heart_query):
  await ctx.send(f':heart: :sparkles: {heart_query} :heart: :sparkles:')

@client.command()
async def quote(ctx, *, quote_query):
  await ctx.channel.purge(limit = 1)
  embed=discord.Embed(description= f'" {quote_query} "', color=random.choice(colors))
  await ctx.send(embed = embed)



#purge command
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 6):

  if amount > 100:
    sun = False
  else:
    sun = True

  if sun == True:
    await ctx.channel.purge(limit = amount + 1)
  else:
    embed = discord.Embed(title = "You can't clear more than 100 messages at a time!", color = random.choice(colors))
    await ctx.send(embed = embed)


#kick command
@client.command()
@commands.has_permissions(administrator=True,kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
  await member.kick(reason = reason)
  embed = discord.Embed(title = f'Kicked {member.mention}', color = random.choice(colors))
  embed.set_footer(text = reason)
  await ctx.send(embed = embed)


@client.command()
@commands.has_permissions(administrator=True,ban_members=True)
async def ban(ctx, member : discord.Member, *, reason = None):
  await member.ban(reason = reason)
  await ctx.send(f'Banned {member.mention}')

@client.command()
async def dadjoke(ctx):
    """Gets a random dad joke."""
    api = 'https://icanhazdadjoke.com/'
    async with aiohttp.request('GET', api, headers={'Accept': 'text/plain'}) as r:
      result = await r.text()
    await ctx.send('`' + result + '`')

@client.command()
async def sum(ctx, num1, num2, num3 = 0, num4 = 0, num5 = 0):
  
  result = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
  embed = discord.Embed(title = result, color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def subtract(ctx, num1, num2, num3 = 0, num4 = 0, num5 = 0):
  result = int(num1) - int(num2) - int(num3) - int(num4) - int(num5)
  embed = discord.Embed(title = result, color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def multiply(ctx, num1, num2):
  result = int(num1) * int(num2)
  embed = discord.Embed(title = result, color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def divide(ctx, num1, num2):

  result = int(num1) / int(num2)
  embed = discord.Embed(title = result, color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def square(ctx, num):
  result = int(num) * int(num)
  embed = discord.Embed(title = result, color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def pmsquare(ctx, side):
  result = int(side) * 4
  embed = discord.Embed(title = f'the perimetre of the square is {result}', color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def areasquare(ctx, side):
  result = int(side) * int(side)
  embed = discord.Embed(title = f'the area of the square is {result}', color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def pmrect(ctx, l, b):
  result = (int(l) * 2) + (int(b) * 2)
  embed = discord.Embed(title = f'the perimetre of the rectangle is {result}', color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def arearect(ctx, l, b):
  result = int(l) * int(b)
  embed = discord.Embed(title = f'the area of the rectangle is {result}', color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def circum(ctx, radius):
  result = 2 * 3.14 * int(radius)
  rounded = round(result)
  embed = discord.Embed(title = f'the round offed Circumference of the circle is {rounded} and the undrounded off circumference is {result}', color = discord.Colour.blurple())
  await ctx.send(embed = embed)

@client.command()
async def areacircle(ctx, radius):
  result = 3.14 * (int(radius) * int(radius))
  rounded = round(result)
  embed = discord.Embed(title = f'the round offed area of the circle is {rounded} and the undrounded off circumference is {result}', color = discord.Colour.blurple())
  await ctx.send(embed = embed)



@client.command()
async def meme(ctx):
  res = requests.get('https://memes.blademaker.tv/api/memes')
  meme = res.json()
  memeimg = meme['image']
  meme_title = meme['title']
  status = meme['ups']
  embed = discord.Embed(title = meme_title, color = random.choice(colors))
  embed.set_image(url = memeimg)
  embed.set_footer(text = f'upvotes: {status}')
  await ctx.send(embed = embed)

@client.command()
async def dankmeme(ctx):
  res = requests.get('https://memes.blademaker.tv/api/dankmemes')
  meme = res.json()
  memeimg = meme['image']
  meme_title = meme['title']
  status = meme['ups']
  embed = discord.Embed(title = meme_title, color = random.choice(colors))
  embed.set_image(url = memeimg)
  embed.set_footer(text = f'updootes: {status}')
  await ctx.send(embed = embed)

@client.command()
async def creepypasta(ctx):
  res = requests.get('https://memes.blademaker.tv/api/creepypasta')
  creepy = res.json()
  memeimg = creepy['image']
  meme_title = creepy['title']
  author = creepy['author']
  embed = discord.Embed(title = meme_title, color = random.choice(colors))
  embed.set_image(url = memeimg)
  embed.set_footer(text = f'updootes: {author}')
  await ctx.send(embed = embed)



@client.command()
async def reddit(ctx, *, subreddit = None):
      if subreddit != None:
        res = requests.get(f'https://memes.blademaker.tv/api/{subreddit}')
        request = res.json()
        try:
          title = request['title']
          img = request['image']
          upvotes = request['ups']
          author = request['author']
          nsfw = request['nsfw']

          if nsfw == False:
            embed = discord.Embed(title = title, color = random.choice(colors))
            embed.set_image(url = img)
            embed.set_footer(text = f'updootes: {upvotes} || author: u/{author}')
            await ctx.send(embed = embed)

          if nsfw == True:
            if ctx.channel.is_nsfw():
              embed = discord.Embed(title = title, color = random.choice(colors))
              embed.set_image(url = img)
              embed.set_footer(text = f'updootes: {upvotes} || author: u/{author}')
              await ctx.send(embed = embed)
            else:
              await ctx.send('The subreddit or post is nsfw! Please use a nsfw channel to view them')



        except:
          await ctx.send('The subreddit either does not exist or has text as the post ')
      else: 
        await ctx.send('NANI!!??..YOU NEED TO TYPE A SUBREDDIT NAME TOO!')

@client.command()
@commands.has_permissions(manage_messages = True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"the slowmode is now {seconds} seconds!")

@client.command()
async def chance(ctx, *, suggestion):
  number = random.randint(1, 100)
  message = await ctx.send("Reading the data...")
  await asyncio.sleep(1)
  await message.edit(content="Creating advanced machine learning models")
  await asyncio.sleep(1.5)
  await message.edit(content=f"training the models")
  await asyncio.sleep(1.5)
  await message.edit(content="Taking a coffee brake ( •̀ ω •́ )✧")
  await asyncio.sleep(2)
  await message.edit(content="analyzing...")
  await asyncio.sleep(2)
  await message.edit(content=f"according to my calculation there is a {number}% chance  ψ(｀∇´)ψ")

@client.command(description="Mutes the specified user.")
@commands.has_permissions(administrator=True,ban_members=True, kick_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")




# @client.cmomand()
# async def addrole(ctx, member: discord.Member, *,  role_name):
#   role = discord.utils.get(guild.roles, name=role_name)
#   member.add_roles(role, reason = None)

# with open('reports.json', encoding='utf-8') as f:
#   try:
#     report = json.load(f)
#   except ValueError:
#     report = {}
#     report['users'] = []




# @client.command(aliases = ['inform', 'w'] , pass_context = True)
# @has_permissions(manage_roles=True, ban_members=True)
# async def warn(ctx,user:discord.User,*reason:str):
#   if not reason:
#     await ctx.send("Please provide a reason")
#     return
#   reason = ' '.join(reason)
#   for current_user in report['users']:
#     if current_user['name'] == user.name:
#       current_user['reasons'].append(reason)
#       break
#   else:
#     report['users'].append({
#       'name':user.name,
#       'reasons': [reason,]
#     })
#   with open('reports.json','w+') as f:
#     json.dump(report,f)



# @client.command(pass_context = True)
# async def warnings(ctx,user:discord.User):
#   for current_user in report['users']:
#     if user.name == current_user['name']:
#       await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
#       break
#   else:
#     await ctx.send(f"{user.name} has never been reported")  



# @warn.error
# async def kick_error(error, ctx):
#   if isinstance(error, MissingPermissions):
#       text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#       await ctx.send(ctx.message.channel, text)

# @client.command()
# @has_permissions(manage_roles=True, ban_members=True)
# async def warning(ctx, member: discord.Member):
#   warning = open('reports.json', )
#   data = json.load(warning)
#   users = data['users']
#   user_list = users[0]
#   str(member)
#   name = user_list['name']
#   reasons = user_list['reasons']
#   warnings = tuple(reasons)
#   embed = discord.Embed(title = f'user: {name}', description = f'reasons: {warnings}', color = random.choice(colors))
#   await ctx.send(embed = embed)
  
# @client.command()
# async def wikisearch(ctx, *, query):
#   result = wikipedia.page(query)
#   res = list(result.content)
  
#   embed = discord.Embed()
#   await ctx.send(embed=embedVar)


#   await ctx.send(embed = embed)



@client.command()
async def kill(ctx, member: discord.Member):
    await ctx.send(f'{member.mention} {random.choice(scenerios)}')



# @client.command()
# async def blur(ctx, member : discord.Member):
#   pfp = member_pfp = member.avatar_url
#   im = Image.open(pfp)
  
#   blurImage = im.filter(ImageFilter.BLUR)


#   await ctx.send(blurImage.show())

@client.command()
async def wordgame(ctx):
  res = requests.get('https://random-word-api.herokuapp.com/word?number=1')

  response = res.json()

  message = await ctx.send("On Your Marks...")
  await asyncio.sleep(1)

  await message.edit(content="Get Set...")
  await asyncio.sleep(1.5)
  await message.edit(content=f"GOOOOO")
  await asyncio.sleep(0.5)
  word = response[0]
  await message.edit(content=word)

 

  # if message.content.startswith('testing'):
  #   print('i made this far')
  #   await message.channel.send('You won!')

  # await message.edit(content= f'the word is: {word}')


  # if message.content == word:
  #     await ctx.send('you won')
  # else:
  #   await asyncio.sleep(10)
  #   await ctx.send('10 seconds passed dumbass')

@client.event
async def on_message(message):
    if not message.author.bot:
        print('function load')
        with open('level.json','r') as f:
            users = json.load(f)
            print('file load')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open('level.json','w') as f:
            json.dump(users, f)
    await client.process_commands(message)

    if message.author == client.user:
      return

    if message.content.startswith('-_-help'):
      await message.channel.send('-_- was my old prefix!! my new prefix is rubi. Please type rubi help to get started :)')



async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
async def add_experience(users, user, exp, server):
  users[str(user.guild.id)][str(user.id)]['experience'] += exp

async def level_up(users, user, channel, server):
  experience = users[str(user.guild.id)][str(user.id)]['experience']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  lvl_end = int(experience ** (1/4))
  if str(user.guild.id) != '757383943116030074':
    if lvl_start < lvl_end:
      await channel.send('{} has leveled up to Level {}'.format(user.mention, lvl_end))
      users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@client.command(aliases = ['rank','lvl'])
async def level(ctx,member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('level.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP " ,color = random.choice(colors))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
      with open('level.json','r') as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['experience']
      embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP" ,color = discord.Color.green())
      embed.set_author(name = member, icon_url = member.avatar_url)

      await ctx.send(embed = embed)




@client.command()
async def cpustats(ctx):
  cores = psutil.cpu_count()


  usage = psutil.cpu_percent(1)

  load = psutil.getloadavg()
  
  embed = discord.Embed(title = 'CPU', color = random.choice(colors))
  embed.add_field(name = 'Cores', value = cores)
  embed.add_field(name = 'Usage', value = f'{usage}%')
  embed.add_field(name = 'Load', value = f'{load[0]}%')

  await ctx.send(embed = embed)

@client.command()
async def memstats(ctx):
  mem = psutil.virtual_memory()
  embed = discord.Embed(title = 'MEMORY', color = random.choice(colors))

  memo = mem[0]
  memo = memo / 1024
  meme = memo / 1024
  moi = meme / 1024
  moii = round(moi)
  
  ava = mem[1]
  ava = ava / 1024
  avu = ava / 1024
  avo = avu / 1024
  avui = round(avo)

  embed.add_field(name = 'Total Memory', value = f'{moii} GB')
  embed.add_field(name = 'Available', value = f'{avui} GB')
  embed.add_field(name = 'Usage', value = f'{mem[2]}%')

  await ctx.send(embed = embed)



# @client.command()
# async def balance(ctx, user = None):
#   if user == None:
#       await open_account(ctx.author)
#       user = ctx.author
#       users = await get_bank_data()

#       wallet_amt = users[str(user.id)]["wallet"]
#       bank_amt = users[str(user.id)].get("bank", 0)

#       em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.red())
#       em.add_field(name = "Wallet Balance",value = wallet_amt)
#       em.add_field(name = "Bank Balance",value = bank_amt)
#       await ctx.send(embed = em)
#   else:
#       await open_account(user)
#       users = await get_bank_data()

#       wallet_amt = users[str(user.id)]["wallet"]
#       bank_amt = users[str(user.id)].get("bank", 0)

#       em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.red())
#       em.add_field(name = "Wallet Balance",value = wallet_amt)
#       em.add_field(name = "Bank Balance",value = bank_amt)
#       await ctx.send(embed = em)

# @client.event()
# async def on_command_error(ctx, error):
#   if isinstance(error, commands.CommandOnCooldown):
#     msg = '**STILL ON COOLDOWN!!**, Please try again in {:.2f}s'.format(error.entry_after)
#     await ctx.message.send(msg)



# @client.command()
# @commands.cooldown(1, 30, commands.BucketType.user)
# async def beg(ctx):
#         await open_account(ctx.author)

#         users = await get_bank_data()

#         user = ctx.author

#         earnings = random.randrange(345)

#         await ctx.send(f"Someone gave you {earnings} coins!!")


#         users[str(user.id)]["wallet"] += earnings

#         with open("mainbank.json","w") as f:
#               json.dump(users,f)

# minecrypto_cool = 2300


# @client.command()
# @commands.cooldown(1, 2300, commands.BucketType.user)
# async def minecrypto(ctx):
#         await open_account(ctx.author)

#         users = await get_bank_data()

#         user = ctx.author

#         earnings = random.randrange(500)
#         electricity_cost = random.randint(100, 350)


#         embed = discord.Embed(title = 'Spent/Earned', color = random.choice(colors), inline = False)
#         embed.add_field(name = 'Spent', value = f'The electricity cost to mine was: {electricity_cost}',inline = False)
#         embed.add_field(name = 'Earned', value = f'You mined: {earnings} Boltos!!',inline = False)
#         embed.add_field(name = 'Profit/loss', value = f'{earnings - electricity_cost} Boltos',inline = False)
#         await ctx.send(embed = embed)



#         users[str(user.id)]["wallet"] -= electricity_cost
#         users[str(user.id)]["wallet"] += earnings

#         with open("mainbank.json","w") as f:
#               json.dump(users,f)

        
        




# @beg.error
# async def command_name_error(ctx, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
#         await ctx.send(embed=em)


@spitdoggo.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"To prevent spam, you can only use this command 2 times per minute",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
        await ctx.send(embed=em)
@spitcatto.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"To prevent spam, you can only use this command 2 times per minute",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
        await ctx.send(embed=em)

@spitbirb.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"To prevent spam, you can only use this command 2 times per minute",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
        await ctx.send(embed=em)

@spitpanda.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"To prevent spam, you can only use this command 2 times per minute",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
        await ctx.send(embed=em)

@spitfoxy.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"To prevent spam, you can only use this command 2 times per minute",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
        await ctx.send(embed=em)

# @minecrypto.error
# async def command_name_error(ctx, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         em = discord.Embed(title=f"Slow it down bro!",description=f"Try again in {error.retry_after:.2f}s.", color=random.choice(colors))
#         await ctx.send(embed=em)

    
# @client.command()
# async def withdraw(ctx,amount = None):
#     await open_account(ctx.author)
    
#     if amount == None:
#         await ctx.send("Please enter an ammount")
#         return

#     bal = await update_bank(ctx.author)


#     amount = int(amount)
#     if amount>bal[1]:
#         await ctx.send("You don't have that much money!")
#         return
#     if amount<0:
#         await ctx.send("Amount must be positive!")
#         return
    
#     await update_bank(ctx.author,amount)
#     await update_bank(ctx.author,-1*amount,"bank")

#     await ctx.send(f"you withdrew {amount} coins")







# async def open_account(user):

#     users = await get_bank_data()
    
#     if str(user.id) in users:
#         return False
#     else:
#         users[str(user.id)] = {}
#         users[str(user.id)]["wallet"] = 0
#         users[str(user.id)]["bank"] = 0

#     with open("mainbank.json","w") as f:
#         json.dump(users,f)
#     return True



# async def get_bank_data():
#     with open("mainbank.json","r") as f:
#         users = json.load(f)

#     return users


# async def update_bank(user,change = 0,mode = "wallet"):
#     users = await get_bank_data()

#     users[str(user.id)][mode] += change

#     with open("mainbank.json","w") as f:
#           json.dump(users,f)

#     bal = [users[str(user.id)]["wallet"].users[str(user.id)]["bank"]]
#     return bal
  


@client.command()
async def wanted(ctx, member:discord.Member = None):
  if member == None:
    member = ctx.author
  wanted = Image.open("wanted.jpg")

  asset = ctx.author.avatar_url_as(size = 128)

  data = BytesIO(await asset.read())

  pfp = Image.open(data)

  pfp = pfp.resize((177,177))
  wanted.paste(pfp, (120, 212))
  wanted.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))

# @client.command()
# async def backstab(ctx, member : discord.Member):
#   img = Image.open("backstab.jpg")
#   author = ctx.author
#   stabbed = member.avatar_url_as(size = 128)
#   authory = BytesIO(await author.read())
#   stabby = BytesIO(await stabbed.read())

#   pfp = Image.open(authory)
#   pfp2 = Image.open(stabby)



#   pfp = pfp.resize((177,177))
#   img.paste(pfp, (120, 212))
#   img.save("profile.jpg")

#   pfp = pfp.resize((177,177))
#   img.paste(pfp, (300, 412))
#   img.save("profile2.jpg")

#   await ctx.send(file = discord.File("profile.jpg"))



@client.command()
async def power(ctx, *, query):
  img = Image.open("status.jpg")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("CourierPrime-Bold.ttf", 16)
  text = query


  draw.text((5, 183), text, (0,0,0), font = font)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))



@client.command()
async def info(ctx, user: discord.Member):
      asset = user.avatar_url_as(size = 128)
      name = user.name
      nick = user.display_name
      creation = user.created_at
      toprole = user.top_role
      joined = user.joined_at

      embed = discord.Embed(title = f"{name}'s Info", color = random.choice(colors))
      embed.set_image(url = asset)
      embed.add_field(name = 'Nickname', value = nick)
      embed.add_field(name = 'Date Created', value = creation.date())
      embed.add_field(name = 'Top Role', value = toprole)
      embed.add_field(name = 'Joined The Server At', value = joined.date())

      await ctx.send(embed = embed)

    

mainshop = [{'name':'watch','price' : '3000', 'description' : 'time'},
            {'name':'Laptop','price' : '15000', 'description' : 'Work'},
            {'name':'PC','price' : '20000', 'description' : 'Gaming'}]


# @client.command()
# async def shop(ctx):
#   embed = discord.Embed(title = 'Shop')

#   for item in mainshop:
#     name = item['name']
#     price = item['price']
#     description = item['description']
#     embed.add_field(name = name, value = f'{price}boltos | {description}')

#     await ctx.send(embed = embed)

@client.command()
async def winnie(ctx, word1 = None, word2 = None):
  img = Image.open("Tuxedo-Winnie-The-Pooh.png")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("Raleway-Thin.ttf", 46)
  font2 = ImageFont.truetype("DancingScript-Regular.ttf", 46)
  text = word1
  text2 = word2





  draw.text((420, 140), text, (0,0,0), font = font)
  draw.text((420, 440), text2, (0,0,0), font = font2)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))

# @client.command()
# async def tictactoe(ctx, member : discord.Member):

@client.command()
async def think(ctx, text):
  img = Image.open("think.jpg")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("CourierPrime-Bold.ttf", 55)

  text = f'Think {text} think!'
  draw.text((200,660), text, (255, 221, 0), font = font)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))

@client.command()
async def drawuno(ctx, word1 = None, word2 = None):
  img = Image.open("drawuno.jpg")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("Raleway-Thin.ttf", 20)
  font2 = ImageFont.truetype("CourierPrime-Bold.ttf", 40)
  text = word1
  text2 = word2





  draw.text((120, 170), text, (0,0,0), font = font)
  draw.text((400, 170), text2, (255,255,255), font = font2)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))


@client.command()
async def mimicpower(ctx, word1 = None, word2 = None):
  img = Image.open("mimic.png")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("CourierPrime-Bold.ttf", 40)
  font2 = ImageFont.truetype("CourierPrime-Bold.ttf", 40)
  text = word1
  text2 = word2





  draw.text((80, 260), text, (255,255,255), font = font)
  draw.text((430, 900), text2, (19,19,38), font = font2)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))


@client.command()
async def buffdoge(ctx, word1 = None, word2 = None, word3 = None, word4 = None):
  img = Image.open("buffdoge.png")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("CourierPrime-Bold.ttf", 25)
  font2 = ImageFont.truetype("CourierPrime-Bold.ttf", 20)
  text = word1
  text2 = word2
  text3 = word3
  text4 = word4





  draw.text((60, 260), text, (0,0,0), font = font)
  draw.text((20, 550), text2, (0,0,0), font = font2)
  draw.text((710, 280), text3, (0,0,0), font = font)
  draw.text((530, 570), text4, (0,0,0), font = font2)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))


@client.command()
async def yellcat(ctx, word1 = None, word2 = None):
  img = Image.open("yellcat.jpg")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("CourierPrime-Bold.ttf", 20)
  font2 = ImageFont.truetype("CourierPrime-Bold.ttf", 20)
  text = word1
  text2 = word2





  draw.text((80, 500), text, (255,255,255), font = font)
  draw.text((710, 190), text2, (255,255,255), font = font2)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))

@client.command()
async def average(ctx, word1, word2):
  img = Image.open("average.jpg")
  
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("Montserrat-Regular.ttf", 46)
  text = word1
  text2 = word2


  draw.text((40, 120), text, (0,0,0), font = font)
  draw.text((520, 120), text2, (0,0,0), font = font)
  img.save("profile.jpg")

  await ctx.send(file = discord.File("profile.jpg"))


snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")



#error handlers
@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
      embed = discord.Embed(title = 'I could not find that member...', color = random.choice(colors))
      await ctx.send(embed = embed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
      embed = discord.Embed(title = 'I could not find that member...', color = random.choice(colors))
      await ctx.send(embed = embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
      embed = discord.Embed(title = 'I could not find that member...', color = random.choice(colors))
      await ctx.send(embed = embed)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
      embed = discord.Embed(title = 'I could not find that member...', color = random.choice(colors))
      await ctx.send(embed = embed)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(title = 'I dont have the permissions to mute this member', color = random.choice(colors))
      await ctx.send(embed = embed)

@pfp.error
async def userpfp_error(ctx, error):
    if isinstance(error, commands.BadArgument):
      embed = discord.Embed(title = 'I could not find that member...', color = random.choice(colors))
      await ctx.send(embed = embed)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have the permissions to do that!")
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please give all the required arguments!')



# @client.command()
# async def gamble(ctx, bet : int):
#   await open_account(ctx.author)

#   users = await get_bank_data()

#   user = ctx.author

#   bot_role = random.randint(1, 12)
#   player_role = random.randint(1, 12)




#   if player_role > bot_role:
#     profit = bet 

#     embed = discord.Embed(title = f'{ctx.author} Has Won!', color = random.choice(colors), inline = False)
#     embed.add_field(name = 'Bot rolled: ', value = f'**{bot_role}**',inline = True)
#     embed.add_field(name = f'{ctx.author} rolled: ', value = f'{player_role}',inline = True)
#     embed.add_field(name = 'You won:', value = f'{profit * 2} ⁁Boltos!', inline = False)
#     users[str(user.id)]["wallet"] += profit
#     await ctx.send(embed = embed)


#   elif player_role < bot_role:
#     loss = bet 

#     embed = discord.Embed(title = f'{ctx.author} Has lost :(', color = random.choice(colors), inline = False)
#     embed.add_field(name = 'Bot rolled: ', value = f'**{bot_role}**',inline = True)
#     embed.add_field(name = f'{ctx.author} rolled: ', value = f'{player_role}',inline = True)
#     embed.add_field(name = 'You lost:', value = f'{loss} Boltos :(', inline = False)
#     users[str(user.id)]["wallet"] -= loss
#     await ctx.send(embed = embed)
  
#   elif player_role == bot_role:

#     embed = discord.Embed(title = 'Match Tied!!', color = random.choice(colors), inline = False)
#     embed.add_field(name = 'Bot rolled: ', value = f'**{bot_role}**',inline = True)
#     embed.add_field(name = f'{ctx.author} rolled: ', value = f'{player_role}',inline = True)
#     embed.add_field(name = 'Tied!', value = f'Both the bot and you earned nothing!', inline = False)
#     await ctx.send(embed = embed)


#   with open("mainbank.json","w") as f:
#         json.dump(users,f)







@client.command()
async def invite(ctx):
  embed = discord.Embed(title = 'Invite Me To Your Server', color = random.choice(colors), url = " https://discord.com/api/oauth2/authorize?client_id=839461452913573888&permissions=8&scope=bot")
  await ctx.send(embed = embed)



@client.command()
async def pat(ctx, member: discord.Member):
  response_birb = requests.get('https://some-random-api.ml/animu/pat')
  birb = response_birb.json()
  birbpic = birb['link']
  embed = discord.Embed(title = f'{ctx.author} Pats {member} ', color = random.choice(colors))
  embed.set_image(url = birbpic)
  await ctx.send(embed = embed)


@client.command()
async def wink(ctx, member : discord.Member):
  response_birb = requests.get('https://some-random-api.ml/animu/wink')
  birb = response_birb.json()
  birbpic = birb['link']
  embed = discord.Embed(title = f'{ctx.author} Winked at {member} ', color = random.choice(colors))
  embed.set_image(url = birbpic)
  await ctx.send(embed = embed)


@client.command()
async def hug(ctx, member : discord.Member):
  response_birb = requests.get('https://some-random-api.ml/animu/hug')
  birb = response_birb.json()
  birbpic = birb['link']
  embed = discord.Embed(title = f'{ctx.author} Hugged  {member} ', color = random.choice(colors))
  embed.set_image(url = birbpic)
  await ctx.send(embed = embed)


# @client.command()
# async def wasted(ctx, member : discord.Member):
#   pfp = f"{member.avatar_url}"

  
#   new_pfp = str(pfp[:len(pfp)-10])

#   wasted = requests.get(f'https://some-random-api.ml/canvas/wasted/?avatar={new_pfp}')
#   await ctx.send(wasted)
  


keep_alive()
client.run(os.environ["TOKEN"])
client.run(os.getenv("TOKEN"))
