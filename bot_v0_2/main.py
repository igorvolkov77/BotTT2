import discord
from discord.ext import commands
from discord import utils
import config
import raid

bot = commands.Bot(command_prefix = config.settings['prefix'])

@bot.command()
async def raidend(ctx, akronim):
    roleID = config.role[akronim];
    role = utils.get(ctx.guild.roles, id = roleID);
    flag = False;
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
bot.run(config.settings['token'])
