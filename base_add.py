import sqlite3
import requests
from bs4 import BeautifulSoup


mydb = sqlite3.connect("database.sqlite")

mycurslor = mydb.cursor()


def get_from_pornhub(album, table):
    url = album
    html = requests.get(url).content
    root = BeautifulSoup(html, "html.parser")
    pics = []
    for pic in root.find_all('div', {"class": "js_lazy_bkg photoAlbumListBlock"}):
        picture = "https://www.pornhub.com" + pic.find('a').get('href')
        pics.append(picture)

    for wanted_pic in pics:
        try:
            wanted_pic = BeautifulSoup(requests.get(wanted_pic).content, "html.parser")
            pic_url = wanted_pic.find('div', {"class": "centerImage"}).find('img').get('src')
            var = """INSERT INTO {} (url) VALUES ("{}")""".format(table, pic_url)
            print(var)
            mycurslor.execute(var)
        except:
            pass

    mydb.commit()


category = {"category" : ['list of album urls']
             }



for cat in category.keys():
    table_create = "CREATE TABLE {} (ID INTEGER PRIMARY KEY AUTOINCREMENT, url BLOB NOT NULL)".format(cat)
    mycurslor.execute(table_create)
    for url_album in category[cat]:
        print(url_album)
        get_from_pornhub(url_album, part)
        

mydb.close()
print("done")

