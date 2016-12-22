'''
A Q-Learning algorithm learns the state-action values for Tic-Tac-Toe board
positions against a deterministic Alpha-Beta player. Aftere the values are
learned, we use a Greedy Player to play 100 games against AlphaBeta.

A greedy player that uses the learned state-action values should always
draw against Alpha-Beta assuming the Q-learning algorithm ran for a high
number of episodes.

Note that Q-learning runs to only learn the values for board-moves for
the first player. If we want to learn this to play as the second player,
we need to run the algorithm against using an MDP where opp_idx = 0.
'''
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


game = TicTacToe()
ab = AlphaBeta()
mdp = GameMDP(game, ab, 1)
env = Environment(mdp)
qf = {}
QLearning(env, qf=qf, n_episodes=1000).learn()
players = [PolicyPlayer(qf), ab]
play_series(TicTacToe(), players, 100)
