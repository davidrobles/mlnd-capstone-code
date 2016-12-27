'''
A Q-Learning algorithm learns the state-action values for Tic-Tac-Toe board
positions against a deterministic Alpha-Beta player. Aftere the values are
learned, we use a Greedy Player to play 100 games against AlphaBeta.

Since Q-learning is a model-free algorithm, i.e. it does not require a model,
it takes environment and it does not have access to the transition and
reward dynamics.

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
from capstone.player import AlphaBeta, GreedyQF
from capstone.util import play_series

board = 'XOXO-O--X'
game = TicTacToe(board)
ab = AlphaBeta()
mdp = GameMDP(game, ab, 1)
env = Environment(mdp)
qf = {}
QLearning(env, qf=qf, n_episodes=1000).learn()
players = [GreedyQF(qf), ab]
play_series(TicTacToe(board), players, n_matches=100)
