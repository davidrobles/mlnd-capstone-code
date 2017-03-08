'''
Q-Learning is used to estimate the state-action values for all
Tic-Tac-Toe positions against a Random opponent.
'''
from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta, RandPlayer
from capstone.game.utils import tic2pdf
from capstone.rl import FixedGameMDP, Environment
from capstone.rl.learners import QLearning
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter, QValuesPlotter
from capstone.rl.value_functions import TabularQ

seed = 23
game = TicTacToe()
mdp = FixedGameMDP(game, RandPlayer(random_state=seed), 1)
env = Environment(mdp)
qlearning = QLearning(
    env=env,
    qfunction=TabularQ(random_state=seed),
    policy=RandomPolicy(env.actions, random_state=seed),
    learning_rate=0.1,
    discount_factor=1.0,
    n_episodes=65000
)
qlearning.train(
    callbacks=[
        QValuesPlotter(
            state=game,
            actions=game.legal_moves(),
            period=100,
            filepath='figures/tic_ql_tab_full_qvalues_plot.pdf'
        ),
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=1000,
            period=1000,
            filepath='figures/tic_ql_tab_full_wld_plot.pdf'
        )
    ]
)

####################
# Generate figures #
####################

tic2pdf('figures/tic_ql_tab_full_start_board.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = qlearning.qfunction[(game, move)]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_tab_full_move_{}_board.pdf'.format(move)
    tic2pdf(filename, new_game.board)
