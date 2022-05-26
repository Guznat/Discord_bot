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
import os
import shutil
from discord.ext import commands
import requests

startup_extensions = ["Music", "exception", "roll", "major"]
BOT_PREFIX = ("?", "$")
TOKEN = "NTMzNjM0NzA3NjYyMDQ1MTg0.XDnoDA.0A4cUGYGveXpeZ7lxiQ4sb4Cq1s"  # Get at discordapp.com/developers/applications/me


bot = discord.Client()
server= bot.get_guild(287944176870359040)
client = commands.Bot(command_prefix=BOT_PREFIX)
status = ['LECYMY', 'DUUUR']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    while client.is_ready():
        current_status = next(msgs)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=current_status))
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print('Bot w gotowosci')
    kapitularz = client.get_channel(287944176870359040)
    #await kapitularz.send('Dobranoc :peepohug:')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='🌿Gość w zakonie')
    await server.add_roles(member, role)
    await server.send(f"```WITAMY W ZAKONIE {member}! Dostajesz rangę: {role}```")


#                                          COMMANDS DEFINITIONS
@client.command()
async def github(ctx):
    await ctx.send("www.github.com/Guznat")

@client.command()
async def google(ctx, *args):
    f_string = []
    for s in str(args):
        f_string.append(str(s))
    final = "".join(f_string).replace(" ", "+").replace(",", "").replace("'", "").replace(")","").replace("(", "")
    googe_url = f"https://www.google.com/search?q={final}"
    await ctx.send(str(googe_url))
    # replace is a best option according https://stackoverflow.com/questions/3411771/multiple-character-replace-with-python





@client.command()
async def roll20(ctx):
    # role = discord.utils.get(member.server.roles, name='🌿 Gracz RPG 🎲')
    embed = discord.Embed(
        title='Roll20!',
        description='Wbijać bohaterowie, przygoda czeka! ``` https://roll20.net/ ```',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text=f'@Gracz RPG (soon)')
    embed.set_image(url='https://app.roll20.net/v2/images/roll20-logo.png?v=2')
    embed.set_thumbnail(url='https://app.roll20.net/v2/images/roll20-logo.png?v=2')
    embed.set_author(name='N4T4N')

    await ctx.send(embed=embed)



@client.command()
async def pogoda(ctx, miasto):

    if miasto=="Warszawa":
        d=52.22
        s=21.01

    elif miasto=="Bielsko-Biała":
        d = 49.81
        s = 19.04

    elif miasto=="Katowice":
        d = 50.26
        s = 19.02

    elif miasto=="Wrocław":
        d = 51.10
        s = 17.02

    elif miasto=="Poznań":
        d = 52.39
        s = 16.95

    elif miasto=="Gdańsk":
        d = 54.34
        s = 18.66

    elif miasto=="Gdynia":
        d = 54.51
        s = 18.53

    elif miasto=="Białystok":
        d = 53.12
        s = 23.16
    elif miasto =="Opole":
        d=  50.66
        s= 17.92



    else:
        await ctx.send("Niema takiego miasta w spisie")


    async with aiohttp.ClientSession() as session:  # Async HTTP request
        url = f'http://api.weatherunlocked.com/api/current/{str(d)},{str(s)}?app_id=b2b042cf&app_key=0b5e4d36d7c17551b832bc12c53f3b43'
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        now = datetime.now()
        format = "%d/%m/%Y %H:%M:%S"
        print(response)
        await ctx.send(
            f"```W mieście {miasto} o czasie {str(now.strftime(format))} jest właśnie {str(response['temp_c'])}°C. Temperatura odczuwalna to  {str( response['feelslike_c'])}°C. Prędkość wiatru wynosi {str(response['windspd_kmh'])}km/h"
            f" Wilgotność wynosi {str(response['humid_pct'])}%, a na drogach można spodziewać się widoczności do {str(response['vis_km'])}km. Dziękuję za uwagę elo benc! z fartem mordeczko!  ```")



@client.command(pass_context=True)
async def clear(ctx, amount=1):
    author_id = ctx.author.id
    channel = ctx.channel
    if author_id == 215167611636416514:
        messages = []
        async for message in server.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await ctx.delete_messages(messages)
        await ctx.send('Wiadomości skasowane')

    else:
        permission_false = str('Wybacz' + ctx.message.author + " nie masz pozwolenia do korzystania z tej komendy")
        await server.send(permission_false)


@client.command()
async def write():
    string = str(input("Wpisz cos"))
    input_list = []
    output_list = []
    for i in string.split(" "):
        for split_i in i:
            if split_i.lower() == 'a':
                a= get(server.get_all_emojis(), name='regional_indicator_a')
                output_list.append(a)
            elif split_i.lower() == 'b':
                b = get(server.get_all_emojis(), name='regional_indicator_b')
                output_list.append(b)
                #TODO standard emoiji problem
    await client.send(output_list)

#                                               ON_MESSAGE EVENTS


