import sqlite3


mydb = sqlite3.connect("database.sqlite")


parts = {"tits": "https://www.pornpics.com/recent/natural-tits/",
        "ass": "https://www.pornpics.com/recent/ass/",
        "pussy": "https://www.pornpics.com/recent/pussy/",
         "asian": "https://www.pornpics.com/recent/asian/",
             "milf": "https://www.pornpics.com/recent/milf/",
             "creampie": "https://www.pornpics.com/recent/creampie/",
             "latina": "https://www.pornpics.com/recent/latina/",
             "lesbian": "https://www.pornpics.com/recent/lesbian/",
             "goth": "https://www.pornpics.com/recent/goth/",
             "schoolgirl": "https://www.pornpics.com/recent/schoolgirl/",
             "bikini": "https://www.pornpics.com/recent/bikini/",
             "anal": "https://www.pornpics.com/recent/anal/",
             "teen": "https://www.pornpics.com/recent/teen/",
             "hentai": "none",
            "bukkake": "none",
             }
li = []
mycurslor = mydb.cursor()
for key in parts.keys():
    li.append(key)
    print(li)

mydb.close()

