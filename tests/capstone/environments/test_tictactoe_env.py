import unittest
from capstone.environment import TicTacToeEnv


class TestTicTacToeEnv(unittest.TestCase):

    def test_states(self):
        pass

    # def test_reward_before_game_is_over(self):
    #     cur_state = TicTacToe()
    #     action = 1
    #     next_state = cur_state.copy().make_move(action)
    #     reward = self.mdp.reward(cur_state, action, next_state)
    #     self.assertEqual(reward, 0)

    # def test_reward_when_game_is_over(self):
    #     cur_state = TicTacToe()
    #     action = 1
    #     next_state = cur_state.copy().make_move(action)
    #     reward = self.mdp.reward(cur_state, action, next_state)
    #     self.assertEqual(reward, 0)

    # def test_reward_when_game_is_over_and_first_player_wins(self):
    #     cur_state = TicTacToe().make_moves([1, 4, 2, 5])
    #     action = 3
    #     next_state = cur_state.copy().make_move(action)
    #     reward = self.mdp.reward(cur_state, action, next_state)
    #     self.assertEqual(reward, 1)
