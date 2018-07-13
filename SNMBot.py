import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from DiscordBots.BotResources import *


Client = discord.Client()
client = commands.Bot(command_prefix="")
botName = "SNMBot#8413"

users = {}
try:
    with open("users.txt") as f:
        userdict = eval(f.read())
        for x in userdict.values():
            users[x["_User__userID"]] = User(
                x["_User__userID"],
                x["_User__rps_games"],
                x["_User__rps_wins"],
                x["_User__rps_losses"],
                RPSGame(
                    x["_User__userID"],
                    x["_User__rps_game"]["_RPSGame__round"],
                    x["_User__rps_game"]["_RPSGame__winner"],
                    x["_User__rps_game"]["_RPSGame__comp_wins"],
                    x["_User__rps_game"]["_RPSGame__user_wins"]
                ) if x["_User__rps_game"] is not None else None
            )
except FileNotFoundError: print("file not found")

print(users)

@client.event
async def on_ready():
    print("SNMBot has connected to its servers!")

@client.event
async def on_message(mes):
    if str(mes.author) != botName: #str(mes.channel.server) == "Bot Test Realm": # for debuggin
        try:
            print(users[mes.author.id].userID + ": " + mes.content + "\nResponse:")
        except KeyError:
            users[mes.author.id] = User(mes.author.id)
            print(mes.author.id + ": " + mes.content + "\nResponse:\nCreated new user")
        user = users[mes.author.id]
        if mes.content.lower().startswith("!rpsrank"):
            print("Showed user their rps rank")
            ranks = sorted(list(users.values()), key=lambda x: x.rps_kd, reverse=True)
            await client.send_message(
                mes.channel,
                "<@" + user.userID + "> RPS rank is #" + str([x.userID for x in ranks].index(user.userID) + 1) + "\n" + str(user.rps_kd)
            )
        if mes.content.lower().startswith("!playrps"):
            if user.rps_game is not None:
                print("Informed user of existing rps game")
                await client.send_message(
                    mes.channel,
                    "We're already playing a game <@" + mes.author.id + ">!\nHere's the status:\n" + user.rps_game.status(True)
                )
            else:
                user.play_rps()
                print("Started rps game")
                await client.send_message(
                    mes.channel,
                    "Alright <@" + mes.author.id + ">, let's play 3 rounds of Rock Paper Scissors!\n" +
                    "To pick type '!pick <your pick> in chat! (Example: !pick rock)"
                )
        elif mes.content.lower().startswith("!pick"):
            if user.rps_game is not None:
                result = user.rps_game.play_round((mes.content.split() + [""])[1])
                print("Played rps with user")
                if user.rps_game.winner is not None:
                    result += "\n\n The winner is " + user.rps_game.winner + "!\n Thanks for playing!"
                    user.game_over_rps()
                    print("Displayed winner")
                await client.send_message(mes.channel, result)
            else:
                print("Informed user that they have not started a rps game")
                await client.send_message(mes.channel, "You first have to start a game by typing *!playrps* <@" + mes.author.id + ">!")
        print()
        with open("users.txt", "w") as f:
            f.write(str(users))


client.run("NDY2NzE4MzIyMTY0MTA1MjE2.DilKtQ.OIUu-fTBigSfM8DvdhXU0pTkiS8")