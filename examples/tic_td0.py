from capstone.game.games import TicTacToe
from capstone.game.players import AlphaBeta, RandPlayer
from capstone.game.utils import tic2pdf
from capstone.rl import GameMDP, Environment
from capstone.rl.learners import TabularTD0
from capstone.rl.policies import RandomPolicy
from capstone.rl.policy import Policy
from capstone.rl.utils import Callback
from capstone.rl.value_functions import TabularV

seed = 23
board = [[' ', ' ', 'X'],
         [' ', 'X', ' '],
         ['O', 'O', ' ']]
game = TicTacToe(board)
# mdp = FixedGameMDP(game, AlphaBeta(), 1)
mdp = GameMDP(game)
env = Environment(mdp)


class MyPolicy(Policy):

    def __init__(self, action_space):
        self._action_space = action_space

    ##########
    # Policy #
    ##########

    def action(self, state):
        if state.cur_player() == 0:
            return RandomPolicy(self._action_space).action(state)
        return RandomPolicy(self._action_space).action(state)
        # return AlphaBeta().choose_move(state)


td0 = TabularTD0(
    env=env,
    vfunction=TabularV(),
    policy=MyPolicy(env.actions),
    learning_rate=0.1,
    discount_factor=1.0
)

class Monitor(Callback):

    def on_episode_begin(self, episode, vfunction):
        if episode % 50 == 0:
            print('Episode {}'.format(episode))


td0.train(
    n_episodes=1000,
    callbacks=[Monitor()]
)



####################
# Generate figures #
####################

# tic2pdf('figures/tic_ql_tab_current.pdf', game.board)

for move in game.legal_moves():
    print('*' * 80)
    new_game = game.copy().make_move(move)
    value = td0.vfunction[new_game]
    # print('Move: %d' % move)
    print('Value: %f' % value)
    # new_game = game.copy().make_move(move)
    new_game.print_summary()
    # filename = 'figures/tic_ql_tab_move_{}.pdf'.format(move)
    # tic2pdf(filename, new_game.board)
