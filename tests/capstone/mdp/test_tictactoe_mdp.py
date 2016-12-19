import unittest
from capstone.games import TicTacToe
from capstone.mdps import TicTacToeMDP
from capstone.players import RandPlayer
from capstone.util import play_match


class TestTicTacToeMDP(unittest.TestCase):

    mdp = TicTacToeMDP(None)

    def test_states(self):
        self.assertEqual(len(self.mdp.states), 5478)

    def test_actions(self):
        cur_state = TicTacToe()
        actual_actions = list(range(1, 10))
        expected_actions = self.mdp.actions(cur_state)
        self.assertItemsEqual(actual_actions, expected_actions)

    def test_actions_at_end_of_game_are_empty(self):
        game = TicTacToe()
        players = [RandPlayer(), RandPlayer()]
        play_match(game, players, verbose=False)
        actual_n_actions = len(self.mdp.actions(game))
        self.assertEqual(actual_n_actions, 0)

    def test_reward_when_game_is_not_over_is_zero(self):
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
        play_match(game, players, verbose=False)
        self.assertTrue(self.mdp.is_terminal(game))
