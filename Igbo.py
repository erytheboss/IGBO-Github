import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def help(ctx):
    await ctx.send('no u')

bot.run('YOUR BOT TOKEN')