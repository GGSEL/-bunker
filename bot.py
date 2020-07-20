import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import config

client = commands.Bot(command_prefix='!')

# channels.id = {
#     'news': iD,
# }

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@client.command(pass_context=True)
async def showrole(ctx):
    
    await ctx.send(config.persone.showrole())


client.run('NzM0Nzk2ODk3MTU5NzQxNTQw.XxXLVA.DkIcRM7W5LGfLZrp6dTBrhDUoE4')