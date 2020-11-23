from asyncio import TimeoutError
from games.TicTacToe import TicTacToe
import metrics_utils

ROUND_TIME_LIMIT = 40.0
TOO_SLOW_MESSAGE = "too slow darling -_-"
GAME_OVER_MESSAGE = "GAME OVER"


async def create_ttt_game(client, msg):
    msg_content = msg.content
    if msg_content == '!2 tt':
        await start_ttt_game(client, channel=msg.channel, user=msg.author)


async def start_ttt_game(client, channel, user):
    game = TicTacToe()
    empty_board = str(game)
    game_msg = await channel.send(empty_board)
    reactions = game.board.keys()
    for r in reactions:
        await game_msg.add_reaction(r)
    await enter_game_loop(client, channel, user, game, game_msg)


async def enter_game_loop(client, channel, user, game, game_msg):
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
        await update_game_message(client, channel, user, user_reaction, game, game_msg)


async def update_game_message(client, channel, user, user_reaction, game, game_msg):
    """Update the original game-message with the new board."""
    user_move = str(user_reaction.emoji)
    game.update_board(user_move=user_move)
    await game_msg.edit(content=str(game))
    if not game.is_over():
        await enter_game_loop(client, channel, user, game, game_msg)
    else:
        metrics_utils.increment_tictactoe_count()
        print("gg tt")
        await channel.send(GAME_OVER_MESSAGE)
