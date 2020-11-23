import random
import os
import discord
import google_handler
import metrics_utils

IMAGE_FILE_EXTENSIONS = [".jpg", ".png", ".gif"]

NAMES = [" 002", " 02", "002 ", "02 ", "darling", "dino", "dinosaur", "waifu", "zerotwo", "o2", "oxygen", "003"]
NAMES_RESPONSES = os.listdir('zerotwo/')
IMAGE_DIR = "zerotwo/"

THINGS_TO_RESPOND_TO = {
    "rpg miniboss @here": ["fight", "please accept my moral support", "we shall win"],
    "rpg arena @everyone": ["join", "moral support", "we cannot lose"],
    "stfu": ["don't be mean, darling!", "that hurts", "after ypu suck my d*ck"],
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
    "!np": ["i think... i like this song", "this song sucks", "listed to Kiss of Death"],
    "rpg buy edgy lootbox": ["damn darling! you gotta lotta money", "$$$$$", "you must drive a lambo"],
    "darling": ["you mean DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARLING", "in the franxx"],
    "hmm": ["I wonder if...", "well...", "okay but...", "no I disagree"],
    "bro": ["yeah?", "let's get drunk", "saturdays are for the boys", "i'm an only child"],
    "ily": ["ily too", "*ily 3000", "ily 6353542"],
    "002": ["what?", "yes?", "that's my name", "is the best", "*speaking*", "no, i am 003", "i love ben"],
    "02": ["yes?", "one sec, i'm on the phone", "hey darling", "03", "the moon landing was faked"],
    "ben fix ur bot": ["i will notify him", "my developer is currently watching anime"],
}


async def respond_to_google(message, msg_content):
    if msg_content.startswith("!2 g"):
        print(f"googling / {msg_content}")
        msg_content = msg_content.split("!2 g")
        if len(msg_content) == 2:
            query = msg_content[1]
            response = google_handler.chatbot_query(query)
            await message.channel.send(response)
            return
        await message.channel.send("dunno :(")

async def respond_to_name(message, msg_content):
    """Send a msg when 02's name is detected"""
    if any(name in msg_content for name in NAMES):
        await send_random(message, NAMES_RESPONSES, img_dir="zerotwo/")


async def respond_to_certain_things(message, msg_content):
    """Send pre-programmed responses to certain messages"""
    if msg_content in THINGS_TO_RESPOND_TO.keys():
        responses = THINGS_TO_RESPOND_TO[msg_content]
        await send_random(message, responses)


async def respond_to_math(message, msg_content):
    if msg_content.startswith("!2 math"):
        if len(msg_content) == 2:
            eqn = msg_content[1]
            ans = eval(eqn)
            await message.channel.send(f"too easy bruh, {eqn} = {ans}")
    ValueError("bad message for !2 math")


# helpers


async def send_random(message, responses, img_dir=""):
    """Sends a random message from a list, including images"""
    metrics_utils.increment_conversation_count()
    print("send_random")
    response = random.choice(responses)
    img_name = img_dir + response
    if is_image(img_name):
        await message.channel.send(file=discord.File(img_name))
    elif response == ".DS_Store":
        await message.channel.send("asjhdsakdbsjnsacsadasdcnsbcjhasjdsa it is i adasdasdsadasdasdsada")
    else:
        await message.channel.send(response)
    return


def is_image(path):
    return path[-4:].lower() in IMAGE_FILE_EXTENSIONS \
           and os.path.exists(path) and "DS_Store" not in path
