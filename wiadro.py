import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NTMzNjM0NzA3NjYyMDQ1MTg0.Dxt_aw.jovVKTzRPaaqgWuXzutyOToTf2A"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!siema'):
        msg = 'Sieeeeeema {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)


@client.command(name='!wiadro',
                description="Tak/nie",
                brief="Odp z zewnatrz",
                aliases=['wiadereczko', 'wiad', 'wiadroo'],
                pass_context=True)
async def wiadro(context):
    possible_responses = [
        'Nabijaj wiadro',
        'Nabijaj 2 wiadra',
        'Jeboj 3!',
        'Resetuj biosa wal 4',
        '5, juz po tobie',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.event
async def on_message(message):
    if message.content.startswith('!wali'):
        await client.send_message(message.channel, 'Kto wali wiadro? !imie <tutaj>')

        def check(msg):
            return msg.content.startswith('!imie')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('!zakonnik'):].strip()
        await client.send_message(message.channel, '{} WALI WIADERECZKO!'.format(name))


@client.event
async def on_message(message):
    if message.content.startswith('!kto'):
        await client.send_message(message.channel, 'Kto poliże nutelle? !imie <tutaj>')

        def check(msg):
            return msg.content.startswith('!imie')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('!imie'):].strip()
        await client.send_message(message.channel, '{} CHYBA COS CI STOI :LUL: !'.format(name))

    if message.content == "hej":
        if message.author.id == ('224550108136472576'):
            await client.send_message(message.channel,'```roll 1 krytyczne niepowodzenie.``` Witając się połknąłeś pszczołę która Cię ugryzła. Trafiasz do szpitala tracisz 2 tury.')
        elif message.author.id == ('222143837605330945'):

            await client.send_message(message.channel,'Sebek, daj chlebek')
        elif message.author.id == ('222484443368128513'):

            await client.send_message(message.channel,'RYBIARZ DO WODY UCIEKAJ!')
        elif message.author.id == ('215167611636416514'):
            await client.send_message(message.channel,'Witaj mistrzu, dobrze Cię widzieć!')
        elif message.author.id == ('206100992180224002'):
            await client.send_message(message.channel,'ŻUBEEER ')
        elif message.author.id == ('232860146622005248'):
            await client.send_message(message.channel,'Na przyrke!!')
        elif message.author.id == ('318134058171367425'):
            await client.send_message(message.channel,'No cześć, jak odbyt po dzisiejszej nocy?')
        elif message.author.id == ('318134058171367425'):
            await client.send_message(message.channel,'No cześć, jak odbyt po dzisiejszej nocy?')
        else:
            await client.send_message(message.channel, 'No galosz')


    elif message.content == "kto poliże":
        await client.send_message(message.channel, 'temu stanie.')

    elif message.content == "XD":
        await client.send_message(message.channel, 'IKS KURWA DE.')


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="WALE WIADRO NA ZAMKU ZE ZŁOTA"))
    print("Logged in as " + client.user.name)


@client.command()
async def pizza(message):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    if message.content.startswith('!pizza'):
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            await client.say("Twoja pizza za bitcoin kosztuje: $" + response['bpi']['USD']['rate'])


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
