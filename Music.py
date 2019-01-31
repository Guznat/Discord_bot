from discord.ext import commands
import discord
players = {}

class Music:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)
        await self.client.say(f"Dołączono do {channel}")

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await voice_client.disconnect()
        await self.client.say(f"Odchodzę z {voice_client.channel}")

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice = self.client.voice_client_in(server)
        player = await voice.create_ytdl_player(url, ytdl_options={'default_search': 'auto', 'quality': 'highestaudio',
                                                                   'liveBuffer': '50000'})
        players[server.id] = player
        await self.client.say(f"Puszczam: {player.title}")
        player.start()

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        id = ctx.message.server.id
        await self.client.say("Zatrzymuje")
        players[id].pause()

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        id = ctx.message.server.id
        await self.client.say("Wnzawiam")
        players[id].resume()

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        id = ctx.message.server.id
        await self.client.say("Koniec odtwarzania")
        players[id].stop()


def setup(client):
    client.add_cog(Music(client))