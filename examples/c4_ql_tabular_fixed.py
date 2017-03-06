'''
Q-Learning is used to estimate the state-action values for a
Connect 4 board position against a fixed Alpha-Beta opponent.
'''
from capstone.game.games import Connect4
from capstone.game.players import AlphaBeta
from capstone.game.utils import c42pdf
from capstone.rl import FixedGameMDP, Environment
from capstone.rl.learners import QLearning
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import QValuesPlotter
from capstone.rl.value_functions import TabularQ

seed = 23
board = [['X', 'O', 'O', ' ', 'O', ' ', ' '],
         ['X', 'O', 'X', ' ', 'X', ' ', ' '],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
game = Connect4(board)
mdp = FixedGameMDP(game, AlphaBeta(), 1)
env = Environment(mdp)
qlearning = QLearning(
    env=env,
    qfunction=TabularQ(random_state=seed),
    policy=RandomPolicy(env.actions, random_state=seed),
    learning_rate=0.1,
    discount_factor=1.0,
    n_episodes=1000
)
qlearning.train(
    callbacks=[
        QValuesPlotter(
            game=game,
            actions=game.legal_moves(),
            filepath='figures/c4_ql_tab_qvalues.pdf'
        )
    ]
)

####################
# Generate figures #
####################

c42pdf('figures/c4_ql_tab_current.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = qlearning.qfunction[(game, move)]
    print('Move: %s' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/c4_ql_tab_move_{}.pdf'.format(move)
    c42pdf(filename, new_game.board)
