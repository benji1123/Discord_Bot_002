import random
import asyncio
import metrics_utils

ROCK = '🤘'
PAPER = '📝'
SCISSORS = '✂️'
RPS_MOVES = [ROCK, PAPER, SCISSORS]

GAME_RULES = {
    ROCK: [PAPER, ROCK, SCISSORS],
    PAPER: [SCISSORS, PAPER, ROCK],
    SCISSORS: [ROCK, SCISSORS, PAPER]
}


async def play_rps(client, message, msg_content):
    if msg_content == '!2 rps':
        channel = message.channel
        game_msg = await channel.send('10 seconds to choose, darling')
        # add reacts to msg_content
        for move in RPS_MOVES:
            await game_msg.add_reaction(move)
        # await user response
        try:
            reaction, user = await client.wait_for(
                'reaction_add',
                timeout=20.0,
                check=lambda r, u: str(r.emoji) in RPS_MOVES and u == message.author
            )
        except asyncio.TimeoutError:
            await channel.send('too slow darling -_-')
        else:
            res, cpu_choice = simulate_game(user_choice=str(reaction.emoji))
            await channel.send(res + " I chose: " + cpu_choice)


def simulate_game(user_choice):
    metrics_utils.increment_rps_count()
    cpu_choice = random.choice(RPS_MOVES)

    if cpu_choice == GAME_RULES[user_choice][0]:
        return 'LOSS', cpu_choice
    elif cpu_choice == GAME_RULES[user_choice][1]:
        return 'DRAW', cpu_choice
    else:
        return 'WIN', cpu_choice

