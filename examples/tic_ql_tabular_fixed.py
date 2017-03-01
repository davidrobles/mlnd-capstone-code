'''
Q-Learning is used to learn the state-action values for a
Tic-Tac-Toe board position against a fixed Alpha-Beta opponent
'''
from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta, RandPlayer
from capstone.game.utils import tic2pdf
from capstone.rl import FixedGameMDP, Environment
from capstone.rl.learners import QLearning
from capstone.rl.policies import RandomPolicy
from capstone.rl.utils import EpisodicWLDPlotter
from capstone.rl.value_functions import TabularQ

seed = 23
board = [['X', ' ', ' '],
         ['O', 'X', ' '],
         [' ', 'O', ' ']]
game = TicTacToe(board)
mdp = FixedGameMDP(game, AlphaBeta(), 1)
env = Environment(mdp)
qlearning = QLearning(
    env=env,
    qfunction=TabularQ(random_state=seed),
    policy=RandomPolicy(env.actions, random_state=seed),
    learning_rate=0.1,
    discount_factor=1.0,
    n_episodes=10000,
)
qlearning.train(
    callbacks=[
        EpisodicWLDPlotter(
            game=game,
            opp_player=RandPlayer(random_state=seed),
            n_matches=100,
            period=100,
            filepath='figures/tic_ql_tabular_fixed.pdf'
        )
    ]
)

####################
# Generate figures #
####################

tic2pdf('figures/tic_ql_current.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    value = qlearning.qfunction[(game, move)]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_move_%d_value_%.4f.pdf' % (move, value)
    tic2pdf(filename, new_game.board)
