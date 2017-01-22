from __future__ import unicode_literals
import unittest
from capstone.game import Connect4


class TestConnect4(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_name(self):
        self.assertEqual(Connect4.name, 'Connect4')

    def test_init_with_board(self):
        game = Connect4(
            [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', 'O', ' ', ' ', ' '],
             ['X', 'O', 'X', 'O', 'O', ' ', ' ']]
        )
        b = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', 'O', ' ', ' ', ' '],
             ['X', 'O', 'X', 'O', 'O', ' ', ' ']]
        self.assertEqual(game.board, b)
        # self.assertTrue(game.is_over())
        # self.assertTrue(game._is_win(game._boards[0]))
        # self.assertFalse(game._is_win(game._boards[1]))
        # self.assertEqual(game._height, [1, 8, 18, 23, 29, 35, 42])
        # self.assertEqual(game.legal_moves(), [])


    def test_init_with_mdlist_board_that_is_over(self):
        game = Connect4(
            [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', 'O', ' ', ' ', ' '],
             ['X', 'O', 'X', 'O', 'O', ' ', ' ']]
        )
        self.assertTrue(game.is_over())
        self.assertTrue(game._is_win(game._boards[0]))
        self.assertFalse(game._is_win(game._boards[1]))
        self.assertEqual(game._height, [1, 8, 18, 23, 29, 35, 42])
        self.assertEqual(game.legal_moves(), [])

    def test_init_with_board_that_is_over(self):
        game = Connect4(
            [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', ' ', ' ', ' ', ' '],
             [' ', ' ', 'X', 'O', ' ', ' ', ' '],
             ['X', 'O', 'X', 'O', 'O', ' ', ' ']]
        )
        self.assertTrue(game.is_over())
        self.assertTrue(game._is_win(game._boards[0]))
        self.assertFalse(game._is_win(game._boards[1]))
        self.assertEqual(game._height, [1, 8, 18, 23, 29, 35, 42])
        self.assertEqual(game.legal_moves(), [])

    def test_init_with_board_that_is_not_over_1(self):
        game = Connect4(
            [['O', ' ', ' ', ' ', ' ', ' ', ' '],
             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
             ['X', ' ', ' ', ' ', ' ', ' ', ' '],
             ['O', ' ', ' ', ' ', ' ', ' ', ' '],
             ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        )
        self.assertFalse(game.is_over())
        self.assertFalse(game._is_win(game._boards[0]))
        self.assertFalse(game._is_win(game._boards[1]))
        self.assertEqual(game.cur_player(), 0)
        self.assertEqual(game._height, [6, 7, 14, 21, 28, 35, 42])
        self.assertEqual(game.legal_moves(), ['b', 'c', 'd', 'e', 'f', 'g'])

    def test_init_with_board_that_is_not_over_2(self):
        game = Connect4(
            [['O', ' ', ' ', 'X', ' ', ' ', ' '],
             ['X', ' ', ' ', 'O', ' ', ' ', ' '],
             ['O', ' ', ' ', 'X', ' ', ' ', ' '],
             ['X', ' ', ' ', 'O', ' ', ' ', ' '],
             ['O', ' ', ' ', 'X', ' ', ' ', ' '],
             ['X', 'X', ' ', 'O', ' ', ' ', ' ']]
        )
        self.assertFalse(game.is_over())
        self.assertFalse(game._is_win(game._boards[0]))
        self.assertFalse(game._is_win(game._boards[1]))
        self.assertEqual(game.cur_player(), 1)
        self.assertEqual(game.legal_moves(), ['b', 'c', 'e', 'f', 'g'])

    def test_copy(self):
        self.game.make_moves('a', 'b')
        game_copy = self.game.copy()
        self.assertEqual(game_copy, self.game)
        self.assertIsNot(game_copy, self.game)
        self.assertIsInstance(game_copy, Connect4)
        self.assertIsInstance(game_copy, Connect4)
        self.assertEqual(game_copy.legal_moves(), self.game.legal_moves())
        self.assertIsNot(game_copy.legal_moves(), self.game.legal_moves())

    def test_hash(self):
        game1 = Connect4().make_moves('a', 'f')
        table = {game1: 'game1'}
        self.assertEqual(len(table), 1)
        self.assertEqual(table[game1], 'game1')
        game2 = Connect4().make_moves('a', 'f')
        table[game2] = 'game2'
        self.assertEqual(table[game1], 'game2')
        self.assertEqual(table[game2], 'game2')
        game3 = Connect4().make_moves('a', 'f', 'a')
        table[game3] = 'game3'
        self.assertEqual(len(table), 2)
        self.assertEqual(table[game3], 'game3')

    def test_not_equal(self):
        other = Connect4().make_moves('a')
        self.assertNotEqual(self.game, other)

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

    def test_make_moves(self):
        self.game.make_moves(*((['a'] * 6) + (['b'] * 6)))
        actual = self.game.legal_moves()
        expected = ['c', 'd', 'e', 'f', 'g']
        self.assertEqual(actual, expected)

    def test_make_moves_returns_self(self):
        self.assertIs(self.game.make_moves('a', 'b', 'c'), self.game)

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
