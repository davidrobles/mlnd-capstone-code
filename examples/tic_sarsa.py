'''
A SARSA Q-Learning algorithm learns the state-action values for Tic-Tac-Toe board
positions against a deterministic Alpha-Beta player. After the values are
learned, we use a Greedy Player to play 100 games against AlphaBeta.
'''

from capstone.algorithms import Sarsa
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta, GreedyQF
from capstone.util import play_series

board = 'XOXO-O--X'
game = TicTacToe(board)
ab = AlphaBeta()
mdp = GameMDP(game, ab, 1)
env = Environment(mdp)
qf = {}
Sarsa(env, qf=qf, n_episodes=1000).learn()
players = [GreedyQF(qf), ab]
play_series(TicTacToe(board), players, n_matches=100)
