import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import reaction, user
import time
import asyncio
import character
import game
import catastrophes
from catastrophes import *


bot = commands.Bot(command_prefix='!')

game = False


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@bot.event
async def on_ready(ctx):
    embed = discord.Embed(title='Спасибо, что пригласил меня!',
                                    colour=discord.Color.green())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text='Чтоб начать игру, напиши !play и жди роль!')

    await ctx.send(embed=embed)


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)

    if ctx.content.startswith('**Игра начинается!**') and ctx.author.id == 734796897159741540:
        await ctx.add_reaction('cometa_746623:735442759057539092')

        


@bot.command(pass_context=True)
async def play(message):
    await message.channel.purge(limit=1)

    global game
    await message.channel.send('**Игра начинается!**')
    game = True

    c = catastrophes.text()

    time.sleep(1)

    embed = discord.Embed(title='Поспеши!',
                                    colour=discord.Color.green())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text='Осталось 59 секунд до начала игры...')

    await message.send(embed=embed)


    time.sleep(30)

    embed = discord.Embed(title='Поспеши!',
                                    colour=discord.Color.green())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text='Осталось 29 секунд до начала игры...')

    await message.send(embed=embed)

    time.sleep(30)

    embed = discord.Embed(title='Игра начинается!',
                        colour=discord.Color.green())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text='Не успел? Ничего! В следующий раз точно успеешь')


    await message.send(embed=embed)

    time.sleep(3)


    await message.channel.purge(limit=4)
    time.sleep(2)


    embed = discord.Embed(title=c.get('title'),
                        colour=discord.Color.green())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=c.get('description'))
    await message.send(embed=embed)

    game = False



@bot.event
async def on_raw_reaction_add(payload):
    global game

    if payload.emoji.name == 'cometa_746623' and game == True:
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


token = os.environ.get('BOT_TOKEN')
client.run(str(token))
