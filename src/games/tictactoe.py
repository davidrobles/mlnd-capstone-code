from __future__ import print_function
from aec import print_aec, str_aec


class TicTacToeView(object):

    def next_player(self, game):
        return str_aec('Next player: ', 'bold_green') + str(game.cur_player) + '\n'

    def moves(self, game):
        s = '[' + ', '.join([str(s) for s in game.legal_moves()]) + ']'
        out = ''
        out += str_aec('Moves: ', 'bold_green') + s + '\n'
        return out

    def board(self, game):
        out = ''
        for i in range(9):
            if game.boards[0] & (1 << i):
                out += str_aec(' X ', 'bold_red')
            elif game.boards[1] & (1 << i):
                out += str_aec(' O ', 'bold_blue')
            else:
                out += ' - '
            if i % 3 == 2:
                out += '\n'
        return out

    def __call__(self, game):
        out = ''
        if game.is_over():
            out += str_aec('Game Over!', 'bold_green') + '\n'
        else:
            out += self.next_player(game)
            out += self.moves(game)
        out += '\n'
        out += self.board(game)
        return out


class TicTacToe(object):

    """
    1 2 3
    4 5 6
    7 8 9
    """

    name = 'Tic Tac Toe'

    WINS = [0b000000111, 0b000111000, 0b111000000, 0b001001001,
            0b010010010, 0b100100100, 0b100010001, 0b001010100]

    #############
    # TicTacToe #
    #############

    def __init__(self):
        self.reset()

    def __str__(self):
        view = TicTacToeView()
        outStr = ''
        outStr += view(self)
        outStr += '\n'
        return outStr

    def check_win(self, board):
        return any((board & win) == win for win in TicTacToe.WINS)

    def __eq__(self, other):
        if self.cur_player != other.cur_player:
            return False
        if self.boards[0] != other.boards[0]:
            return False
        if self.boards[1] != other.boards[1]:
            return False
        return True

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
        if self.check_win(self.boards[0]) or self.check_win(self.boards[1]):
            return []
        legal_board = ~(self.boards[0] | self.boards[1])
        return [move for move in range(1, 10) if legal_board & (1 << (move - 1))]

    def make_move(self, move):
        """Takes a move for the player in turn"""
        self.boards[self.cur_player] |= (1 << (move - 1))
        self._cur_player = (self.cur_player + 1) % 2
        return self

    def make_moves(self, moves):
        for move in moves:
            self.make_move(move)
        return self

    def outcomes(self):
        """Returns a list of outcomes for each player at the end of the game"""
        if self.check_win(self.boards[0]):
            return ['W', 'L']
        elif self.check_win(self.boards[1]):
            return ['L', 'W']
        return ['D', 'D']

    def reset(self):
        """Restarts the game"""
        self._cur_player = 0
        self.boards = [0, 0]


class TicUtility(object):

    def eval(self, game, player):
        if game.outcomes()[player] == 'W':
            return 1.0
        elif game.outcomes()[player] == 'L':
            return -1.0
        elif game.outcomes()[player] == 'D':
            return 0.0
        print('something is wrong' + game.outcomes()[player])
        return 0.0
