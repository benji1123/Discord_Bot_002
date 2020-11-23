from games.RockPaperScissors import RockPaperScissors

from asyncio import TimeoutError


async def create_rps_game(client, msg):
    msg_content = msg.content
    if msg_content == "!2 rps":
        await start_rps_game(client, channel=msg.channel, user=msg.author)


async def start_rps_game(client, channel, user):
    game = RockPaperScissors()
    game_msg = await channel.send('10 seconds to choose, darling')
    for react in game.moves:
        await game_msg.add_reaction(react)
    await run_rps_game(client, channel, user, game)


async def run_rps_game(client, channel, user, game):
    try:
        user_reaction, user = await client.wait_for(
            'reaction_add',
            timeout=40.0,
            check=lambda r, u: str(r.emoji) in game.moves and u == user
        )
    except TimeoutError:
        await channel.send('too slow darling -_-')
    else:
        res, cpu_choice = game.simulate_game(user_choice=str(user_reaction.emoji))
        await channel.send(res + " I chose: " + cpu_choice)