@client.event
async def on_message(ctx):
    # SERVER MESSAGE LOG
    author_id = ctx.author.id
    author = ctx.author
    content = ctx.content
    channel = ctx.channel


    print(f'{channel} | {author}: {content} | {author_id} |')

    for attachment in ctx.attachments:
        zdjecie = attachment.url
        kroniki = client.get_channel(750844903403028490)
        if content:
            await kroniki.send(content)
        await kroniki.send(zdjecie)
        await kroniki.send(author)
    emoji = '<:peepecum:753348146658279435>'
    walenie_konia = [
"Polerować torpedę",
"Czochrać bobra",
"Marszczyć Freda",
"Wyświechtać bombala",
"Brąchać dżdżownicę"
"Glancować lizaczka"
"Szlifować stalagmita",
"Rypać choinę",
"ściskać truskawę",
"Głaskać Jasia",
"Strobilizować polipa",
"ślupać wojownika",
"ślizgać bambusa",
"Szturchać pieczarę",
"Podawać hot-doga",
"Łuskać grocha",
"Gmerać morelę",
"Straszyć Gargamela",
"Stukać gumiaka",
"Dynamizować ślimaka",
"Cofać Bułgara",
"Rozgrzewać sopla",
"Trzepać dywanik",
"Obierać wafla",
"Klepać kołderkę",
"Bawić się Fantomasem",
"Ubijać śmietanę",
"Kręcić dżointa",
"Grzmocić armatę",
"Flirtować z Wackiem",
"Przeczyszczać rurę",
"Obierać banana",
"Kwasić ogóra",
"Lukrować pączka",
"Detonować bombę",
"ślipać Flipa",
"ślupać Flapa",
"Rolować batona",
"Ocieplać Nerona",
"Robić naleśnika",
"Ważyć sosa",
"Wietrzyć trąbę",
"Grać fleta",
"Stukać tukana",
"ściągać kaptura",
"Poić wielbłąda",
"Gwizdać milicjanta",
"Moczyć szynszyla",
"Miętosić pompę",
"Siorbać czajnik",
"Ciosać kołek",
"Szlifować migdała",
"Cmokać dziobaka",
"Trząchać palmę",
"Łachotać Conana",
"Rozciągać parowe",
"Gilgotać gila",
"Dziubdziać Smerfa",
"Siorbać kucyka",
"Trenować ogiera",
"Formować pasztet",
"Rechotać Bazyla",
"Wielce improwizować",
"Walić pioruna",
"Froterować szczotę",
"Czyścić brudasa",
"Kleić łapę",
"Wałkować rogala",
"Poskromić złośnika",
"Demaskować świntucha",
"Ćwiczyć szabelkę",
"Walić Walezego",
"Poruszać ogonkiem",
"Ostrzyć ołówek",
"Robić kreta",
"Więzić ptaka",
"Drażnić frędzelka",
"Sprawdzać hydraulikę",
"Majstrować przy kablu",
"Dokręcać śrubę",
"Dziczyć kaczora",
"Wydoić byka",
"Gnieść korniszona",
"Kręcić śrubokręta",
"Zmiękczać twardziela",
"Ścinać pieniek",
"Dziergać Batmana",
"Skrobać Bena",
"Wyrywać rzepę",
"Wybrudzić świerszczyka",
"Zaciągać ręczny",
"Zgniatać Plastusia",
"Sterować pilotem",
"Zrypać kasztana",
"Poruszać imadłem",
"Zlustrować motyla",
"Obrzezać Cygana",
"Obciągnąć zmarszczucha",
"Uwolnić jaszczura",
"tarmosić Showa po rudej brodzie",
"Robótki ręczne",
"namaszczać Izahiasza",
"walić niemca w chełm",
"sztyrchać pingwina",
"heblować wióra"]

    # REACTION

    if "Naura" in ctx.content:
        await channel.send("NAURA!")
    elif "naura" in ctx.content:
        await channel.send("NAURA!")


    if author_id == 215167611636416514:
        emoji = '<:peepecum:753348146658279435>'
        #await ctx.add_reaction(emoji)
        #await asyncio.sleep(2)



        if "siema" in ctx.content:
            await channel.send("Witaj mistrzu!")


    elif author_id != 215167611636416514:
        if "siema" in ctx.content:
            await channel.send("Witaj zakonniku!")

    if "walić konia" in ctx.content:
        await  channel.send(random.choice(walenie_konia)+emoji)


        # await client.send_message(message.channel, 'Witaj mistrzu, dobrze Cię widzieć!')

    # LAST CODE LINE FOR COMMANDS WORKING
    await client.process_commands(ctx)


# @client.event
# async def on_message_delete(message):
#     author = message.author
#     channel = message.channel
#     await client.send_message(channel, f'Wiadomość od {author} została skasowana na kanale {channel}')








client.loop.create_task(change_status())
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = f"{type(e).__name__}: {e}"
            print(f"Failed to load extension {extension}, {exc} ")
    client.run(TOKEN)
