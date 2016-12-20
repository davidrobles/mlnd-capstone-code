import unittest
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta, RandPlayer
from capstone.util import play_match


class TestGameMDP(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.mdp = GameMDP(self.game, None, 0)

    # def test_states(self):
    #     self.assertEqual(len(self.mdp.states()), 5478)

    def test_actions(self):
        cur_state = TicTacToe()
        actual_actions = list(range(1, 10))
        expected_actions = self.mdp.actions(cur_state)
        self.assertEqual(actual_actions, expected_actions)

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

    def test_reward_when_game_is_over_and_is_draw(self):
        cur_state = TicTacToe().make_moves(1, 3, 2, 4, 6, 5, 7, 8)
        action = 9
        next_state = cur_state.copy().make_move(action)
        reward = self.mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 0.0)

    def test_reward_when_agent_moves_first_and_wins(self):
        ab = AlphaBeta()
        mdp = GameMDP(self.game, ab, 1)
        cur_state = TicTacToe().make_moves(1, 4, 2, 5)
        action = 3
        next_state = cur_state.copy().make_move(action)
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 1.0)

    def test_reward_when_agent_moves_first_and_losses(self):
        ab = AlphaBeta()
        mdp = GameMDP(self.game, ab, 1)
        cur_state = TicTacToe().make_moves(1, 4, 2, 5, 7)
        action = 6
        next_state = cur_state.copy().make_move(action)
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, -1.0)

    def test_reward_when_agent_moves_second_and_wins(self):
        ab = AlphaBeta()
        mdp = GameMDP(self.game, ab, 0)
        cur_state = TicTacToe().make_moves(1, 4, 2, 5, 7)
        action = 6
        next_state = cur_state.copy().make_move(action)
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 1.0)

    def test_reward_when_agent_moves_second_and_losses(self):
        ab = AlphaBeta()
        mdp = GameMDP(self.game, ab, 0)
        cur_state = TicTacToe().make_moves(1, 4, 2, 5)
        action = 3
        next_state = cur_state.copy().make_move(action)
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, -1.0)

    def test_non_terminal_state(self):
        game = TicTacToe().make_moves(1, 2)
        self.assertFalse(self.mdp.is_terminal(game))

    def test_terminal_state(self):
        game = TicTacToe()
        players = [RandPlayer(), RandPlayer()]
        play_match(game, players, verbose=False)
        self.assertTrue(self.mdp.is_terminal(game))

    def test_transitions(self):
        # X - O
        # - - X
        # - - O
        game = TicTacToe().make_moves(1, 3, 6, 9)
        # Create an mdp where AlphaBeta is the
        # second player to move
        mdp = GameMDP(game, AlphaBeta(), 1)
        # Put X in 7 slot, and the mdp should
        # make the transition assuming O moving 4
        transitions = mdp.transitions(game, 7)
        self.assertEqual(len(transitions), 1)
        next_game, prob = transitions[0]
        self.assertEqual(game.copy().make_moves(7, 4), next_game)
        self.assertEqual(prob, 1.0)

    def test_transitions_empty_when_game_is_over(self):
        players = [RandPlayer(), RandPlayer()]
        play_match(self.game, players, verbose=False)
        self.assertEqual(self.mdp.transitions(self.game, None), {})
