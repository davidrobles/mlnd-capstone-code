from capstone.algorithms import QLearning
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta
from capstone.util import play_series


class PolicyPlayer(object):

    def __init__(self, qf):
        self.qf = qf

    def choose_move(self, game):
        best_value = -100000
        best_move = None
        for move in game.legal_moves():
            if (game, move) not in self.qf:
                continue
            temp_value = self.qf[(game, move)]
            if temp_value > best_value:
                best_value = temp_value
                best_move = move
        if best_move is None:
            return random.choice(game.legal_moves())
        return best_move


game = TicTacToe(
    '---'
    '---'
    '---'
)
ab = AlphaBeta()
mdp = GameMDP(game, ab, 1)
env = Environment(mdp)
qf = {}
ql = QLearning(env, qf=qf, n_episodes=1000)
ql.learn()
players = [PolicyPlayer(qf), AlphaBeta()]
play_series(TicTacToe(), players, 100)
