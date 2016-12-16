import unittest
from games import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_copy(self):
        self.game.make_moves([1, 3, 2])
        clone = self.game.copy()
        self.assertItemsEqual(self.game.legal_moves(), clone.legal_moves())
        self.assertEqual(self.game.cur_player, clone.cur_player)
        self.assertEqual(self.game, clone)

    def test_cur_player_start(self):
        self.assertEqual(self.game.cur_player, 0)

    def test_cur_player_after_one_move(self):
        self.game.make_move(3)
        self.assertEqual(self.game.cur_player, 1)

    def test_cur_player_after_two_moves(self):
        self.game.make_moves([3, 7])
        self.assertEqual(self.game.cur_player, 0)

    def test_is_not_over_at_start(self):
        self.assertFalse(self.game.is_over())

    def test_is_over_at_end_of_game(self):
        self.game.make_moves([1, 4, 2, 5, 3])
        self.assertTrue(self.game.is_over())

    def test_legal_moves_start(self):
        actual = self.game.legal_moves()
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertItemsEqual(actual, expected)

    def test_legal_moves_after_one_move(self):
        self.game.make_move(1)
        actual = self.game.legal_moves()
        expected = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertItemsEqual(actual, expected)

    def test_legal_moves_after_two_moves(self):
        self.game.make_moves([3, 7])
        actual = self.game.legal_moves()
        expected = [1, 2, 4, 5, 6, 8, 9]
        self.assertItemsEqual(actual, expected)

    def test_legal_moves_are_empty_when_is_over(self):
        self.game.make_moves([1, 4, 2, 5, 3])
        self.assertTrue(len(self.game.legal_moves()) == 0)

    def test_make_move_returns_self(self):
        self.assertIs(self.game.make_move(1), self.game)

    def test_make_moves(self):
        self.game.make_moves([1, 2, 3])
        actual = self.game.legal_moves()
        expected = [4, 5, 6, 7, 8, 9]
        self.assertItemsEqual(actual, expected)

    def test_make_moves_returns_self(self):
        actual = self.game.make_moves([1, 2, 3])
        expected = self.game
        self.assertEquals(actual, expected)

    def test_name(self):
        self.assertEqual(TicTacToe.name, 'Tic Tac Toe')

    def test_outcomes_win_first_player(self):
        self.game.make_moves([1, 4, 2, 5, 3])
        self.assertItemsEqual(self.game.outcomes(), ['W', 'L'])

    def test_outcomes_win_second_player(self):
        self.game.make_moves([1, 4, 2, 5, 9, 6])
        self.assertItemsEqual(self.game.outcomes(), ['L', 'W'])

    def test_outcomes_draw(self):
        self.game.make_moves([1, 3, 2, 4, 6, 5, 7, 8, 9])
        self.assertItemsEqual(self.game.outcomes(), ['D', 'D'])
