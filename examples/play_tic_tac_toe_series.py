import random
import sys
sys.path.insert(0, '/home/drobles/projects/mlnd-capstone-code/src/')
from tictactoe import TicTacToe
from utils import play_random_game, play_series


class RandPlayer(object):

    def chooseMove(self, game):
        return random.choice(game.legal_moves())


players = [RandPlayer(), RandPlayer()]
game = TicTacToe()
play_series(game, players)
