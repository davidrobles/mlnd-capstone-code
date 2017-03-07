'''
The Q-learning algorithm is used to estimate the state-action values for a
simple Connect 4 position by playing games against itself (self-play).
'''
from capstone.game.games import Connect4
from capstone.game.players import RandPlayer
from capstone.game.utils import c42pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter, QValuesPlotter
from capstone.rl.value_functions import TabularQ


seed = 23
board = [['X', 'O', 'O', ' ', 'O', ' ', ' '],
         ['X', 'O', 'X', ' ', 'X', ' ', ' '],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
game = Connect4(board)
mdp = GameMDP(game)
env = Environment(mdp)
qlearning = QLearningSelfPlay(
    env=env,
    qfunction=TabularQ(random_state=seed),
    policy=RandomPolicy(env.actions, random_state=seed),
    learning_rate=0.1,
    discount_factor=1.0,
    n_episodes=4000,
)
qlearning.train(
    callbacks=[
        QValuesPlotter(
            state=game,
            actions=game.legal_moves(),
            filepath='figures/c4_ql_tab_simple_selfplay_progress.pdf'
        )
    ]
)

####################
# Generate figures #
####################

c42pdf('figures/c4_ql_tab_simple_selfplay_cur.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = qlearning.qfunction[(game, move)]
    print('Move: {}'.format(move))
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/c4_ql_tab_simple_selfplay_move_{}.pdf'.format(move)
    c42pdf(filename, new_game.board)
