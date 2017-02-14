'''
This implementation is based in John Tromp's Java implementation
of Connect 4.

https://github.com/qu1j0t3/fhourstones/blob/master/Connect4.java
'''

from __future__ import division, unicode_literals

import six
from . import Game
from ..utils import print_aec, str_aec, ZobristHashing


ROWS = 6
COLS = 7
H1 = ROWS + 1
H2 = ROWS + 2
SIZE = ROWS * COLS
SIZE1 = H1 * COLS
ALL1 = (1 << SIZE1) - 1
COL1 = (1 << H1) - 1
BOTTOM = ALL1 // COL1
TOP = BOTTOM << ROWS


def board_str_to_board_mdarray(board):
    return [list(board[row*COLS:(row*COLS)+COLS]) for row in range(ROWS)]


class Connect4(Game):

    ROWS = 6
    COLS = 7

    name = 'Connect4'
    n_positions = ROWS * COLS
    n_pieces = 2
    zobrist_hash = ZobristHashing(n_positions, n_pieces)

    def __init__(self, board=None):
        if board:
            if isinstance(board, six.string_types):
                self.board = board_str_to_board_mdarray(board)
            elif isinstance(board, list):
                self.board = board
        else:
            self.reset()

    def __hash__(self):
        b = []
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS):
                hello = (col * 7) + row
                if (1 << hello) & self._boards[0]:
                    b.append(0)
                elif (1 << hello) & self._boards[1]:
                    b.append(1)
                else:
                    b.append(' ')
        return Connect4.zobrist_hash(b)

    def __eq__(self, other):
        attrs = ['_cur_player', '_boards', '_moves', '_height']
        return all([getattr(self, name) == getattr(other, name) for name in attrs])

    def __repr__(self):
        return Connect4View(self).render()

    def __str__(self):
        return Connect4View(self).render()

    ########
    # Game #
    ########

    def copy(self):
        c4 = Connect4()
        c4._cur_player = self._cur_player
        c4._boards = self._boards[:]
        c4._moves = self._moves[:]
        c4._height = self._height[:]
        return c4

    def cur_player(self):
        return self._cur_player

    def legal_moves(self):
        '''
        Returns the legal moves for the player in turn.
        Each move is the letter of the column where the piece
        will be placed.
        Example: ['a', 'b', 'c', 'f']
        '''
        return [chr(ord('a') + move) for move in self._moves]

    def make_move(self, move):
        '''
        A move is the letter of the column where the piece will be placed.
        '''
        move = ord(move) - ord('a')
        if move not in self._moves:
            print(type(move))
            raise Exception('Invalid move: {}'.format(move))
        new_board = self._boards[self.cur_player()] | (1 << self._height[move])
        self._height[move] += 1
        self._boards[self.cur_player()] = new_board
        self._cur_player ^= 1
        self._moves = [] if self._is_win(new_board) else self._generate_moves()
        if self._is_win(new_board):
            self._moves = []
            # self._cur_player = None
        else:
            self._moves = self._generate_moves()
        return self

    def outcomes(self):
        if self._is_win(self._boards[0]):
            return ['W', 'L']
        elif self._is_win(self._boards[1]):
            return ['L', 'W']
        return ['D', 'D']

    def reset(self):
        self._cur_player = 0
        self._boards = [0, 0]
        self._height = [H1 * col for col in range(COLS)]
        self._moves = self._generate_moves()

    #############
    # Connect 4 #
    #############

    @property
    def board(self):
        board = [[' '] * COLS for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                ix = (col * 7) + (ROWS - row - 1)
                if (1 << ix) & self._boards[0]:
                    board[row][col] = 'X'
                elif (1 << ix) & self._boards[1]:
                    board[row][col] = 'O'
        return board

    @board.setter
    def board(self, board):
        self._boards = [0, 0]
        counters = [0, 0]
        self._height = [H1 * col for col in range(COLS)]
        max_cols = [0] * COLS
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == 'X'):
                    self._boards[0] |= 1 << ((col * COLS) + (ROWS - row - 1))
                    counters[0] += 1
                    max_cols[col] = max(max_cols[col], 6 - row)
                elif (board[row][col] == 'O'):
                    self._boards[1] |= 1 << ((col * COLS) + (ROWS - row - 1))
                    counters[1] += 1
                    max_cols[col] = max(max_cols[col], 6 - row)
        for col in range(COLS):
            self._height[col] = (col * 7) + max_cols[col]
        if self._is_win(self._boards[0]) or self._is_win(self._boards[1]):
            # self._cur_player = None
            self._moves = []
            return
        diff = counters[0] - counters[1]
        if diff == 0:
            self._cur_player = 0
        elif diff == 1:
            self._cur_player = 1
        else:
            raise Exception('Illegal board!')
        self._moves = self._generate_moves()

    def _generate_moves(self):
        return [col for col in range(COLS) if ((1 << self._height[col]) & TOP) == 0]

    def _is_win(self, board):
        '''Returns Ttrue if the given bitboard has a winning pattern.'''
        y = board & (board >> ROWS)
        if y & (y >> 2 * ROWS):
            return True
        y = board & (board >> H1)
        if y & (y >> 2 * H1):
            return True
        y = board & (board >> H2)
        if y & (y >> 2 * H2):
            return True
        y = board & (board >> 1)
        if y & (y >> 2):
            return True
        return False

    #############
    # Debugging #
    #############

    def print_bitboard(self, board):
        out = '  '
        for col in range(COLS):
            out += ' ' + chr(97 + col)
        out = str_aec(out, 'bold_green') + '\n'
        for row in range(ROWS, -1, -1):
            out += ' ' + str_aec(str(row + 1), 'bold_green')
            for col in range(COLS + 10):
                hello = (col * 7) + row
                if (1 << hello) & board:
                    out += str_aec(' X', 'bold_red')
                else:
                    out += ' .'
            out += '\n'
        out += '\n'
        out += '-' * 80
        out += '\n'
        print(out)


class Connect4View(object):

    def __init__(self, game):
        self.game = game

    def _info(self):
        if self.game.is_over():
            return self._game_over() + '\n'
        return self._next_player() + self._moves() + '\n'

    def _game_over(self):
        return str_aec('Game Over!', 'bold_green') + '\n'

    def _next_player(self):
        return str_aec('Next player: ', 'bold_green') + str(self.game.cur_player()) + '\n'

    def _moves(self):
        s = '[{}]'.format(', '.join([str(s) for s in self.game.legal_moves()]))
        out = ''
        out += str_aec('Moves: ', 'bold_green') + s + '\n'
        return out

    def _board(self):
        out = '  '
        for col in range(COLS):
            out += ' ' + chr(97 + col)
        out = str_aec(out, 'bold_green') + '\n'
        for row in range(ROWS - 1, -1, -1):
            out += ' ' + str_aec(str(row + 1), 'bold_green')
            for col in range(COLS):
                hello = (col * 7) + row
                if (1 << hello) & self.game._boards[0]:
                    out += str_aec(' X', 'bold_red')
                elif (1 << hello) & self.game._boards[1]:
                    out += str_aec(' O', 'bold_blue')
                else:
                    out += ' .'
            out += '\n'
        return out

    def _outcomes(self):
        return '\n' + str(self.game.outcomes()) if self.game.is_over() else ''

    def render(self):
        return '{info}{board}{outcomes}'.format(
            info=self._info(),
            board=self._board(),
            outcomes=self._outcomes()
        )
