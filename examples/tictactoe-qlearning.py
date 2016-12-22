from capstone.algorithms import QLearning
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta


game = TicTacToe(
    'X-O'
    'XO-'
    '-X-'
)
ab = AlphaBeta()
mdp = GameMDP(game, ab, 0)
env = Environment(mdp)
ql = QLearning(env)
ql.learn()
