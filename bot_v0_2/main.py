import discord
from discord.ext import commands
from discord import utils
import config
import raid
import createTable
import random

bot = commands.Bot(command_prefix = config.settings['prefix'])

@bot.command()
async def raidend(ctx, akronim):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =raidend ".format(ctx.message.author)
    mes+=' '.join(akronim)
    await my_channel.send(mes)
    roleID = config.role[akronim];
    role = utils.get(ctx.guild.roles, id = roleID);
    flag = True; #надо исправить на False
    await ctx.send(role.members)
    for member in role.members:
        await ctx.send(member.id)
        await ctx.send(ctx.author.id)
        if (member.id == ctx.author.id):
            flag = True;
    if (flag == False):
        await ctx.send("You don't have a role!");
    else:
        await ctx.send("Ok");
        result = raid.raid_obr(akronim);
        await ctx.send(result);
        await ctx.send(file=discord.File('saved_figure.png'))

@bot.command()
async def createClan(ctx, akronim):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =createClan ".format(ctx.message.author)
    mes+=' '.join(akronim)
    await my_channel.send(mes)
    #result = createTable.create_new_clan(akronim);
    #await ctx.send(result);
    await ctx.send("This function is currently not enabled.");

@bot.command()
async def Kt(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =Kt ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    await ctx.message.delete()
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def Kto(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =Kto ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def kt(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =kt ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    await ctx.message.delete()
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def kto(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =kto ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def кт(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =кт ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    await ctx.message.delete()
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def кто(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =кто ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def Кт(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =Кт ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    await ctx.message.delete()
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def Кто(ctx, *arg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =Кто ".format(ctx.message.author)
    mes+=' '.join(arg)
    await my_channel.send(mes)
    name = ["Стас","Максим","Антон","Игорь","Саркис","Алексей","Миша","Андрей","Артем", "Вадим", "Емеля"]
    a = " ".join(arg)
    k = random.randint(0, 10)
    b = name[k]+" "+a
    b = b.replace("?",".")
    await ctx.send(b);

@bot.command()
async def mes(ctx, *msg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =mes ".format(ctx.message.author)
    mes+=' '.join(msg)
    await my_channel.send(mes)
    await ctx.message.delete()
    await ctx.send(' '.join(msg))

@bot.command()
async def мес(ctx, *msg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =мес ".format(ctx.message.author)
    mes+=' '.join(msg)
    await my_channel.send(mes)
    await ctx.message.delete()
    await ctx.send(' '.join(msg))

@bot.command()
async def БотПишетВОбщий(ctx, *msg):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =БотПишетВОбщий ".format(ctx.message.author)
    mes+=' '.join(msg)
    await my_channel.send(mes)
    await ctx.message.delete()
    my_channel_1 = bot.get_channel(852785029603786762)
    await my_channel_1.send(' '.join(msg))

@bot.command()
async def sm(ctx):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =sm ".format(ctx.message.author)
    await my_channel.send(mes)
    await ctx.send("SM (см) или сайлент марш ( <:3silent:916195886185476146> ) - механика игры, которая позволяет проходить этапы пока игрок не в сети. Благодаря легендарному сету Sly Wolf позволяет доходить до 90% от мс. Время, за которое проходятся этапы можно рассчитать самостоятельно тут: https://docs.google.com/spreadsheets/d/1sH5mFmcpn9zeXTnGN1fI8L6A1dNHE0szxSzX-olOiCo/edit?usp=drivesdk")

@bot.command()
async def ивент(ctx):
    my_channel = bot.get_channel(967803977402040370)
    mes = "{} написал Боту команду: =sm ".format(ctx.message.author)
    await my_channel.send(mes)
    await ctx.send("В игре существует ивент, в котором вам необходимо собирать ивент валюту с различных источников (ежедневные задания, феи, атаки в рейде, престижи). Длится он обычно около 3-х недель и стартует вместе с обновлениями игры раз в месяц. Собирая ивент валюту и достигая определённых значений, вы получаете небольшие вознаграждения (питомцев, оружия героев, алмазы и т.д.). Достигая числа в 3000 и собирая валюту далее, вы можете побороться в топе за бейдж в своём профиле. Их бывает 4 вида: бронзовый, серебрянный, золотой и платиновый. На главном экране разверните панель слева, под значком короны обычно располагается значок с подробной информацией о турнире. Там же можно найти и награды за каждый бейдж. Стоит упомянуть только то, что навсегда остается только бонус к урону, остальные же бонусы продлятся ровно до конца следующего ивента.")

bot.run(config.settings['token'])
