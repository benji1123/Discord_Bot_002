import metrics_utils

import dbl
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

import os
import random

load_dotenv()
DBL_TOKEN = os.getenv("DBL_TOKEN")


class TopGG(commands.Cog):
    """
    This example uses tasks provided by discord.ext to create a task that posts guild count to top.gg periodically.
    """
    def __init__(self, bot):
        self.bot = bot
        self.token = DBL_TOKEN
        self.dblpy = dbl.DBLClient(self.bot, self.token)
        self.update_stats.start()

    def cog_unload(self) -> None:
        self.update_stats.cancel()

    @tasks.loop(minutes=10)
    async def update_stats(self) -> None:
        """update server count periodically."""
        await self.bot.wait_until_ready()
        try:
            print(f"user: {len(self.bot.users)}")
            # server count
            guilds = self.bot.guilds
            guild_count = len(guilds)
            await self.dblpy.post_guild_count(guild_count)
            print('Posted server count ({})'.format(guild_count))
            # member count across all guilds
            member_count = 0
            for g in guilds:
                member_count += g.member_count
            print(f"num users: {member_count}")
            # shuffle the bot's presence
            msg_count_presence = f"{metrics_utils.get_msg_count()} 💌"
            member_count_presence = f"~{round(member_count/1000000, 1)}M darlings"
            xmas_presence = "MERRY XMAS"
            presence = random.choice([msg_count_presence, msg_count_presence, member_count_presence])
            
            shard_count = len(self.bot.latencies)
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.playing, name=f"in {guild_count}({shard_count}) | {presence}"))
        except Exception as e:
            print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))


def setup(bot) -> None:
    bot.add_cog(TopGG(bot))
