import discord
import os

from discord.flags import Intents

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep} 1- Não desrespeitar ninguem {os.linesep} 2-Seja Ativo {os.linesep} 3- Presta atenção ao fazer suas jogadas {os.linesep} 4- Ao tenta chamar o mestre da partida usar o ?off')
        elif message.content == '?nivel':
            await message.author.send('Nivel 1')  

    async def on_member_join(self,member):
        guild = member.guid
        if guild.system_chanel is not None:
            mensagem = f'{member.mention} acaboou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)


intents = discord.Intents.default()
Intents.members = True

client = MyClient(intents=intents)
client.run('OTIxODUzNDY1MjgwNTEyMDky.Yb488Q.2aGFqUNb2ErLmfoeXZpIe-_e8Vs')