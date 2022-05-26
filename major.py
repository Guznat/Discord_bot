from discord.ext import commands
import random



class Major(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jaki_major(self, ctx):
        majorek = ["https://www.wykop.pl/cdn/c3201142/comment_uJUJzD87nrm6IfN0clHz5e9oAlbE9mAp.jpg",
                   "https://pbs.twimg.com/media/D63H6kHWwAEG5u4.jpg",
                   "https://images.genius.com/6ad4ab79eb102b81369ab5fefd09ed16.900x900x1.jpg",
                   "https://www.wykop.pl/cdn/c3201142/comment_FE6FEMi1tXLht26eS4ZjCSqjcIWXVxZA.jpg",
                   "https://www.wykop.pl/cdn/c3201142/comment_ofEcheZodrV4drjoEsVGIluzREta1TIp.jpg",
                   "https://i.ytimg.com/vi/7KoS19DfN4o/maxresdefault.jpg",
                   "https://www.wykop.pl/cdn/c3201142/comment_TVUIWEzz292zmaAGPrIxLWyJ93kAZgw7.jpg",
                   "https://www.wykop.pl/cdn/c3201142/comment_UJj4aWodj0kKN4vQm0bt7VuOJ9xnmCwJ.jpg",
                   "https://i.ytimg.com/vi/mSrZ7kvObmY/maxresdefault.jpg",
                   "https://i.ytimg.com/vi/ndyi9bKAohw/maxresdefault.jpg",
                   "https://i.ytimg.com/vi/qvaLWNVXS9M/maxresdefault.jpg",
                   "https://i.ytimg.com/vi/7zD2ISnMiWs/maxresdefault.jpg",
                   "https://pbs.twimg.com/media/EQsCTJmWAAAagDV.jpg",
                   "https://pbs.twimg.com/media/EQsCTJnX0AQzBhv?format=jpg&name=small"]
        await ctx.channel.send(f"RNG boże wylosowało dla Ciebie psznego Majorka {random.choice(majorek)}")



def setup(client):
    client.add_cog(Major(client))