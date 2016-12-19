import unittest
from capstone.games import TicTacToe
from capstone.mdps import TicTacToeMDP
from capstone.players import RandPlayer
from capstone.util import play_match


class TestTicTacToeMDP(unittest.TestCase):

    mdp = TicTacToeMDP(None)

    def setUp(self):
        pass

    def test_states(self):
        self.assertEqual(len(self.mdp.states), 5478)

    def test_reward_before_game_is_over(self):
        cur_state = TicTacToe()
        action = 1
        next_state = cur_state.copy().make_move(action)
        reward = self.mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 0)

    def test_reward_when_game_is_over(self):
        cur_state = TicTacToe()
        action = 1
        next_state = cur_state.copy().make_move(action)
        reward = self.mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 0)

    def test_reward_when_game_is_over_and_first_player_wins(self):
        cur_state = TicTacToe().make_moves(1, 4, 2, 5)
        action = 3
        next_state = cur_state.copy().make_move(action)
        reward = self.mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 1)

    def test_non_terminal_state(self):
        game = TicTacToe().make_moves(1, 2)
        self.assertFalse(self.mdp.is_terminal(game))

    def test_terminal_state(self):
        game = TicTacToe()
        players = [RandPlayer(), RandPlayer()]
        play_match(game, players)
        self.assertTrue(self.mdp.is_terminal(game))
