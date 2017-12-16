import discord
import asyncio
import random
import json
import os
import datetime
from discord.ext import commands
import time
import traceback


tickets = discord.Object("376563001643499522")
suggest = discord.Object('376776759221288961')
bot_invite="https://discordapp.com/oauth2/authorize?client_id=375370278810681344&scope=bot&permissions=2146958583"
support="https://discord.gg/HcMhj3q"
prefix='s.'
bot=commands.Bot(command_prefix=prefix)
bot.remove_command('help')

class Utils():
    print('Utils Loaded')
    print('------')
    global utils
    utils = 1
    

    @commands.command(pass_context = True)
    async def serverinfo(ctx):
        server = ctx.message.server
        i = 0
        humanusers = 0
        botusers = 0
        online = 0
        voicechanneles = 0
        textchannels = 0 
        totalusers = 0
        totalchannels = 0
        for members in server.members:
          totalusers += 1
          if members.bot is True:
            botusers += 1
          else:
            humanusers += 1
          if members.status.online is True:
            online += 1
        for channels in server.channels:
          totalchannels += 1
 #         if channels.type == "text":
  #          textchannels += 1
   #       else:
    #        voicechanneles += 1
     #   print(textchannels)
        
        ago = (ctx.message.timestamp - server.created_at).days
        embed = discord.Embed(title= "Server", description="-", color=0x00ff00)
        embed.set_thumbnail(url=server.icon)
        embed.add_field(name="Server Name", value=server.name, inline=False)
        embed.add_field(name="Server Owner", value=server.owner, inline=False)
