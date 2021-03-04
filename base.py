import sqlite3


mydb = sqlite3.connect("database.sqlite")

mycur = mydb.cursor()

li = ['tits', 'ass', 'pussy', 'asian', 'milf', 'creampie', 'latina', 'lesbian', 'goth', 'schoolgirl', 'bikini', 'anal', 'teen', 'hentai', 'bukkake']
num = 0
for i in li:
    var = "SELECT Count(*) FROM {}".format(i)
    num += mycur.execute("SELECT Count(*) FROM tits").fetchone()[0]

print(num)
mydb.close()