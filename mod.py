import discord
import asyncio
import random
import json
import os
import datetime
from discord.ext import commands
import time
import traceback

prefix='s.'
bot=commands.Bot(command_prefix=prefix)
perm_error = discord.Embed(title=":warning: Error!",description="You do not have the permission to use this command",color=0xff0000)
perm_errorbis = discord.Embed(title=":warning: Error!",description="I do not have the permission to use this command",color=0xff0000)

class Mod():
    print('Mod loaded')
    print('------')

    @bot.command(pass_context = True)
    async def mod(ctx):
        await ctx.bot.say("I am working!")

    @bot.command(pass_context = True)
    async def ban(ctx, *, member: discord.Member = None):
        if member is None:
            await ctx.bot.say("Who do I ban ?")
    
        elif ctx.message.server.me.server_permissions.ban_members == True:
                if ctx.message.author.server_permissions.ban_members == True:
                    if ctx.message.author.top_role.position > member.top_role.position:
                        await ctx.bot.ban(member)
                        await ctx.bot.say(":white_check_mark: Succesfully banned {}".format(member))
                    else:
                        await ctx.bot.say(embed=perm_error)
                else:
                    await ctx.bot.say(embed=perm_error)
        else:
            await ctx.bot.say(embed=perm_errorbis)
            
    @bot.command(pass_context = True)
    async def kick(ctx, *, member: discord.Member = None):
        if member is None:
            await ctx.bot.say("Who do I kick ?")
    
        if ctx.message.server.me.server_permissions.kick_members == True:
                if ctx.message.author.server_permissions.kick_members == True:
                    if ctx.message.author.top_role.position > member.top_role.position:
                        await ctx.bot.kick(member)
                        await ctx.bot.say(":white_check_mark: Succesfully kicked {}".format(member))
                    else:
                        await ctx.bot.say(embed=perm_error)
                else:
                    await ctx.bot.say(embed=perm_error)
        else:
            await ctx.bot.say(embed=perm_errorbis)
    
    @bot.command(pass_context = True)
    async def clear(ctx, number):
      try:
        val = int(number)
      except ValueError:
        await ctx.bot.say("Please use a valid number `1-100`")
      await ctx.bot.say("Please specify a number of messages to delete!")
      await ctx.bot.purge_from(ctx.message.channel, limit=number)
      

def setup(bot):
    bot.add_cog(Mod)
