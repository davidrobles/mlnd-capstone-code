from __future__ import print_function, unicode_literals
from aec import print_aec, str_aec
from .import Game


class TicTacToe(Game):

    """
    1 2 3
    4 5 6
    7 8 9
    """

    name = 'Tic Tac Toe'

    WINS = [0b000000111, 0b000111000, 0b111000000, 0b001001001,
            0b010010010, 0b100100100, 0b100010001, 0b001010100]

    def __init__(self):
        self.reset()

    @property
    def board(self):
        b = []
        for i in range(9):
            if self.boards[0] & (1 << i):
                b.append(0)
            elif self.boards[1] & (1 << i):
                b.append(1)
            else:
                b.append(' ')
        return b

    def _check_win(self, board):
        return any((board & win) == win for win in TicTacToe.WINS)

    def __eq__(self, other):
        if self.cur_player != other.cur_player:
            return False
        if self.boards[0] != other.boards[0]:
            return False
        if self.boards[1] != other.boards[1]:
            return False
        return True

    def __repr__(self):
        return TicTacToeView(self).render()

    def __str__(self):
        return TicTacToeView(self).render()

    ########
    # Game #
    ########

    def copy(self):
        """Returns a copy of the game"""
        tic = TicTacToe()
        tic._cur_player = self._cur_player
        tic.boards = self.boards[:]
        return tic

    @property
    def cur_player(self):
        return self._cur_player

    def is_over(self):
        """Returns true if the game is over"""
        return len(self.legal_moves()) == 0

    def legal_moves(self):
        """Returns the list of legal moves for the player in turn"""
        if self._check_win(self.boards[0]) or self._check_win(self.boards[1]):
            return []
        legal_board = ~(self.boards[0] | self.boards[1])
        return [move for move in range(1, 10) if legal_board & (1 << (move - 1))]

    def make_move(self, move):
        """Takes a move for the player in turn"""
        self.boards[self.cur_player] |= (1 << (move - 1))
        self._cur_player = (self.cur_player + 1) % 2
        return self

    def make_moves(self, *moves):
        for move in moves:
            self.make_move(move)
        return self

    def outcomes(self):
        """Returns a list of outcomes for each player at the end of the game"""
        if self._check_win(self.boards[0]):
            return ['W', 'L']
        elif self._check_win(self.boards[1]):
            return ['L', 'W']
        return ['D', 'D']

    @property
    def outcome(self):
        if self._check_win(self.boards[0]):
            return 'p1win'
        elif self._check_win(self.boards[1]):
            return 'p2win'
        return 'draw'

    def reset(self):
        """Restarts the game"""
        self._cur_player = 0
        self.boards = [0, 0]


class TicTacToeView(object):

    def __init__(self, game):
        self.game = game

    def _next_player(self):
        return str_aec('Next player: ', 'bold_green') + str(self.game.cur_player) + '\n'

    def _moves(self):
        s = '[{}]'.format(', '.join([str(s) for s in self.game.legal_moves()]))
        out = ''
        out += str_aec('Moves: ', 'bold_green') + s + '\n'
        return out

    def _board(self):
        s = ''
        for i in range(9):
            if self.game.boards[0] & (1 << i):
                s += str_aec(' X ', 'bold_red')
            elif self.game.boards[1] & (1 << i):
                s += str_aec(' O ', 'bold_blue')
            else:
                s += ' - '
            if i % 3 == 2:
                s += '\n'
        return s

    def _game_over(self):
        return str_aec('Game Over!', 'bold_green') + '\n'

    def render(self):
        s = ''
        if self.game.is_over():
            s += self._game_over()
        else:
            s += self._next_player()
            s += self._moves()
        s += '\n'
        s += self._board()
        return s
