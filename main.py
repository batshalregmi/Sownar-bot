import discord
import asyncio
import json
import os
import datetime
from discord.ext import commands
import time
import traceback


logs = discord.Object("376778387676594176")
console = discord.Object("376552211817299968")
tickets = discord.Object("376563001643499522")
seconds=0
minutes=0
hours=0
days=0
weeks=0
prefix='s.'
ownerids=['221381001476046849', '221263215496134656']

bot=commands.Bot(command_prefix=prefix)
perm_error = discord.Embed(title=":warning: Error!",description="You do not have the permission to use this command",color=0xff0000)

class Main():
    print('main Loaded')
    print('------')

    @bot.event
    async def on_server_join(server):
      embed = discord.Embed(title="__Server Joined!__", description="I have joined a new server !", color=0x00ff00)
      embed.add_field(name="Server Name", value=server.name, inline=True)
      embed.add_field(name="Server Owner", value=server.owner, inline=True)
      embed.add_field(name="Member Count", value="{0} members".format(server.member_count), inline=True)
      embed.add_field(name="Server Region", value=server.region, inline=True)
      await bot.send_message(console, embed=embed)
      await bot.send_message(logs, embed=embed)
    
    @bot.event
    async def on_server_remove(server):
      embed = discord.Embed(title="__Server Left!__", description="I have left a server !", color=0xff0000)
      embed.add_field(name="Server Name", value=server.name, inline=True)
      embed.add_field(name="Server Owner", value=server.owner, inline=True)
      embed.add_field(name="Member Count", value="{0} members".format(server.member_count), inline=True)
      embed.add_field(name="Server Region", value=server.region, inline=True)
      await bot.send_message(console, embed=embed)
      await bot.send_message(logs, embed=embed)
    

# -- Random.py --
#@bot.command(pass_context = True)
#async def say(ctx, *, echo: str):
#    await bot.say(echo)


    @bot.command(pass_context = True)
    async def todoadd(ctx, *, todo: str):
      if ctx.message.author.id not in ownerids:
          await bot.say(embed=perm_error)
      else:
          if not os.path.isfile("todo_file.pk1"):
              todo_list = []
          else:
              with open("todo_file.pk1", "r") as todo_file:
                  todo_list = json.load(todo_file)
          todo_list.append(todo)
          with open("todo_file.pk1", "w") as todo_file:
              json.dump(todo_list, todo_file)
          await bot.say("Added to todo list")

    @bot.command(pass_context = True)
    async def todo(ctx):
      if ctx.message.author.id not in ownerids:
          await bot.say(embed=perm_error)
      else:
          with open("todo_file.pk1", "r") as todo_file:
              todo_list = json.load(todo_file)
          for item in todo_list:
              await bot.say('`item`')

    @bot.command(pass_context = True)
    async def tododel(ctx, *, item: str):
      if ctx.message.author.id not in ownerids:
          await bot.say(embed=perm_error)
      else:
        try:
          with open('todo_file.pk1', 'r') as todo_list:
            todo = json.load(todo_list)
      
          for element in todo:
              if item in element:
                  del element[item]
      
          with open('todo_file.pk1', 'w') as todo_list:
              todo = json.dump(todo, todo_list)
      except IndexError:
          await bot.say("Please use a valid todo item")
        
def setup(bot):
    bot.add_cog(main)


