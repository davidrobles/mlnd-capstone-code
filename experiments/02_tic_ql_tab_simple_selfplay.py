'''
The Q-learning algorithm is used to estimate the state-action values for a
simple Tic-Tac-Toe position by playing games against itself (self-play).
'''
from capstone.game.games import TicTacToe
from capstone.game.utils import tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearning
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import QValuesPlotter
from capstone.rl.value_functions import TabularVF


seed = 23
board = [[' ', ' ', 'X'],
         [' ', 'X', ' '],
         ['O', 'O', ' ']]
game = TicTacToe(board)
mdp = GameMDP(game)
env = Environment(mdp)
qlearning = QLearning(
    env=env,
    qfunction=TabularVF(random_state=seed),
    policy=RandomPolicy(env.actions, random_state=seed),
    learning_rate=0.1,
    discount_factor=1.0,
    selfplay=True
)
qlearning.train(
    n_episodes=4000,
    callbacks=[
        QValuesPlotter(
            state=game,
            actions=game.legal_moves(),
            filepath='figures/tic_ql_tab_simple_selfplay_progress.pdf'
        )
    ]
)

####################
# Generate figures #
####################

tic2pdf('figures/tic_ql_tab_simple_selfplay_cur.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = qlearning.qfunction[(game, move)]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_tab_simple_selfplay_move_{}.pdf'.format(move)
    tic2pdf(filename, new_game.board)
