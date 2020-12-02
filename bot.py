from games import RockPaperScissorsHandler, TicTacToeHandler
from conversation import conversation, help_msg_sender
import metrics_utils
from dbl_class import TopGG

import discord
from dotenv import load_dotenv

import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


class ZeroTwoBot(discord.Client):
    async def on_ready(self):
        self.dbl = TopGG(client)
        print("Connected")

    async def on_message(self, msg):
        # ignore self
        if msg.author == self.user:
            return

        # conversation
        await help_msg_sender.respond_to_help(msg)
        await conversation.respond_to_name(msg)
        await conversation.respond_to_trigger_word(msg)
        await conversation.respond_to_certain_things(msg)
        await conversation.respond_to_google(msg)

        # games
        await RockPaperScissorsHandler.create_rps_game(client, msg)
        await TicTacToeHandler.create_ttt_game(client, msg)


client = ZeroTwoBot()
client.run(DISCORD_TOKEN)
