# -*- coding: utf-8 -*- 
from encodings import utf_8
from lib2to3.pgen2 import token
from turtle import end_fill 
import os, json, nextcord, logging, datetime, random, time ,sentry_sdk ,asyncio,openai,opencc,googletrans,requests
from googletrans import Translator
from opencc import OpenCC
from ssl import CHANNEL_BINDING_TYPES
from nextcord.ext import commands
from nextcord.ui import *
from nextcord import TextChannel
from nextcord.utils import get
server_id = 978680658740260865 # replace with your server ID
intents=nextcord.Intents.all() 
bot = commands.Bot(command_prefix='$',intents=nextcord.Intents.all()) 
translator = Translator()
with open ("test.json","r",encoding='utf8') as jfile:
  jdate=json.load(jfile)

@bot.command(name="ping", description="Get bot ping value.")
async def ping(ctx):
    bot_ping = round(bot.latency * 1000)
    await ctx.response.send_message(f"Bot's ping is {bot_ping}ms.")

@bot.message_command()
async def say(interaction: nextcord.Interaction, message: nextcord.Message):
    tw_to_cn=opencc.OpenCC('t2s')
    await interaction.response.send_message(tw_to_cn.convert(message.content), ephemeral=True)

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cod.{extension}')
    await ctx.send(f'load {extension} successful')
    print(f'-> Loaded {extension} successful!')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cod.{extension}')
    await ctx.send(f'unload {extension} succesful')
    print(f'-> Unloaded {extension} successful!')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cod.{extension}')
    await ctx.send(f'reload {extension} succesful')
    print(f'-> Reloaded {extension} successful!')
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

for filename in os.listdir('./cod'):
    if filename.endswith('.py'):
        bot.load_extension(f'cod.{filename[:-3]}')
        
if __name__ == "__main__":  
    bot.run(jdate['token'])