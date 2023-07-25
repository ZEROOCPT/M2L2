import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

sampah_organik = ["daun","buah",'makanan']
sampah_anorganik = ['plastik','stereofoam','cabel']

@bot.command()
async def pilih(ctx):
    while True:
        await ctx.send("masukan sampah")
        msg = await bot.wait_for("message")

        if msg.content in sampah_organik :
            await ctx.send("masukkan dalam organik")
        elif msg.content in sampah_anorganik :
            await ctx.send("masukkan dalam anorganik") 
        else :
            await ctx.send("entri tidak ada maka program berhenti") 
            break
bot.run("Token")

