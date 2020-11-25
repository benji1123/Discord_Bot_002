import random
import metrics_utils

ROCK = '🤘'
PAPER = '📝'
SCISSORS = '✂️'

USER_LOSS = 0
DRAW = 1
USER_WIN = 2


class RockPaperScissors:
    moves = {
        ROCK: [PAPER, ROCK, SCISSORS],
        PAPER: [SCISSORS, PAPER, ROCK],
        SCISSORS: [ROCK, SCISSORS, PAPER]
    }

    def simulate_game(self, user_choice):
        metrics_utils.increment_rps_count()
        cpu_choice = random.choice(list(self.moves))
        outcome = self.get_outcome(user_choice, cpu_choice)
        return outcome, cpu_choice

    def get_outcome(self, user_choice, cpu_choice):
        outcomes = self.moves[user_choice]
        if cpu_choice == outcomes[USER_WIN]:
            return 'WIN'
        elif cpu_choice == outcomes[DRAW]:
            return 'DRAW'
        return 'LOSS'
