import random

EMPTY = '⬜'
USER_SYMBOL = '🅾️'
CPU_SYMBOL = '❎'
MAX_MOVES = 9
ROWS = [['↖️', '⬆️', '↗️'], ['⬅️', '⚫', '➡️'], ['↙️', '⬇️', '↘️']]
COLS = [['↖️', '⬅️', '↙️'], ['⬆️', '⚫', '⬇️'], ['↗️', '➡️', '↘️']]
DIAGS = [['↖️', '⚫', '↘️'], ['↙️', '⚫', '↗️']]
WINNING_PATTERNS = ROWS + COLS + DIAGS


class TicTacToe:
    moves = 0

    def __init__(self):
        self.board = {
            '↖️': EMPTY, '⬆️': EMPTY, '↗️': EMPTY,
            '⬅️': EMPTY, '⚫': EMPTY, '➡️': EMPTY,
            '↙️': EMPTY, '⬇️': EMPTY, '↘️': EMPTY}

    def __str__(self):
        """String representation of this object is the board."""
        b = self.board
        top = f"{b['↖️']}{b['⬆️']}{b['↗️']}"
        middle = f"{b['⬅️']}{b['⚫']}{b['➡️']}"
        bottom = f"{b['↙️']}{b['⬇️']}{b['↘️']}"
        # use below if a TicTacToe object is printed.
        board_str = "Here's the board:" + "\n" + top + '\n' + middle + "\n" + bottom
        return board_str

    def update_board(self, user_move):
        """Apply user's move and cpu's move."""
        if user_move:
            self.apply_move(symbol=USER_SYMBOL, position=user_move)
        try:
            self.apply_move(symbol=CPU_SYMBOL, position=random.choice([sq for sq in self.board if self.board[sq] == EMPTY]))
        except IndexError:
            print("board full")

    def apply_move(self, symbol, position=None):
        """Apply a move onto the board."""
        if not self.is_over() and self.board[position] == EMPTY:
            self.board[position] = symbol
            self.moves += 1

    def is_position_empty(self, position):
        """Check that the position is EMPTY."""
        return position in self.board and self.board[position] == EMPTY

    def is_over(self):
        """Return GAME OVER if max-moves is reached."""
        # are all the spaces occupied?
        if self.moves >= MAX_MOVES:
            return True
        # did someone win?
        for seq in WINNING_PATTERNS:
            seq = [self.board[pos] for pos in seq]
            if len(set(seq)) == 1 and seq[0] != EMPTY:
                return True
        return False



