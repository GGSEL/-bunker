import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import character

client = commands.Bot(command_prefix='!')

# channels.id = {
#     'news': iD,
# }


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@client.command(pass_context=True)
async def showrole(ctx, *, quontity):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title = 'Тебе выдана роль!',
                          colour = discord.Color.green())
    embed.set_author(name = client.user.name, icon_url = client.user.avatar_url)
    quontity = int(quontity)

    for i in range(quontity):
        c = character.create_Character(quontity)
        embed.set_footer(text = c)
        await ctx.send(embed = embed)


client.run('NzM0Nzk2ODk3MTU5NzQxNTQw.XxXLVA.DkIcRM7W5LGfLZrp6dTBrhDUoE4')