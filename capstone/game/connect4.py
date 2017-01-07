from __future__ import print_function, unicode_literals
from . import Game
from ..util import print_aec, str_aec, ZobristHashing


class Connect4(Game):

    Rows = 6
    Cols = 7
    H1 = Rows + 1
    H2 = Rows + 2
    SIZE = Rows * Cols
    SIZE1 = H1 * Cols
    ALL1 = (1 << SIZE1) - 1
    COL1 = (1 << H1) - 1;
    BOTTOM = ALL1 / COL1
    TOP = BOTTOM << Rows

    def __init__(self):
        self.reset()

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
        if self._check_win(self._boards[0]) or self._check_win(self._boards[1]):
            return c4
        c4._moves = []
        for m in self._moves:
            c4._moves.append(m)
        for c in range(Connect4.Cols):
            c4._height[c] = self._height[c]
        return c4

    def cur_player(self):
        return self._cur_player

    def legal_moves(self):
        return self._moves

    def make_move(self, move):
        if move not in self._moves:
            print(type(move))
            raise Exception('Invalid move: {}'.format(move))
        self._move_made = move
        new_board = self._boards[self.cur_player()] | (1 << self._height[move])
        self._height[move] += 1
        self._boards[self.cur_player()] = new_board
        self._cur_player = (self.cur_player() + 1) % 2
        if self._check_win(new_board):
            self._moves = []
        else:
            self._moves = []
            for i in range(Connect4.Cols):
                if ((1 << self._height[i]) & Connect4.TOP) == 0:
                    self._moves.append(i)
        return self

    def outcomes(self):
        if self._check_win(self._boards[0]):
            return ['W', 'L']
        elif self._check_win(self._boards[1]):
            return ['L', 'W']
        return ['D', 'D']

    def reset(self):
        self._cur_player = 0
        self._boards = [0, 0]
        self._height = [0] * Connect4.Cols
        self._init_moves()
        self._move_made = None

    #############
    # Connect 4 #
    #############

    def _init_moves(self):
        self._moves = []
        for i in range(Connect4.Cols):
            self._height[i] = Connect4.H1 * i
            if (1 << self._height[i]) & Connect4.TOP == 0:
                self._moves.append(i)

    def _check_win(self, board):
        y = board & (board >> 7)
        if (y & (y >> 2 * 7)): # check \ diagonal
            return True
        y = board & (board >> 8)
        if (y & (y >> 2 * 8)): # check horizontal -
            return True
        y = board & (board >> 9)
        if (y & (y >> 2 * 9)): # check / diagonal
            return True
        y = board & (board >> 1)
        if (y & (y >> 2)):     # check vertical |
            return True
        return False


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
        if self.game._move_made:
            out += str_aec('Move made: ', 'bold_green') + str(self.game._move_made) + '\n'
        return out

    def _board(self):
        out = ''
        for a in range(Connect4.Cols):
            out += str(self.game._height[a]) + '\n'
        out += '\n\n  '
        for col in range(Connect4.Cols):
            out += ' ' + chr(97 + col)
        out = str_aec(out, 'bold_green') + '\n'
        for row in range(Connect4.Rows - 1, -1, -1):
            out += ' ' + str_aec(str(row + 1), 'bold_green')
            for col in range(Connect4.Cols):
                hello = (col * 7) + row
                if (1 << hello) & self.game._boards[0]:
                    out += str_aec(' X', 'bold_red')
                elif (1 << hello) & self.game._boards[1]:
                    out += str_aec(' O', 'bold_blue')
                else:
                    out += ' .'
            out += '\n'
        out += '\n'
        out += '-' * 80
        out += '\n'
        return out

    # def _piece(self, ix):
    #     if self.game._boards[0] & (1 << ix):
    #         return str_aec('X', 'bold_red')
    #     elif self.game._boards[1] & (1 << ix):
    #         return str_aec('O', 'bold_blue')
    #     else:
    #         return '-'

    def _outcomes(self):
        return '\n' + str(self.game.outcomes()) if self.game.is_over() else ''

    def render(self):
        return '{info}{board}{outcomes}'.format(
            info=self._info(),
            board=self._board(),
            outcomes=self._outcomes()
        )
