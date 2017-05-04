from capstone.game.games import TicTacToe
from capstone.game.utils import tic2pdf
from capstone.rl.learners import MinimaxQ
from capstone.rl.policies import RandomPolicy
from capstone.rl.value_functions import TabularVF
from capstone.rl.mdp import AlternatingMarkovGame
from capstone.rl.interactions import AMGInteraction


board = [[' ', ' ', 'X'],
         [' ', 'X', ' '],
         ['O', 'O', ' ']]
amg = AlternatingMarkovGame(TicTacToe(board))
minimaxq = MinimaxQ(
    action_space=amg.actions,
    qfunction=TabularVF(),
    policy=RandomPolicy(action_space=amg.actions),
    learning_rate=0.1,
    discount_factor=1.0
)
policies = [minimaxq, minimaxq]
AMGInteraction(amg, policies).train(n_episodes=5000)


game = TicTacToe(board)
for move in game.legal_moves():
    print('*' * 80)
    value = minimaxq.qfunction[game, move]
    print('Move: %d' % move)
    print('Value: %f' % value)
    new_game = game.copy().make_move(move)
    print(new_game)
    filename = 'figures/tic_ql_tab_move_{}.pdf'.format(move)
    tic2pdf(filename, new_game.board)
