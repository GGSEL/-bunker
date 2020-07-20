import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = commands.Bot(command_prefix='!')

channels.id = {
    'news': iD,
}


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


client.run('NzM0Nzk2ODk3MTU5NzQxNTQw.XxW7xw.-ON-UTwmu10T2ULf-UmK1nwT0Ko')