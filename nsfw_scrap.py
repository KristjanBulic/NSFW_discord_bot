from bs4 import BeautifulSoup
import requests
import random


def get_albums(part):
    par = {"class": "photoAlbumListBlock js_lazy_bkg"}
    parts = {"tits": "https://www.pornhub.com/albums/female-straight-uncategorized?search=tits&o=mr&verified=1",
             "ass": "https://www.pornhub.com/albums/female-straight-uncategorized?search=ass",
             "pussy": "https://www.pornhub.com/albums/female-straight-uncategorized?search=pussy",
             "asian": "https://www.pornhub.com/albums/female-straight-uncategorized?search=asian",
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

def get_pic2(part):
    par = {"class": "ll-loaded"}
    parts = {"tits": "https://www.pornpics.com/natural-tits/",
             "ass": "https://www.pornpics.com/ass/",
             "pussy": "https://www.pornpics.com/pussy/",
             "asian": "https://www.pornpics.com/asian/",
             }
    url = parts[part]
    #print(url)
    html = requests.get(url).content
    root = BeautifulSoup(html, "html.parser")
    pics = []
    for picture in root.find_all('a', {"class":"rel-link"}):
        pic = picture.find('img').get('src')
        pics.append(pic)
    wanted_pic = random.choice(pics)
    print(wanted_pic)

def hentai():
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
print(get_pic2("pussy"))