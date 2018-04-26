import discord
from discord.ext import commands



bot = commands.Bot(command_prefix="!")
allowed_roles = ["knight", "wizard", "priest", "berzerker",
                 "heavy gunner", "assassin", "thief", "archer"]

@bot.event
async def on_message(message):
    if message.content.startswith("!addc"):
        user = message.author
        userin = str(message.content[6:]).lower()
        role = discord.utils.get(message.server.roles, name=userin)
        if userin in str(role) and userin in allowed_roles:
            await bot.add_roles(user, role)
            changeinfo = discord.Embed(color=0x00ff00)
            changeinfo.add_field(name="You have added a class role", value=userin)
            await bot.send_message(message.channel, embed=changeinfo)
        else:
            await bot.send_message(message.channel, "Incorrect Command, check channel description for roles")

    elif message.content.startswith("!delc"):
        user = message.author
        userin = str(message.content[6:]).lower()
        role = discord.utils.get(message.server.roles, name=userin)
        if userin in str(role) and userin in allowed_roles:
            await bot.remove_roles(user, role)
            changeinfo = discord.Embed(color=0x00ff00)
            changeinfo.add_field(name="You have deleted one of your classes", value=userin)
            await bot.send_message(message.channel, embed=changeinfo)
        else:
            await bot.send_message(message.channel, "Incorrect Command, check channel description for roles")

# @bot.command(pass_context=True)
# async def X(ctx):
s = open("C:/Users/jeffe/secret.txt", "r")
secret = s.read()
bot.run(secret)
