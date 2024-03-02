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
async def carton(ctx):
    with open('M2L1/img/h.jpg ', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)  
    await ctx.send("En general, el cartón es biodegradable y se descompondrá con el tiempo en condiciones adecuadas. Sin embargo, la velocidad exacta de descomposición puede variar significativamente según los factores mencionados anteriormente. En un vertedero, donde las condiciones pueden ser menos favorables para la descomposición aeróbica, el cartón puede tardar más tiempo en descomponerse completamente, a menudo años o décadas. En un entorno de compostaje o en la naturaleza, donde se proporcionan condiciones más adecuadas para la descomposición, el proceso puede ser considerablemente más rápido.")

@bot.command()
async def vidrio(ctx):
    with open('M2L1/img/d.jpg ', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)  
    await ctx.send("El vidrio es un material inorgánico que no se descompone de la misma manera que los materiales orgánicos. En condiciones naturales, el vidrio puede tardar muchos años e incluso siglos en descomponerse. De hecho, en la mayoría de los casos, el vidrio no se descompone por completo, sino que se fragmenta en pedazos más pequeños a lo largo del tiempo.")
@bot.command()
async def plastico(ctx):
    with open('M2L1/img/a.jpg ', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)  
    await ctx.send("El plástico es conocido por su durabilidad y resistencia a la descomposición natural. Dependiendo del tipo de plástico y las condiciones ambientales, puede tardar cientos o incluso miles de años en descomponerse por completo. Aquí hay algunas estimaciones aproximadas de descomposición para diferentes tipos de plásticos bajo ciertas condiciones")
@bot.command()
async def metales (ctx):
    with open('M2L1/img/f.jpg ', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)  
    await ctx.send("El tiempo que tarda el metal en corroerse o deteriorarse depende del tipo de metal, las condiciones ambientales y otros factores. Algunos metales, como el acero inoxidable, pueden resistir la corrosión durante períodos muy largos, mientras que otros metales, como el hierro o el aluminio, pueden corroerse más rápidamente en ciertas condiciones.")



@bot.command()
async def l(ctx):
    elementos_reciclables = """
**Papel y cartón:**
- Papel de oficina
- Revistas y periódicos
- Cajas de cartón
- Envases de cartón para alimentos (como las cajas de cereales)

**Vidrio:**
- Botellas de vidrio (de bebidas, salsas, etc.)
- Frascos de vidrio (de alimentos, medicinas, etc.)

**Plástico:**
- Botellas de plástico (de agua, refrescos, detergentes, etc.)
- Envases de plástico (de alimentos, productos de limpieza, etc.)
- Bolsas y películas de plástico (como bolsas de supermercado)
- Envases de yogur y otros productos lácteos

**Metales:**
- Latas de aluminio (de bebidas)
- Latas de conserva (de alimentos como las de atún, tomate, etc.)
- Envases de metal (como los de aerosol)
- Tapas y tapones metálicos

**Tetra Pak:**
- Envases de cartón para líquidos como leche, jugos, y otros productos alimenticios.

**Textiles:**
- Ropa usada
- Sábanas, toallas y otros textiles de hogar

**Electrodomésticos y aparatos electrónicos:**
- Electrodomésticos viejos (lavadoras, refrigeradores, etc.)
- Teléfonos móviles, ordenadores, y otros dispositivos electrónicos
"""
    await ctx.send(f'Lista de elementos reciclables: {elementos_reciclables}')





bot.run("MTIwMzM4MjIyMzA0MzA0MzQxOA.GkH-Z8.orp_sfP0XWeM04gmF2T5Hu2DSWw-t1ouv7ydl8")

































