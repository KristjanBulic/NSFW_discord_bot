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


parts = {"tits": ["https://www.pornhub.com/albums/female-straight-uncategorized?search=tits"],
        "ass": ["https://www.pornhub.com/album/13673211",
                "https://www.pornhub.com/album/41269771",
                "https://www.pornhub.com/album/14895152",
                "https://www.pornhub.com/album/27543271",
                "https://www.pornhub.com/album/25486162"
                ],
        "pussy": ["https://www.pornhub.com/album/18822201",
                  "https://www.pornhub.com/album/8172291",
                  "https://www.pornhub.com/album/39267981",
                  "https://www.pornhub.com/album/26276481"
                  ],
         "asian": ["https://www.pornhub.com/album/24154402",
                   "https://www.pornhub.com/album/30356461",
                   "https://www.pornhub.com/album/28715371",
                   "https://www.pornhub.com/album/19627631",
                   "https://www.pornhub.com/album/330228",
                   ],
             "milf": ["https://www.pornhub.com/album/3270371",
                      "https://www.pornhub.com/album/69141302",
                      "https://www.pornhub.com/album/32499621",
                      ],
             "creampie": ["https://www.pornhub.com/album/5856301",
                          "https://www.pornhub.com/album/51808822",
                          "https://www.pornhub.com/album/1476601",
                          "https://www.pornhub.com/album/36648181",
                          "https://www.pornhub.com/album/66380342",
                          "https://www.pornhub.com/album/66522132",
                          "https://www.pornhub.com/album/68796241",
                          "https://www.pornhub.com/album/69403682"],
             "latina": ["https://www.pornhub.com/album/28099091",
                        "https://www.pornhub.com/album/38006652",
                        "https://www.pornhub.com/album/23574702",
                        "https://www.pornhub.com/album/8335721",
                        "https://www.pornhub.com/album/19312171"
                        ],
             "goth": ["https://www.pornhub.com/album/30171381"],
             "schoolgirl": ["https://www.pornhub.com/album/30094061"],
             "bikini": ["https://www.pornhub.com/album/39585521?page=2",
                        "https://www.pornhub.com/album/39585521?page=3",
                        ],
             "anal": ["https://www.pornhub.com/album/2893681",
                      "https://www.pornhub.com/album/2893491"
                      ],
             "teen": ["https://www.pornhub.com/album/18822201",
                      "https://www.pornhub.com/album/20428591",
                      "https://www.pornhub.com/album/30216231"
                      ],
             "hentai": ["https://www.pornhub.com/album/36835462",
                        "https://www.pornhub.com/album/23391952",
                        "https://www.pornhub.com/album/43879261",
                        "https://www.pornhub.com/album/64958282",
                        "https://www.pornhub.com/album/67818012",
                        "https://www.pornhub.com/album/18035191",
                        "https://www.pornhub.com/album/62291472"
                        ],
            "bukkake": ["https://www.pornhub.com/album/11147261",
                        "https://www.pornhub.com/album/6559532",
                        "https://www.pornhub.com/album/27159021",
                        "https://www.pornhub.com/album/21233412"],

            'lesbian':["https://www.pornhub.com/album/40833801", "https://www.pornhub.com/album/19818771",
                        "https://www.pornhub.com/album/19981921", "https://www.pornhub.com/album/30801511",
                        "https://www.pornhub.com/album/3786792", "https://www.pornhub.com/album/1795901",
                        "https://www.pornhub.com/album/10469641", "https://www.pornhub.com/album/11423461",
                        "https://www.pornhub.com/album/11324811", "https://www.pornhub.com/album/68271182",
                         "https://www.pornhub.com/album/1795901", "https://www.pornhub.com/album/1951152",
                        "https://www.pornhub.com/album/4249681", "https://www.pornhub.com/album/1795891",
                        "https://www.pornhub.com/album/6184192"],
            'retro' : ["https://www.pornhub.com/album/28845121",
                        "https://www.pornhub.com/album/5769941",
                        "https://www.pornhub.com/album/6101192",
                        "https://www.pornhub.com/album/7654551",
                        "https://www.pornhub.com/album/3822732",
                        "https://www.pornhub.com/album/34501362",
                        "https://www.pornhub.com/album/34500352",
                        "https://www.pornhub.com/album/13797231",
                        "https://www.pornhub.com/album/14489181",
                        "https://www.pornhub.com/album/14488861",
                        "https://www.pornhub.com/album/13804712",
                        "https://www.pornhub.com/album/19724721",
                        ]
             }



i = 1
for part in parts.keys():
    table_create = "CREATE TABLE {} (ID INTEGER PRIMARY KEY AUTOINCREMENT, url BLOB NOT NULL)".format(part)
    mycurslor.execute(table_create)
    for url_album in parts[part]:
        print(url_album, i)
        get_from_pornhub(url_album, part)
        i += 1

mydb.close()
print("done")
print(i)