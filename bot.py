from games import RockPaperScissorsHandler, TicTacToeHandler
from conversation import conversation, help_msg_sender
import metrics_utils
from dbl_class import TopGG

from discord import AutoShardedClient
from dotenv import load_dotenv

import os

SHARD_COUNT=2
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


class ZeroTwoBot(AutoShardedClient):

    async def on_ready(self) -> None:
        self.dbl = TopGG(client)
        print("Connected")
        print(f"num shards: {len(self.latencies)}")

    async def on_message(self, msg) -> None:
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


client = ZeroTwoBot(shard_count=SHARD_COUNT)
client.run(DISCORD_TOKEN)
