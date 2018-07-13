import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix="")
botName = "TestBot_1#1053"
roles = {
    "admin": "466705244387016714"
}

@client.event
async def on_ready():
    print("bot is ready!")

@client.event
async def on_message(mes):
    print(mes.author, ":", mes.content)
    if str(mes.author) != botName:
        if "cookie" in mes.content.lower():
            await client.send_message(mes.channel, ":cookie:")
        if mes.content.lower().startswith("!ping"):
            userID = mes.author.id
            await client.send_message(mes.channel, "<@"+userID+"> Pong!")
        if mes.content.lower().startswith("!amiadmin"):
            if roles["admin"] in [x.id for x in mes.author.roles]:
                await client.send_message(mes.channel, "Yes")
            else:
                await client.send_message(mes.channel, "No")
client.run("NDY2Njc2MjA3NjA2MzAwNjk3.Dif1Dw.DDsLErpSKs8i_jU0n3DmFkH_GIk")