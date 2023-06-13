from .. import bot 
from telethon import events
import asyncio


@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(events):
  await events.reply("Hey this is Junaid Qureshi command")
  


@bot.on(events.NewMessage(incoming=True, pattern="/get"))
async def start(events):
  a=await events.reply("Hey this is Get command")
  await asyncio.sleep(3)
  await a.edit("this is edited message")
  
  

@bot.on(events.NewMessage(incoming=True, pattern="/eval"))
async def start(events):
  await events.reply("Hey this is eval command")
 