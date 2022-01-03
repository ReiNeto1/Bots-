from logging import exception
import discord
from discord.errors import Forbidden
from discord.ext.commands import errors
import requests
import datetime
from discord.ext import commands,tasks

bot = commands.Bot("!")
 
@bot.event
async def on_ready():
    print(f"Estou Pronto! Estou conectado como{bot.user}")
   # current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários!")
        
        await message.delete()
    await bot.process_commands(message)

@bot.event 
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    if reaction.emoji =="👍":
        role = user.guild.get_role(922937322859802634)
        await user.add_roles(role)
    elif reaction.emoji == "👀":
        role = user.guild.get_role(922937576023814164)
        await user.add_roles(role)

#@bot.command(name="oi")
#async def send_hello(ctx):
 #   name = ctx.author.name
  #  response = "olá, " + name
   # await ctx.send (response)
    #except discord.errors.Forbidden
   # await ctx.send("não posso te contar o seredo, habilite receber mensagens de qualquer pessoa do servidor")


@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):
    expression = " ".join(expression)
    print(expression)
    response = eval(expression)
    await ctx.send("A resposta é: " + str(response))

#@bot.command()
#async def binance(ctx,coin,base):
 #   response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
  #  data = response.json() # {"symbol" : "BNBBtC" , "price" : "0.00837200"}
   # price = data.get("price") #0.00837200
    #await ctx.send(f"O valor do par {coin}/{base} é {price}")
    #if price:
    #    await ctx.send(f"O valor do par {coin}/{base} é {price}")
    #else:
     #   await ctx.send(f"o par  {coin}/{base} é inválido")
    #excepti Exception as error:
        
    #await ctx.send("Ops..deu um erro")
    
    #print(errors)

bot.command(name="segredo")
async def secret(ctx):
    await ctx.author.send("1")
    await ctx.author.sed("2")    


#@tasks.loop(seconds=10) 
#async def current_time():
 #   now = datetime.datetime.now()
  #  now = now.strftime("%d/%m/%Y às %H:%M:%S")
   # channel = bot.get_channel(921855011045113967)
    #await channel.send("Data atual:" + now)


bot.run("OTIyNTQ4MjgzMzUwNTg1NDQ0.YcDECg.S7P1fehrBXoO4AvvqQFdp0jf-8A")