import unittest
from capstone.game import TicTacToe
from capstone.mdp import FixedGameMDP
from capstone.player import AlphaBeta, RandPlayer
from capstone.utils import play_match


class TestGameMDP(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.mdp = FixedGameMDP(self.game, AlphaBeta(), 1)
        self.players = [RandPlayer(), RandPlayer()]

    # def test_states(self):
    #     self.assertEqual(len(self.mdp.states()), 5478)

    def test_start_state_when_opponent_is_next_to_move(self):
        game = TicTacToe(
            [['X', 'O', 'O'],
             ['X', 'O', ' '],
             [' ', 'X', 'X']]
        )
        ab = AlphaBeta()
        mdp = FixedGameMDP(game, ab, 1)
        expected = TicTacToe(
            [['X', 'O', 'O'],
             ['X', 'O', ' '],
             ['O', 'X', 'X']]
        )
        self.assertEqual(mdp.start_state(), expected)

    def test_actions(self):
        self.assertEqual(self.mdp.actions(self.game), list(range(1, 10)))

    def test_actions_at_end_of_game_are_empty(self):
        play_match(self.game, self.players, verbose=False)
        self.assertEqual(self.mdp.actions(self.game), [])

    def test_reward_when_game_is_not_over_is_zero(self):
        cur_state = self.game
        action = 1
        next_state = cur_state.copy().make_move(action)
        reward = self.mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 0)

    def test_reward_when_game_is_over_and_is_draw(self):
        cur_state = TicTacToe().make_moves([1, 3, 2, 4, 6, 5, 7, 8])
        # cur_state:
        # X X O
        # O O X
        # X O -
        action = 9
        next_state = cur_state.copy().make_move(action)
        # next_state:
        # X X O
        # O O X
        # X O X
        reward = self.mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 0.0)

    def test_reward_when_agent_moves_first_and_wins(self):
        ab = AlphaBeta()
        opp_idx = 1
        mdp = FixedGameMDP(self.game, ab, opp_idx)
        # Agent moves first, Opponent second
        cur_state = TicTacToe().make_moves([1, 4, 2, 5])
        # cur_state:
        # X X -
        # O O -
        # - - -
        action = 3
        next_state = cur_state.copy().make_move(action)
        # next_state:
        # X X X
        # O O -
        # - - -
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 1.0)

    def test_reward_when_agent_moves_first_and_losses(self):
        ab = AlphaBeta()
        opp_idx = 1
        mdp = FixedGameMDP(self.game, ab, opp_idx)
        # Opponent moves first, Agent second
        cur_state = TicTacToe().make_moves([1, 4, 2, 5, 7])
        # cur_state:
        # X X -
        # O O -
        # X - -
        action = 6
        next_state = cur_state.copy().make_move(action)
        # next_state:
        # X X -
        # O O O
        # X - -
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, -1.0)

    def test_reward_when_agent_moves_second_and_wins(self):
        ab = AlphaBeta()
        opp_idx = 0
        mdp = FixedGameMDP(self.game, ab, opp_idx)
        # Opponent moves first, Agent second
        cur_state = TicTacToe().make_moves([1, 4, 2, 5, 7])
        # cur_state:
        # X X -
        # O O -
        # X - -
        action = 6
        next_state = cur_state.copy().make_move(action)
        # next_state:
        # X X -
        # O O O
        # X - -
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, 1.0)

    def test_reward_when_agent_moves_second_and_losses(self):
        ab = AlphaBeta()
        opp_idx = 0
        mdp = FixedGameMDP(self.game, ab, opp_idx)
        cur_state = TicTacToe().make_moves([1, 4, 2, 5])
        # cur_state:
        # X X -
        # O O -
        # - - -
        action = 3
        next_state = cur_state.copy().make_move(action)
        # next_state:
        # X X X
        # O O -
        # - - -
        reward = mdp.reward(cur_state, action, next_state)
        self.assertEqual(reward, -1.0)

    def test_start_state(self):
        self.assertEqual(self.mdp.start_state(), self.game)

    def test_terminal_state(self):
        play_match(self.game, self.players, verbose=False)
        self.assertTrue(self.mdp.is_terminal(self.game))

    def test_non_terminal_state(self):
        self.game.make_move(1)
        self.assertFalse(self.mdp.is_terminal(self.game))

    def test_transitions(self):
        # X - O
        # - - X
        # - - O
        game = TicTacToe().make_moves([1, 3, 6, 9])
        # Create an mdp where AlphaBeta is the
        # second player to move
        mdp = FixedGameMDP(game, AlphaBeta(), 1)
        # Put X in 7 slot, and the mdp should
        # make the transition assuming O moving 4
        transitions = mdp.transitions(game, 7)
        self.assertEqual(len(transitions), 1)
        next_game, prob = transitions[0]
        self.assertEqual(next_game, game.copy().make_moves([7, 4]))
        self.assertEqual(prob, 1.0)

    def test_transitions_empty_when_game_is_over(self):
        play_match(self.game, self.players, verbose=False)
        self.assertEqual(self.mdp.actions(self.game), [])
        self.assertEqual(self.mdp.transitions(self.game, None), [])
