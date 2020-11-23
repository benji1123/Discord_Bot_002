import metrics_utils

import dbl
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

import os

load_dotenv()
DBL_TOKEN = os.getenv("DBL_TOKEN")


class TopGG(commands.Cog):
    """
    This example uses tasks provided by discord.ext to create a task that posts guild count to top.gg every 30 minutes.
    """
    def __init__(self, bot):
        self.bot = bot
        self.token = DBL_TOKEN
        self.dblpy = dbl.DBLClient(self.bot, self.token)
        self.update_stats.start()

    def cog_unload(self):
        self.update_stats.cancel()

    @tasks.loop(minutes=2)
    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count."""
        await self.bot.wait_until_ready()
        try:
            server_count = len(self.bot.guilds)
            await self.dblpy.post_guild_count(server_count)
            print('Posted server count ({})'.format(server_count))

            msg_count = round(metrics_utils.get_msg_count() / 1000, 3)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server_count} | {msg_count}k msgs"))
        except Exception as e:
            print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))


def setup(bot):
    bot.add_cog(TopGG(bot))
