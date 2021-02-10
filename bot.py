from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import random


used = []


def get_pic(part):
    parts = {"tits": "https://www.pornpics.com/natural-tits/",
             "ass": "https://www.pornpics.com/ass/",
             "pussy": "https://www.pornpics.com/pussy/",
             "asian": "https://www.pornpics.com/asian/",
             "milf": "https://www.pornpics.com/milf/",
             "midget": "https://www.pornpics.com/?q=midget",
             "creampie": "https://www.pornpics.com/creampie/",
             }

    url = parts[part]
    html = requests.get(url).content
    root = BeautifulSoup(html, "html.parser")
    pics = []
    for picture in root.find_all('a', {"class": "rel-link"}):
        pic = picture.find('img').get('data-src')
        pics.append(pic)

    wanted_pic = random.choice(pics)

    if wanted_pic in used:
        get_pic(part)

    else:
        used.append(wanted_pic)
        return wanted_pic


def get_hentai():
    html = requests.get("https://www.pornhub.com/album/36835462").content
    root = BeautifulSoup(html, "html.parser")
    pics = []
    for pic in root.find_all('div', {"class": "js_lazy_bkg photoAlbumListBlock"}):
        picture = "https://www.pornhub.com" + pic.find('a').get('href')
        pics.append(picture)

    wanted_pic = random.choice(pics)
    wanted_pic = BeautifulSoup(requests.get(wanted_pic).content, "html.parser")
    hen = wanted_pic.find('div', {"class": "centerImage"}).find('img').get('src')
    return hen


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
    await ctx.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fu9UnoW4Zr2M%2Fmaxres"
                   "default.jpg&f=1&nofb=1")


@client.command()
async def jesus(ctx):
    await ctx.send("https://deebrestin.com/wp-content/uploads/2014/04/Jesus-Good-Shepherd-06.jpg")


@client.command()
async def milf(ctx):
    await ctx.send(get_pic("milf"))


@client.command()
async def midget(ctx):
    await ctx.send(get_pic("midget"))


@client.command()
async def creampie(ctx):
    await ctx.send(get_pic("creampie"))


@client.command()
async def supermidget(ctx):
    i = 0
    while i < 20:
        try:
            await ctx.send(get_pic("midget"))
            i += 1
        except:
            break


@client.command()
async def hentai(ctx):
    await ctx.send(get_hentai())


client.run("") #token
