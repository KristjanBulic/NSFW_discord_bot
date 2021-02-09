from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import random


def get_albums(part):
    par = {"class": "photoAlbumListBlock js_lazy_bkg"}
    parts = {"tits": "https://www.pornhub.com/albums/female-straight-uncategorized?search=tits&o=mv",
             "ass": "https://www.pornhub.com/albums/female-straight-uncategorized?search=ass&o=mv",
             "pussy": "https://www.pornhub.com/albums/female-straight-uncategorized?search=pussy&o=mv",
             "asian": "https://www.pornhub.com/albums/female-straight-uncategorized?search=asian&o=mv",
             }
    url = parts[part]
    html = requests.get(url).content
    root = BeautifulSoup(html, "html.parser")
    albums = []
    for album in root.find_all('div', par):
        album = "https://www.pornhub.com" + album.find('a').get('href')
        albums.append(album)
    return albums


def get_pic(part):
    albums = get_albums(part)
    album_url = random.choice(albums)
    html = requests.get(album_url).content
    page = BeautifulSoup(html, "html.parser")
    pics_urls = []
    for pic in page.find_all('div', {"class": "js_lazy_bkg photoAlbumListBlock"}):
        pic_url = "https://www.pornhub.com" +  pic.find('a').get('href')
        pics_urls.append(pic_url)

    wanted_pic = requests.get(random.choice(pics_urls)).content
    page = BeautifulSoup(wanted_pic, "html.parser")
    picture = page.find('div', {"class": "centerImage"}).find('img').get('src')
    return picture


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
async def vagina(ctx):
    await ctx.send(get_pic("pussy"))

@client.command()
async def asian(ctx):
    await ctx.send(get_pic("asian"))

@client.command()
async def baklava(ctx):
    await ctx.send("Jebi se stricel")

@client.command()
async def burek(ctx):
    await ctx.send("Ta te barem ate vbrisau v rjuho")


client.run("") #token
