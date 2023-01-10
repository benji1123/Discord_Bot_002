'''
Return an embed that shows each bot-command and the number of times it's been called
'''
import discord
import json


METRICS_REPORT_EMBED = discord.Embed(title="002 Bot Metrics Report",
                               description="Began tracking most metrics Jan 09, 2023",
                               color=0xffadd2)
METRICS_REPORT_EMBED.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/7/71/Franxx_Zero_Two.jpg")

# data is tracked in a JSON
# TODO: the above json file is updated live, 
# but we aren't reading the changes until bot reset
metric_file = open("metrics.json", "r")
metrics_data = json.load(metric_file)
metric_file.close()

# create an embed field for each command
for command, count in metrics_data.items():
    inline = False if command in ["*ALL CONVERSATION*", "*name/aliases (i.e. '002')*", "IMAGES SENT"] else True
    METRICS_REPORT_EMBED.add_field(name=command, value=count, inline=inline)

async def respond_to_report_request(msg) -> None:
    msg_content = msg.content.lower()
    if msg_content in ["!2 metrics", "!2 report"]:
        await msg.channel.send(embed=METRICS_REPORT_EMBED)
