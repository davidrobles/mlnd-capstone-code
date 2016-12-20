import unittest
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta


class TestEnvironment(unittest.TestCase):

    def test_cur_state(self):
        game = TicTacToe()
        mdp = GameMDP(game, None, 0)
        env = Environment(mdp)
        self.assertEqual(env.cur_state(), mdp.start_state())
        self.assertEqual(env.cur_state(), game)

    # def test_do_action(self):
    #     # X - O
    #     # - - X
    #     # - - O
    #     game = TicTacToe().make_moves(1, 3, 6, 9)
    #     mdp = GameMDP(game.copy(), AlphaBeta(), 1)
    #     env = Environment(mdp)
    #     env.do_action(7)
    #     print(env.cur_state())
    #     # expected = TicTacToe().make_moves(1, 3, 6, 9, 7, 4)
    #     # self.assertEqual(env.cur_state(), expected)
