from __future__ import unicode_literals
import unittest
from capstone.game import Connect4


class TestConnect4(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_name(self):
        self.assertEqual(Connect4.name, 'Connect4')

#     def test_with_board(self):
#         game = TicTacToe(
#             'X-X'
#             'O-X'
#             '-O-'
#         )
#         self.assertEqual(game.legal_moves(), [2, 5, 7, 9])
#         self.assertEqual(game.cur_player(), 1)

    def test_copy(self):
        self.game.make_moves('a', 'b')
        game_copy = self.game.copy()
        self.assertEqual(game_copy, self.game)
        self.assertIsNot(game_copy, self.game)
        self.assertIsInstance(game_copy, Connect4)
        self.assertIsInstance(game_copy, Connect4)
        self.assertEqual(game_copy.legal_moves(), self.game.legal_moves())
        self.assertIsNot(game_copy.legal_moves(), self.game.legal_moves())

#     def test_hash(self):
#         game1 = TicTacToe().make_moves(1, 7)
#         table = {game1: 'game1'}
#         self.assertEqual(len(table), 1)
#         self.assertEqual(table[game1], 'game1')
#         game2 = TicTacToe().make_moves(1, 7)
#         table[game2] = 'game2'
#         self.assertEqual(table[game1], 'game2')
#         self.assertEqual(table[game2], 'game2')
#         game3 = TicTacToe().make_moves(1, 7, 9)
#         table[game3] = 'game3'
#         self.assertEqual(len(table), 2)
#         self.assertEqual(table[game3], 'game3')

#     def test_not_equal(self):
#         other = TicTacToe().make_moves(1)
#         self.assertNotEqual(self.game, other)

    def test_cur_player_start(self):
        self.assertEqual(self.game.cur_player(), 0)

    def test_cur_player_after_one_move(self):
        self.game.make_move('a')
        self.assertEqual(self.game.cur_player(), 1)

    def test_cur_player_after_two_moves(self):
        self.game.make_moves('a', 'b')
        self.assertEqual(self.game.cur_player(), 0)

    def test_equal(self):
        moves = ['a', 'b']
        self.game.make_moves(*moves)
        other = Connect4().make_moves(*moves)
        self.assertEqual(self.game, other)

    def test_is_not_over_at_start(self):
        self.assertFalse(self.game.is_over())

    def test_is_over_at_end_of_game(self):
        self.game.make_moves('a', 'b', 'a', 'b', 'a', 'b', 'a')
        self.assertTrue(self.game.is_over())

    def test_legal_moves_start(self):
        actual = self.game.legal_moves()
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.assertEqual(actual, expected)

    def test_legal_moves_after_one_move(self):
        self.game.make_move('a')
        actual = self.game.legal_moves()
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.assertEqual(actual, expected)

    def test_legal_moves_after_two_moves(self):
        self.game.make_moves('a', 'a', 'a', 'a', 'a', 'a')
        actual = self.game.legal_moves()
        expected = ['b', 'c', 'd', 'e', 'f', 'g']
        self.assertEqual(actual, expected)

#     def test_legal_moves_are_empty_when_is_over(self):
#         game = TicTacToe(
#             'XXX'
#             'OO-'
#             '---'
#         )
#         self.assertTrue(len(game.legal_moves()) == 0)

    def test_make_move_returns_self(self):
        self.assertIs(self.game.make_move('a'), self.game)

#     def test_make_moves(self):
#         self.game.make_moves(1, 2, 3)
#         actual = self.game.legal_moves()
#         expected = [4, 5, 6, 7, 8, 9]
#         self.assertEqual(actual, expected)

#     def test_make_moves_returns_self(self):
#         self.assertIs(self.game.make_moves(1, 2, 3), self.game)

#     def test_make_moves_returns_self(self):
#         actual = self.game.make_moves(1, 2, 3)
#         expected = self.game
#         self.assertEqual(actual, expected)

#     def test_outcomes_win_first_player(self):
#         game = TicTacToe(
#             'XXX'
#             'OO-'
#             '---'
#         )
#         self.assertEqual(game.outcomes(), ['W', 'L'])

#     def test_outcomes_win_second_player(self):
#         game = TicTacToe(
#             'XX-'
#             'OOO'
#             '--X'
#         )
#         self.assertEqual(game.outcomes(), ['L', 'W'])

#     def test_outcomes_draw(self):
#         game = TicTacToe(
#             'XXO'
#             'OOX'
#             'XOX'
#         )
#         self.assertEqual(game.outcomes(), ['D', 'D'])
