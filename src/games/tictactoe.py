from __future__ import print_function
from aec import print_aec, str_aec


class TicTacToe(object):

    """
    1 2 3
    4 5 6
    7 8 9
    """

    WINS = [0b000000111, 0b000111000, 0b111000000, 0b001001001,
            0b010010010, 0b100100100, 0b100010001, 0b001010100]

    #############
    # TicTacToe #
    #############

    def __init__(self):
        self.reset()

    def __str__(self):
        outStr = ''
        if self.is_over():
            outStr += str_aec('Game Over!', 'bold_green') + '\n'
        else:
            outStr += str_aec('Next player: ', 'bold_green') + str(self.cur_player) + '\n'
            s = '[' + ', '.join([str(s) for s in self.legal_moves()]) + ']'
            outStr += str_aec('Moves: ', 'bold_green') + s + '\n'
        outStr += '\n'
        for i in range(9):
            if self.boards[0] & (1 << i):
                outStr += str_aec(' X ', 'bold_red')
            elif self.boards[1] & (1 << i):
                outStr += str_aec(' O ', 'bold_blue')
            else:
                outStr += ' - '
            if i % 3 == 2:
                outStr += '\n'
        return outStr

    def check_win(self, board):
        return any((board & win) == win for win in TicTacToe.WINS)

    def is_win(self):
        return self.check_win(self.boards[0]) or self.check_win(self.boards[1])

    ########
    # Game #
    ########

    def copy(self):
        """Returns a copy of the game"""
        tic = TicTacToe()
        tic.cur_player = self.cur_player
        tic.boards = self.boards[:]
        return tic

    def is_over(self):
        """Returns true if the game is over"""
        return len(self.legal_moves()) == 0

    def legal_moves(self):
        """Returns the list of legal moves for the player in turn"""
        if self.is_win():
            return []
        self.legal = ~(self.boards[0] | self.boards[1])
        return [move for move in range(1, 10) if self.legal & (1 << (move - 1))]

    def make_move(self, move):
        """Takes a move for the player in turn"""
        self.boards[self.cur_player] |= (1 << (move - 1))
        self.cur_player = (self.cur_player + 1) % 2

    def name(self):
        """Name of the game"""
        return "Tic Tac Toe"

    def outcomes(self):
        """Returns a list of outcomes for each player"""
        if not self.is_over():
            return ['NA', 'NA']
        elif self.check_win(self.boards[0]):
            return ['W', 'L']
        elif self.check_win(self.boards[1]):
            return ['L', 'W']
        return ['D', 'D']

    def reset(self):
        """Restarts the game"""
        self.cur_player = 0
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
