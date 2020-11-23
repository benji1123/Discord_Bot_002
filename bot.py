from games import RockPaperScissorsHandler, TicTacToeHandler
from conversation import conversation
import metrics_utils
from dbl_class import TopGG

import discord
from dotenv import load_dotenv

import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TICTACTOE_PROMPT = "!2 tt"


class ZeroTwoBot(discord.Client):
    async def on_ready(self):
        self.dbl = TopGG(client)
        print("Connected")
        msg_count = metrics_utils.get_msg_count()
        servers = client.guilds
        num_servers = len(list(servers))
        activity_name = f"{num_servers} | {msg_count}k msgs"
        # activity_name = '| new GIFs -> "hi 02"'
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=activity_name
            )
        )

    async def on_message(self, msg):
        # ignore self
        if msg.author == self.user:
            return

        # conversation
        await conversation.respond_to_name(msg)
        await conversation.respond_to_certain_things(msg)
        await conversation.respond_to_google(msg)

        # games
        await RockPaperScissorsHandler.create_rps_game(client, msg)
        await TicTacToeHandler.create_ttt_game(client, msg)


client = ZeroTwoBot()
client.run(DISCORD_TOKEN)
