import unittest
from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta


class TestEnvironment(unittest.TestCase):

    def test_cur_state(self):
        game = TicTacToe()
        mdp = GameMDP(game, AlphaBeta(), 1)
        env = Environment(mdp)
        self.assertEqual(env.cur_state(), mdp.start_state())
        self.assertEqual(env.cur_state(), game)

    def test_cur_state_when_opponent_should_move_to_start(self):
        game = TicTacToe(
            'XOO'
            'XO-'
            '-XX'
        )
        ab = AlphaBeta()
        mdp = GameMDP(game, ab, 1)
        env = Environment(mdp)
        expected = TicTacToe(
            'XOO'
            'XO-'
            'OXX'
        )
        self.assertEqual(env.cur_state(), expected)

    def test_do_action(self):
        # X - O
        # - - X
        # - - O
        game = TicTacToe().make_moves(1, 3, 6, 9)
        mdp = GameMDP(game.copy(), AlphaBeta(), 1)
        env = Environment(mdp)
        env.do_action(7)
        expected = TicTacToe().make_moves(1, 3, 6, 9, 7, 4)
        self.assertEqual(env.cur_state(), expected)
