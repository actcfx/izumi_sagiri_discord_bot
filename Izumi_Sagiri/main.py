# -*- coding: utf-8 -*-
import os, json, nextcord, opencc
from googletrans import Translator
from nextcord.ext import commands
from nextcord.ui import *

server_id = 978680658740260865 # replace with your server ID
intents=nextcord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=nextcord.Intents.all())
translator = Translator()

with open("Izumi_Sagiri/test.json", "r", encoding='utf8') as jfile:
  jdate=json.load(jfile)

@bot.command(name="ping", description="Get bot ping value.")
async def ping(ctx):
    bot_ping = round(bot.latency * 1000)
    await ctx.response.send_message(f"Bot's ping is {bot_ping}ms.")

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
    await ctx.send(f'unload {extension} successful')
    print(f'-> Unloaded {extension} successful!')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cod.{extension}')
    await ctx.send(f'reload {extension} successful')
    print(f'-> Reloaded {extension} successful!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

for filename in os.listdir('Izumi_Sagiri/cod'):
    if filename.endswith('.py'):
        bot.load_extension(f'cod.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdate['token'])