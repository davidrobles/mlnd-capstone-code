import unittest
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP


class TestEnvironment(unittest.TestCase):

    def test_cur_state(self):
        game = TicTacToe()
        mdp = GameMDP(game, None, 0)
        env = Environment(mdp)
        self.assertEqual(env.cur_state(), mdp.start_state())
        self.assertEqual(env.cur_state(), game)

    def test_do_action(self):
        game = TicTacToe()
        mdp = GameMDP(game.copy(), None, 0)
        env = Environment(mdp)
        env.do_action(3)
        self.assertEqual(env.cur_state(), game.make_move(3))
