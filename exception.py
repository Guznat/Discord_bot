import traceback
import sys
from discord.ext import commands
import discord


class CommandErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command
    async def on_command_error(self, ctx, error):    #TODO problem with displayig the message
        if isinstance(error, commands.CommandNotFound):
            return await ctx.send(f'{ctx.command} nie istnieje. Dostępne komendy znajdziesz tutaj: $help')
        elif isinstance(error, commands.TooManyArguments):
            return await ctx.send(f'{ctx.command} za dużo argumentów')
        elif isinstance(error, commands.BadArgument):
            return await ctx.send("Złe dane.")


def setup(client):
    client.add_cog(CommandErrorHandler(client))
