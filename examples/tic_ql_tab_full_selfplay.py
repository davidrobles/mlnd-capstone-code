'''
The Q-learning algorithm is used to estimate the state-action values for
all Tic-Tac-Toe position by playing games against itself (self-play).
'''
from capstone.game.games import TicTacToe
from capstone.game.players import RandPlayer
from capstone.game.utils import tic2pdf
from capstone.rl import Environment, GameMDP
from capstone.rl.learners import QLearningSelfPlay
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter, QValuesPlotter
from capstone.rl.value_functions import TabularQ


seed = 23
game = TicTacToe()
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
            filepath='figures/tic_ql_tab_full_selfplay_qvalues_plot.pdf'
        ),
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=2000,
            period=1000,
            filepath='figures/tic_ql_tab_full_selfplay_wld_plot.pdf'
        )
    ]
)

####################
# Generate figures #
####################

tic2pdf('figures/tic_ql_tab_full_selfplay_start_board.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = qlearning.qfunction[(game, move)]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_tab_full_selfplay_move_{}_board.pdf'.format(move)
    tic2pdf(filename, new_game.board)
