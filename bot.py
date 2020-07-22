import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import reaction, user
import asyncio
import character


bot = commands.Bot(command_prefix='!')

# channels.id = {
#     'news': iD,
# }

game = False

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.content.startswith('**Игра начинается!**') and message.author.id == 734796897159741540:
        await message.add_reaction('cometa_746623:735442759057539092')


@bot.command(pass_context=True)
async def play(message):
    await message.channel.purge(limit=1)

    global game
    await message.channel.send('**Игра начинается!**')
    game = True

@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.id == '735442759057539092':
        print('success')
        member = payload.member
        embed = discord.Embed(title='Тебе выдана роль!',
                          colour=discord.Color.green())
        embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        embed.set_footer(text=character.create_Character(1))

        await member.send(embed=embed)


# @bot.command(pass_context=True)
# async def showrole(ctx, *, quontity):
#     await ctx.channel.purge(limit=1)
#     embed = discord.Embed(title='Тебе выдана роль!',
#                           colour=discord.Color.green())
#     embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
#     quontity = int(quontity)

#     for i in range(quontity):
#         c = character.create_Character(quontity)
#         embed.set_footer(text=c)
#         await ctx.send(embed=embed)


bot.run('NzM0Nzk2ODk3MTU5NzQxNTQw.XxXLVA.DkIcRM7W5LGfLZrp6dTBrhDUoE4')
