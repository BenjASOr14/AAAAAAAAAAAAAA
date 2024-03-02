import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def mem(ctx):
    with open('M2L1/img/h.jpg ', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)   

bot.run("MTIwMzM4MjIyMzA0MzA0MzQxOA.GkH-Z8.orp_sfP0XWeM04gmF2T5Hu2DSWw-t1ouv7ydl8")