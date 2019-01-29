from datetime import datetime
import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext import commands
from itertools import cycle
import asyncio
from discord.utils import get
from discord.voice_client import VoiceClient
import youtube_dl

# startup_extensions = ["Music"]
BOT_PREFIX = ("?", "$")
TOKEN = "NTMzNjM0NzA3NjYyMDQ1MTg0.Dyzp6w.5d6rIT6DXvxtQZQqqNpvu6zBhFI"  # Get at discordapp.com/developers/applications/me

client = commands.Bot(command_prefix=BOT_PREFIX)
players = {}
status = ['AMENUS','BUCH']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=Game(name=current_status))
        await asyncio.sleep(5)



@client.event
async def on_ready():
    print('Bot w gotowosci')



# class Main_Commands():
#     def __init__(self, client):
#         self.client = client


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='🌿Gość w zakonie')
    await client.add_roles(member, role)
    await client.say(f"```WITAMY W ZAKONIE {member}! Dostajesz rangę: {role}```")





#                                          COMMANDS DEFINITIONS


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)



@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice = client.voice_client_in(server)
    player = await voice.create_ytdl_player(url, ytdl_options={'default_search': 'auto', 'quality': 'highestaudio', 'liveBuffer':'50000'})
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()


@client.command()
async def roll20():
    #role = discord.utils.get(member.server.roles, name='🌿 Gracz RPG 🎲')
    embed = discord.Embed(
        title= 'Roll20!',
        description= 'Wbijać bohaterowie, przygoda czeka! ``` https://roll20.net/ ```',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text=f'@Gracz RPG (soon)')
    embed.set_image(url='https://app.roll20.net/v2/images/roll20-logo.png?v=2')
    embed.set_thumbnail(url='https://app.roll20.net/v2/images/roll20-logo.png?v=2')
    embed.set_author(name='N4T4N')

    await client.say(embed=embed)


@client.command()
async def godzina():
    date = datetime
    await client.say(f"Jest {date.hour}:{date.minute} | {date.day}")


@client.command()
async def pogoda(d=49.82,s=19.04):
    url = f'http://api.weatherunlocked.com/api/current/{str(d)},{str(s)}?app_id=b2b042cf&app_key=0b5e4d36d7c17551b832bc12c53f3b43'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        print(response)
        await client.say("W podanej lokalizacji jest teraz: " + str(response['temp_c']) + "°C. Temperatura odczuwalna to: " + str(
            response['feelslike_c']) + "°C. <:shieet:287968329342386177>")


@client.command(pass_context=True)
async def clearsecret(ctx, amount=3):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Wiadomości skasowane')




#                                               ON_MESSAGE EVENTS





@client.event
async def on_message(message):
    # SERVER MESSAGE LOG
    author = message.author
    content = message.content
    channel = message.channel
    print(f'{channel} | {author}: {content}')

    # REACTION

    if message.author.id == ('215167611636416514'):
        PIW = get(client.get_all_emojis(), name='PIW')
        SKO = get(client.get_all_emojis(), name='SKO')
        await client.add_reaction(message, PIW)
        await client.add_reaction(message, SKO)
        #await client.send_message(message.channel, 'Witaj mistrzu, dobrze Cię widzieć!')


    # LAST CODE LINE FOR COMMANDS WORKING
    await client.process_commands(message)


@client.event
async def on_message_delete(message):
    author = message.author
    channel = message.channel
    await client.send_message(channel, f'Wiadomość od {author} została skasowana na kanale {channel}')



# if __name__ == "__main__":
#     for extension in startup_extensions:
#         try:
#             client.load_extension(extension)
#         except Exception as e:
#             exc = f"{type(e).__name__}: {e}"
#             print(f"Failed to load extension {extension}, {exc} ")


client.loop.create_task(change_status())
client.run(TOKEN)
