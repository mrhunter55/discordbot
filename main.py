import discord,os
import asyncio
from discord.ext import commands 

bot = commands.Bot(command_prefix='ay ') 

@bot.event
async def on_ready():
    game = discord.Activity(name="Under Development", type=discord.ActivityType.playing)
    await bot.change_presence(status=discord.Status.dnd, activity=game)
   
@bot.command() 
async def say(ctx,*,args):
    embed = discord.Embed(title=str(ctx.author), description=args, color=0x0000ff)
    await ctx.send(embed=embed)
    await ctx.message.delete()
@bot.command() 
async def hi(ctx):
    user = ctx.author.mention
    await ctx.send("Hello "+str(user)) 

@bot.command() 
async def dothis(ctx):
    await ctx.send("Done :sunglasses:")
@bot.group() 
async def ign(ctx):
    
    embed = discord.Embed(title="No IGN", description="No IGN  Added!", color=0xff0000)
    await ctx.send(embed=embed)
    
@ign.command()
async def add(ctx,*,inp):
    
    await ctx.send("Your IGN : "+str(inp))
    
@bot.command() 
async def profile(ctx):
    embed = discord.Embed(title=str(ctx.author.mention), description='', color=0x0000ff)
    
    await ctx.send(embed=embed)
    
    
bot.run(os.getenv('token'))