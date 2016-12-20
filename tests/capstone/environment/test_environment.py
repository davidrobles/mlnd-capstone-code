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