#        embed.add_field(name="Server ID", value=server.id, inline=True)
#        embed.add_field(name="Server Owner ID", value=server.owner.id, inline=True)
#        embed.add_field(name="Member Count", value="- {0} members \n - {1} bots \n - {2} total".format(humanusers, botusers, totalusers), inline=False)
#        embed.add_field(name="Channels", value="Total Channels : {}".format(totalchannels), inline=True)
#        embed.add_field(name="Verification Level", value=server.verification_level, inline=False)
#        embed.add_field(name="Server Region", value=server.region, inline=True)
#        embed.add_field(name="Server created at", value="{0}, about {1} days ago".format(server.created_at, ago), inline=False)
        await ctx.bot.say(embed=embed)

    @commands.command(pass_context = True)
    async def test(ctx):
        await ctx.bot.say("I am working!")

    @commands.command(pass_context = True)
    async def ticket(ctx, *, ticket: str):
        embed = discord.Embed(title="__New Ticket!__", description="I have recieved a new ticket !", color=0x00ff00)
        embed.add_field(name="Sent by", value=ctx.message.author, inline=True)
        embed.add_field(name="Ticket", value=ticket, inline=True)
        await ctx.bot.delete_message(ctx.message)
        await ctx.bot.send_message(tickets, embed=embed)
        await ctx.bot.say("Your ticket has been sent to my dev team!")

    @commands.command(pass_context = True)
    async def ping(ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await ctx.bot.send_typing(channel)
        t2 = time.perf_counter()
        await ctx.bot.say("Pong! `{}ms`".format(round((t2-t1)*1000)))

    @commands.command(pass_context = True)
    async def about(ctx):
        await ctx.bot.say("This command is undergoing a rewrite, please try again later!")

    @commands.command(pass_context = True)
    async def invite(ctx):
      try:
        embed = discord.Embed(title=":link: __Bot Links__", description='[{}]({})''\n[{}]({})'.format("Bot invite", bot_invite, "Support Server", support), color=0x00ff00)
        await ctx.bot.send_message(ctx.message.author, embed=embed)
        await ctx.bot.send_message(ctx.message.channel, "Check your DM's :envelope_with_arrow:")
      except:
        todo = discord.Embed(title=":warning: Error!",description="An error occured, you may have DM's disabled",color=0xff0000)
        await ctx.bot.say(embed = todo)

    @commands.command(pass_context = True)
    async def help(ctx):
      try:
        
        await ctx.bot.send_message(ctx.message.channel, "Some commands may not be available at the time, sorry for the inconvinience")
        embed = discord.Embed(title="__Bot commands!__", description="", color=0x00ff00)
        embed.add_field(name=":warning: **Remember**", value="More commands will be added in the future", inline=False)
        embed.add_field(name="**For info on a certain command**", value="s.help <command>", inline=False)
        embed.add_field(name="s.help", value="Show this message", inline=False)
        embed.add_field(name="s.invite", value="DM's all the useful links about the bot", inline=False)          
        util = discord.Embed(title="__Utility commands!__", description="", color=0x00ff00)
        util.add_field(name="s.servers", value="Show the number of servers and members the bot is serving", inline=False)
        util.add_field(name="s.serverinfo", value="Shoes information on the server", inline=False)
        util.add_field(name="s.ticket", value="Sends a ticket to the dev team", inline=False)
        util.add_field(name="s.suggest", value="Sends a suggestion to the dev team", inline=False)
        util.add_field(name="s.getid [user]", value="Get's a user's id (if left empty author's id will be brought up)", inline=False)
        util.add_field(name="~~s.about~~", value="Shows info on the bot", inline=False)
        util.add_field(name="s.stats", value="Shows the bot's stats", inline=False)
        util.add_field(name="s.ping", value="Shows the bot's latency", inline=False)
        util.add_field(name="~~s.changelog [todo/doing/done]~~", value="Shows the bot's functions in developpement (if left empty all info will be shown)", inline=False)
        fun = discord.Embed(title="__Fun commands!__", description="", color=0x00ff00)
        fun.add_field(name="s.flip", value="Flips a coin", inline=False)
        fun.add_field(name="s.roll", value="Rolls a dice", inline=False)
        fun.add_field(name="s.8ball [question]", value="See's what the 8ball has to answer", inline=False)
        fun.add_field(name="s.rps [rock/paper/scissors]", value="Plays a game of rock, paper, scissors", inline=False)
        cool = discord.Embed(title="__Random commands!__", description="", color=0x00ff00)
        cool.add_field(name="s.dog", value="Gets a dog picture", inline=False)
        cool.add_field(name="s.say [message]", value="Repeats your message", inline=False)
        cool.add_field(name="s.cat", value="Gets a cat picture", inline=False)
        mod = discord.Embed(title="__Moderator commands!__", description="", color=0x00ff00)
        mod.add_field(name="s.ban", value="Bans a certain user", inline=False)
        mod.add_field(name="s.kick", value="Kicks a certain user", inline=False)
        mod.add_field(name="s.clear [x]", value="Clears 'x' messages (Maximum of 100 at a time)", inline=False)
        mod.add_field(name="s.prune [x]", value="Kicks users who have been inactive since 'x' days (Maximum of 30)", inline=False)
        await ctx.bot.say("Check your DM's :envelope_with_arrow:")
        await ctx.bot.send_message(ctx.message.author, embed=embed)
        await ctx.bot.send_message(ctx.message.author, embed=util)
        await ctx.bot.send_message(ctx.message.author, embed=fun)
        await ctx.bot.send_message(ctx.message.author, embed=cool)
        await ctx.bot.send_message(ctx.message.author, embed=mod)
      except:
        todo = discord.Embed(title=":warning: Error!",description="An error occured, you may have DM's disabled",color=0xff0000)
        await ctx.bot.say(embed=todo)
        
      

    @commands.command(pass_context = True)
    async def suggest(ctx, *, suggests: str):
        embed = discord.Embed(title="__New suggestion!__", description="I have recieved a new suggestion !", color=0x00ff00)
        embed.add_field(name="Sent by", value=ctx.message.author, inline=True)
        embed.add_field(name="Suggestion", value=suggests, inline=True)
        await ctx.bot.delete_message(ctx.message)
        await ctx.bot.send_message(suggest, embed=embed)
        await ctx.bot.say("Your suggestion has been sent to my dev team!")

    @commands.command(pass_context = True)
    async def servers(ctx):
      
      serverCount = 0
      members = 0
      for server in ctx.bot.servers:
        serverCount += 1
        for member in server.members:
            members += 1
        
      embed = discord.Embed(title="Serving", description='{0} servers for {1} users'.format(serverCount, members), color=0x00ff00)
      await ctx.bot.say(embed=embed)
        
    @commands.command(pass_context = True)
    async def stats(ctx):
        totalusers = 0
        totalchannels = 0
        onlineusers = 0
        humans = 0
        bots = 0
        serverCount = 0
        members = 0
        channels = []
        for server in ctx.bot.servers:
            members += len(server.members)
            channels += [len(server.channels)]
            serverCount += 1
            for member in server.members:
                totalusers += 1
                if member.bot is True:
                  bots += 1
                else:
                  humans += 1
            for channel in server.channels:
                totalchannels += 1
        embed = discord.Embed(title="Here are my stats!", color = 0x000000)
        embed.set_thumbnail(url=ctx.message.server.me.avatar_url)
        embed.add_field(name="Total Servers", value=serverCount)
        embed.add_field(name="Users", value='Total users: {0}\n Human users: {1}\n Bot users: {2}'.format(members, humans, bots))
        embed.add_field(name="Channels", value="Total channels: {}".format(totalchannels))
        await ctx.bot.say(embed=embed)
        
    @commands.command(pass_context = True)
    async def getid(ctx, *, member: discord.Member = None):
      if member is None:
        embed = discord.Embed(title="Your id is:", description=ctx.message.author.id, color=0x000000)
      else:
        embed = discord.Embed(title="{}'s id is:".format(member), description=member.id, color=0x000000)
      await ctx.bot.say(embed=embed)
      
   # @commands.command(pass_context = True)
  #  async def userinfo(ctx, *, member: discord.Member = None):
 #     if member is None:
        
        
        
      
        
def setup(bot):
    bot.add_cog(Utils)
