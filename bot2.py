from discord.ext import commands
import sqlite3
import random


def get_pic(table):
    mydb = sqlite3.connect("database.sqlite")
    cursor = mydb.cursor()
    var_min = "SELECT min(ID) FROM {}".format(table)
    var_max = "SELECT max(ID) FROM {}".format(table)
    min = cursor.execute(var_min).fetchone()[0]
    max = cursor.execute(var_max).fetchone()[0]
    id = random.randint(min, max)
    sql = """SELECT url FROM {} WHERE ID={}""".format(table, id)
    pic = cursor.execute(sql)
    pic = pic.fetchone()[0]
    mydb.close()
    return pic


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print('We have logged in as bot')


    #cteate functions as example bellow
@client.command()
async def category_you_want(ctx):
    await ctx.send(get_pic("table name from database"))



client.run("")  # token
