'''
Sarsa via self-play is used to learn the state-action values, Q(s, a),
for the legal moves of a Connect 4 position.
'''

from capstone.game import Connect4
from capstone.mdp import GameMDP
from capstone.rl import Environment, Sarsa
from capstone.utils import c42pdf

board = [['X', 'O', 'O', ' ', 'O', ' ', ' '],
         ['X', 'O', 'X', ' ', 'X', ' ', ' '],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
game = Connect4(board)
mdp = GameMDP(game)
env = Environment(mdp)
sarsa = Sarsa(env, n_episodes=1000, random_state=0)
sarsa.learn()
c42pdf('figures/c4_sarsa_tabular_selfplay_current.pdf', game.board)
print(game)

for move in game.legal_moves():
    print('*' * 80)
    value = sarsa.qf[(game, move)]
    print('Move: %s' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/c4_sarsa_tabular_selfplay_move_%s_value_%.4f.pdf' % (move, value)
    c42pdf(filename, new_game.board)
