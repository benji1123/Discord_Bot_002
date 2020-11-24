import discord

async def respond_to_help(msg):
    msg_content = msg.content.lower()
    if msg_content == "!2 help":
        embed = discord.Embed(title="002 Guide", url="https://top.gg/bot/774732068282171424",
                              description="Join <https://discord.gg/cVAGdqst48> "
                                          "to suggest GIFs or bot-dialog.",
                              color=0xffadd2)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/7/71/Franxx_Zero_Two.jpg")
        embed.add_field(name="🎥 Trigger a 002 GIF",
                        value="Send a msg with `002` or `02` in it (try sending: *sup 002*). "
                              "The same works for: `dino`, `waifu`, `o2` and more.",
                        inline=False)
        embed.add_field(name="❤️  What does 002 respond to?",
                        value="**22** phrases including: `yummy`,"
                              "`rpg buy edgy lootbox`, `rip`. Periodically updating these!",
                        inline=False)
        embed.add_field(name="🔎  Googling stuff!", value="**Try:** `!2 g do lizard people control the government?`",
                        inline=False)
        embed.add_field(name="❎ ️️🅾️  TicTacToe:", value="`!2 tt`", inline=True)
        embed.add_field(name="🤘 Rock Paper Scissors", value="`!2 rps`", inline=True)
        embed.add_field(name="🙏 Vote", value="<https://top.gg/bot/774732068282171424/vote>", inline=True)
        await msg.channel.send(embed=embed)
