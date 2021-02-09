from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import random


def get_pic(part):
    parts = {"tits": "https://www.pornpics.com/natural-tits/",
             "ass": "https://www.pornpics.com/ass/",
             "pussy": "https://www.pornpics.com/pussy/",
             "asian": "https://www.pornpics.com/asian/",
             "milf": "https://www.pornpics.com/milf/",
             "midget": "https://www.pornpics.com/?q=midget"
             }
    url = parts[part]
    print(url)
    # print(url)
    html = requests.get(url).content
    root = BeautifulSoup(html, "html.parser")
    pics = []
    for picture in root.find_all('a', {"class": "rel-link"}):
        pic = picture.find('img').get('data-src')
        pics.append(pic)
    wanted_pic = random.choice(pics)
    print(wanted_pic)
    return wanted_pic


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('We have logged in as bot')


@client.command()
async def tits(ctx):
    await ctx.send(get_pic("tits"))

@client.command()
async def ass(ctx):
    await ctx.send(get_pic("ass"))

@client.command()
async def pussy(ctx):
    await ctx.send(get_pic("pussy"))

@client.command()
async def asian(ctx):
    await ctx.send(get_pic("asian"))

@client.command()
async def baklava(ctx):
    await ctx.send("Jebi se stricel")

@client.command()
async def burek(ctx):
    await ctx.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fu9UnoW4Zr2M%2Fmaxresdefault.jpg&f=1&nofb=1")

@client.command()
async def jesus(ctx):
    await ctx.send("https://deebrestin.com/wp-content/uploads/2014/04/Jesus-Good-Shepherd-06.jpg")

@client.command()
async def milf(ctx):
    await ctx.send(get_pic("milf"))

@client.command()
async def midget(ctx):
    await ctx.send(get_pic("midget"))


client.run("") #token
