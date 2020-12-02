from conversation import google_utils
from conversation import csv_utils
import metrics_utils

import discord

import os
import random
from typing import List

IMAGE_FILE_EXTENSIONS = [".jpg", ".png", ".gif"]
IMAGE_DIR = os.path.join(os.path.dirname(__file__), "zerotwo/")

NAMES = {" 002", " 02", "002 ", "02 ", "darling", "dino", "dinosaur", "waifu", "zerotwo", "o2", "oxygen", "003"}
RESPONSE_POOL_FOR_NAME = [IMAGE_DIR + filename for filename in os.listdir(IMAGE_DIR)]

EXPLICIT_THINGS_TO_RESPOND_TO = csv_utils.get_dialog_dict(data_path="conversation/dialog_data/fixed_responses.csv")
TRIGGER_WORDS_TO_RESPOND_TO = csv_utils.get_dialog_dict(data_path="conversation/dialog_data/trigger_words.csv")


async def respond_to_name(msg: discord.Message):
    """Send a response if 02's name or alias is detected."""
    msg_content = msg.content.lower()
    if any(name in msg_content for name in NAMES):
        await send_random(msg, RESPONSE_POOL_FOR_NAME)


async def respond_to_trigger_word(msg: discord.Message):
    """Send a response if a message contains a certain word."""
    msg_content = msg.content.lower()
    for trigger in TRIGGER_WORDS_TO_RESPOND_TO:
        if trigger in msg_content:
            await send_random(msg, responses=TRIGGER_WORDS_TO_RESPOND_TO[trigger])


async def respond_to_certain_things(msg: discord.Message):
    """Send a response to a specific message."""
    msg_content = msg.content.lower()
    if msg_content in EXPLICIT_THINGS_TO_RESPOND_TO:
        await send_random(msg, responses=EXPLICIT_THINGS_TO_RESPOND_TO[msg_content])


async def respond_to_google(msg: discord.Message):
    """Send a response to a google request."""
    msg_content = msg.content.lower()
    # google-command prefix
    if msg_content.startswith("!2 g"):
        msg_content = msg_content.split("!2 g")
        if len(msg_content) == 2:
            query = msg_content[1]
            # get result for query
            result = google_utils.chatbot_query(query)
            await msg.channel.send(result)


# helpers


async def send_random(msg: discord.Message, responses: List[str]):
    """Sends a random message from a list, including images"""
    print(f"respond to {msg.content}")
    metrics_utils.increment_conversation_count()  # count outgoing messages
    random_response = random.choice(responses)
    # check if response is an image-file
    if is_image(file_path=random_response):
        await msg.channel.send(file=discord.File(random_response))
    elif ".DS_Store" not in random_response:
        await msg.channel.send(random_response)
    else:
        await msg.channel.send("u found a bug in my code!")


def is_image(file_path: str) -> bool:
    return file_path[-4:].lower() in IMAGE_FILE_EXTENSIONS and os.path.exists(file_path)
