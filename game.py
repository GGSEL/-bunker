import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import reaction, user
import time
import asyncio


bot = commands.Bot(command_prefix='!')


class StartGame:
    @bot.event
    async def startgame(ctx):
        embed = discord.Embed(title='Поспеши!',
                                    colour=discord.Color.green())
        embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        embed.set_footer(text='Осталось 29 секунд до начала игры...')

        await ctx.send(embed=embed)

        time.sleep(30)

        embed = discord.Embed(title='Игра начинается!',
                            colour=discord.Color.green())
        embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        embed.set_footer(text='Не успел? Ничего! В следующий раз точно успеешь')


        await ctx.send(embed=embed)
