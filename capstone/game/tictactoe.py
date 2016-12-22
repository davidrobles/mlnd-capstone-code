from __future__ import print_function, unicode_literals
from . import Game
from ..util import print_aec, str_aec, ZobristHashing


class TicTacToe(Game):

    """
    1 2 3
    4 5 6
    7 8 9
    """

    name = 'Tic-Tac-Toe'
    # used for zobrist hashing
    n_positions = 9
    n_pieces = 2

    WINS = [0b000000111, 0b000111000, 0b111000000, 0b001001001,
            0b010010010, 0b100100100, 0b100010001, 0b001010100]

    zobrist_hash = ZobristHashing(n_positions, n_pieces)

    def __hash__(self):
        return TicTacToe.zobrist_hash(self.board)

    def __init__(self, board=None):
        self.reset()
        if board:
            for ix, c in enumerate(board):
                if c == 'X':
                    self._boards[0] |= 1 << ix
                    self._cur_player ^= 1
                elif c == 'O':
                    self._boards[1] |= 1 << ix
                    self._cur_player ^= 1

    def copy(self):
        tic = TicTacToe()
        tic._cur_player = self._cur_player
        tic._boards = self._boards[:]
        return tic

    @property
    def board(self):
        b = []
        for i in range(9):
            if self._boards[0] & (1 << i):
                b.append(0)
            elif self._boards[1] & (1 << i):
                b.append(1)
            else:
                b.append(' ')
        return b

    def _check_win(self, player_idx):
        '''Returns true if there is a winning board for the given player'''
        board = self._boards[player_idx]
        return any((board & win) == win for win in TicTacToe.WINS)

    def __eq__(self, other):
        if self.cur_player() != other.cur_player():
            return False
        if self._boards[0] != other._boards[0]:
            return False
        if self._boards[1] != other._boards[1]:
            return False
        return True

    def __repr__(self):
        return TicTacToeView(self).render()

    def __str__(self):
        return TicTacToeView(self).render()

    ########
    # Game #
    ########

    def cur_player(self):
        return self._cur_player

    def legal_moves(self):
        if any([self._check_win(pix) for pix in range(2)]):
            return []
        board = ~(self._boards[0] | self._boards[1])
        return [move for move in range(1, 10) if board & (1 << (move - 1))]

    def make_move(self, move):
        self._boards[self.cur_player()] |= (1 << (move - 1))
        self._cur_player ^= 1
        return self

    def outcomes(self):
        """Returns a list of outcomes for each player at the end of the game"""
        if self._check_win(0):
            return ['W', 'L']
        elif self._check_win(1):
            return ['L', 'W']
        return ['D', 'D']

    def reset(self):
        """Restarts the game"""
        self._cur_player = 0
        self._boards = [0, 0]


class TicTacToeView(object):

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
        return '\n'.join([self._row(row) for row in range(3)]) + '\n'

    def _row(self, row):
        return ' '.join([self._piece((row * 3) + col) for col in range(3)])

    def _piece(self, ix):
        if self.game._boards[0] & (1 << ix):
            return str_aec('X', 'bold_red')
        elif self.game._boards[1] & (1 << ix):
            return str_aec('O', 'bold_blue')
        else:
            return '-'

    def _outcomes(self):
        return '\n' + str(self.game.outcomes()) if self.game.is_over() else ''

    def render(self):
        return '{info}{board}{outcomes}'.format(
            info=self._info(),
            board=self._board(),
            outcomes=self._outcomes()
        )
