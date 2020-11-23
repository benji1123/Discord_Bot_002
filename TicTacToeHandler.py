from asyncio import TimeoutError
from TicTacToe import TicTacToe
import metrics_utils

ROUND_TIME_LIMIT = 40.0
TOO_SLOW_MESSAGE = "too slow darling -_-"
GAME_OVER_MESSAGE = "GAME OVER"


async def start_game(client, channel, user):
    game = TicTacToe()
    # user will play the game through a message and its discord-reacts.
    empty_board = str(game)
    game_message = await channel.send(empty_board)
    for square in game.board:
        await game_message.add_reaction(square)
    # start game loop
    await get_user_reaction(client, channel, user, game, game_message)


async def get_user_reaction(client, channel, user, game, game_message):
    # user must react within time limit.
    try:
        user_reaction, user = await client.wait_for(
            'reaction_add',
            timeout=ROUND_TIME_LIMIT,
            check=lambda r, u: game.is_position_empty(str(r.emoji)) and u == user)
    # user took too long
    except TimeoutError:
        await channel.send(TOO_SLOW_MESSAGE)
    # user chose a react in time
    else:
        await update_game_message(client, channel, user, user_reaction, game, game_message)


async def update_game_message(client, channel, user, user_reaction, game, game_message):
    """Update the original game-message with the new board."""
    user_move = str(user_reaction.emoji)
    game.update_board(user_move=user_move)
    await game_message.edit(content=str(game))
    if not game.is_over():
        await get_user_reaction(client, channel, user, game, game_message)
    else:
        metrics_utils.increment_tictactoe_count()
        print("gg tt")
        await channel.send(GAME_OVER_MESSAGE)

