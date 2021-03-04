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
async def latina(ctx):
    await ctx.send(get_pic("latina"))


@client.command()
async def baklava(ctx):
    await ctx.send("Jebi se stricel")


@client.command()
async def burek(ctx):
    await ctx.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fu9UnoW4Zr2M%2Fmaxres"
                   "default.jpg&f=1&nofb=1")


@client.command()
async def jesus(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/808725069399457862/809189804611862580/EP2-IA-60435_R_8x10-56"
                   "a83bea3df78cf7729d314a.jpg")


@client.command()
async def milf(ctx):
    await ctx.send(get_pic("milf"))



@client.command()
async def creampie(ctx):
    await ctx.send(get_pic("creampie"))


@client.command()
async def goth(ctx):
    await ctx.send(get_pic("goth"))


@client.command()
async def schoolgirl(ctx):
    await ctx.send(get_pic("schoolgirl"))


@client.command()
async def bikini(ctx):
    await ctx.send(get_pic("bikini"))


@client.command()
async def anal(ctx):
    await ctx.send(get_pic("anal"))


@client.command()
async def teen(ctx):
    await ctx.send(get_pic("teen"))


@client.command()
async def bukkake(ctx):
    await ctx.send(get_pic("bukkake"))


@client.command()
async def superhentai(ctx):
    i = 0
    while i < 20:
        try:
            await ctx.send(get_pic("hentai"))
            i += 1
        except:
            break

@client.command()
async def gigahentai(ctx):
    i = 0
    while i < 70:
        try:
            await ctx.send(get_pic("hentai"))
            i += 1
        except:
            break


@client.command()
async def pentahentai(ctx):
    i = 0
    while i < 200:
        try:
            await ctx.send(get_pic("hentai"))
            i += 1
        except:
            break


@client.command()
async def hentai(ctx):
    await ctx.send(get_pic("hentai"))


@client.command()
async def bukkake(ctx):
    await ctx.send(get_pic("bukkake"))


client.run("")  # token
