import rps
import conversation
import TicTacToeHandler
import metrics_utils
from dbl_class import TopGG

import discord

import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

TICTACTOE_PROMPT = "!2 tt"


class ZeroTwoBot(discord.Client):
    async def on_ready(self):
        # self.dbl = TopGG(client)
        num_servers = str(len(list(client.guilds)))
        print("Connected")
        msg_count = round(metrics_utils.get_msg_count() / 1000, 2)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{num_servers} | {msg_count}k msgs"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        msg_content = message.content.lower()

        # if someone says something we care about
        await conversation.respond_to_name(message, msg_content)
        await conversation.respond_to_certain_things(message, msg_content)
        await conversation.respond_to_math(message, msg_content)
        await conversation.respond_to_google(message, msg_content)

        # user wants to play Rock Paper Scissors
        await rps.play_rps(client, message, msg_content)
        # a user has requested a TicTacToe game
        if message.content.startswith(TICTACTOE_PROMPT):
            await TicTacToeHandler.start_game(client, message.channel, message.author)


client = ZeroTwoBot()
client.run(DISCORD_TOKEN)

