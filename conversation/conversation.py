from conversation import google_handler
import metrics_utils

import discord

import os
import random


IMAGE_FILE_EXTENSIONS = [".jpg", ".png", ".gif"]

DIR_PATH = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(DIR_PATH, "zerotwo/")
NAMES_RESPONSES = os.listdir(IMAGE_DIR)

NAMES = [" 002", " 02", "002 ", "02 ", "darling", "dino", "dinosaur", "waifu", "zerotwo", "o2", "oxygen", "003"]
THINGS_TO_RESPOND_TO = {
    "rpg miniboss @here": ["fight", "please accept my moral support", "we shall win"],
    "rpg arena @everyone": ["join", "moral support", "we cannot lose"],
    "stfu": ["don't be mean, darling!", "that hurts"],
    "rpg stfu": ["no! 😠", "rpg go away"],
    "lol": ["🤣", "knee slapper", "lmao", "lolololol"],
    "lmao": ["🤣"],
    "haha": ["aHHHaahhHAaahA so funny SO FUNNY i'm dyyyyyying 💀"],
    "rip": ["press 'F' to pay respects", "rest in peace", "rest in pieces"],
    "❤️": ["listen to the beat, beat, beat", "ily too", "💙💙💙"],
    "huh?": ["nani??"],
    "yummy": ["i'm hungry", "my favorite food is mice", "hello i am 02 and i am hungry", "i want", "cookie?"],
    "ohh": ["THAT MAKES SENSE", "we are enlightened", "the moon landing was faked"],
    "congrats": ["yaaaaay great job 🥳", "nice!"],
    "!np": ["i think... i like this song", "this song sucks", "listen to Kiss of Death"],
    "rpg buy edgy lootbox": ["damn darling! you gotta lotta money", "$$$$$", "you must drive a lambo"],
    "darling": ["you mean DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARLING", "in the franxx"],
    "hmm": ["I wonder if...", "well...", "okay but...", "no I disagree"],
    "bro": ["yeah?", "let's get drunk", "saturdays are for the boys", "i'm an only child"],
    "ily": ["ily too", "*ily 3000", "ily 6353542"],
    "002": ["what?", "yes?", "that's my name", "is the best", "*speaking*", "no, i am 003"],
    "02": ["yes?", "one sec, i'm on the phone", "hey darling", "03", "the moon landing was faked"],
    "ben fix ur bot": ["i will notify him", "my developer is currently watching anime"],
}


async def respond_to_google(msg):
    msg_content = msg.content.lower()
    if msg_content.startswith("!2 g"):
        print(f"googling / {msg_content}")
        msg_content = msg_content.split("!2 g")
        if len(msg_content) == 2:
            query = msg_content[1]
            response = google_handler.chatbot_query(query)
            await msg.channel.send(response)
            return
        await msg.channel.send("dunno :(")


async def respond_to_name(msg):
    msg_content = msg.content.lower()
    """Send a msg when 02's name is detected"""
    if any(name in msg_content for name in NAMES):
        await send_random(msg, NAMES_RESPONSES, img_dir=IMAGE_DIR)


async def respond_to_certain_things(msg):
    """Send pre-programmed responses to certain messages"""
    msg_content = msg.content.lower()
    if msg_content in THINGS_TO_RESPOND_TO.keys():
        responses = THINGS_TO_RESPOND_TO[msg_content]
        await send_random(msg, responses)


# helpers


async def send_random(msg, responses, img_dir=IMAGE_DIR):
    """Sends a random message from a list, including images"""
    print("send_random")
    metrics_utils.increment_conversation_count()
    random_response = random.choice(responses)
    if is_image(random_response, img_dir):
        img_path = img_dir + random_response
        await msg.channel.send(file=discord.File(img_path))
    elif random_response == ".DS_Store":
        await msg.channel.send("IS I")
    else:
        await msg.channel.send(random_response)
    return


def is_image(filename, img_dir):
    file_path = img_dir + filename
    return file_path[-4:].lower() in IMAGE_FILE_EXTENSIONS \
           and os.path.exists(file_path) and "DS_Store" not in file_path
