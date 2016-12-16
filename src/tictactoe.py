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

    def __init__(self):
        self.reset()

    def __str__(self):
        outStr = ''
        if self.is_over():
            outStr += str_aec('Game Over!', 'bold_green') + '\n'
        else:
            outStr += str_aec('Next player: ', 'bold_green') + str(self.cur_player()) + '\n'
            s = '[' + ', '.join([str(s) for s in self.legal_moves()]) + ']'
            # outStr += str_aec('Moves: ', 'bold_green') + str(self.num_moves()) + '\n'
            outStr += str_aec('Moves: ', 'bold_green') + s + '\n'
        outStr += '\n'
        for i in range(9):
            if self.crosses & (1 << i):
                outStr += ' X '
            elif self.noughts & (1 << i):
                outStr += ' O '
            else:
                outStr += ' - '
            if i % 3 == 2:
                outStr += '\n'
        return outStr

    def check_win(self, board):
        return any((board & win) == win for win in TicTacToe.WINS)

    def set_cur_board(self, board):
        if self.cur_player() == 0:
            self.crosses = board
        else:
            self.noughts = board

    def cur_board(self):
        return self.crosses if self.cur_player() == 0 else self.noughts

    def bit_count(self, int_type):
        count = 0
        while int_type:
            int_type &= int_type - 1
            count += 1
        return count

    def legal_moves(self):
        if self.is_win():
            return []
        self.legal = ~(self.crosses | self.noughts)
        return [move for move in range(1, 10) if self.legal & (1 << (move - 1))]

    def is_win(self):
        return self.check_win(self.crosses) or self.check_win(self.noughts)

    ########
    # Game #
    ########

    def copy(self):
        tic = TicTacToe()
        tic.crosses = self.crosses
        tic.noughts = self.noughts
        return tic

    def cur_player(self):
        """Returns the index of the player in turn: 0 (Player 1), 1 (Player 2)"""
        return -1 if self.is_over() else (len(self.legal_moves()) + 1) % 2

    def is_over(self):
        return self.is_win() or len(self.legal_moves()) == 0

    def make_move(self, move):
        print('Trying to move: ', move)
        # TODO: Check for ilegal moves?
        move -= 1
        # bit_ms = self.bit_moves()
        # if move < 0 or move >= self.num_moves():
        #     print('Illegal move!')
        # self.set_cur_board(self.cur_board() | bit_ms[move])
        self.set_cur_board(self.cur_board() | (1 << move))

    def name(self):
        return "Tic Tac Toe"

    def num_moves(self):
        return len(self.legal_moves())

    def outcomes(self):
        if not self.is_over():
            return ['NA', 'NA']
        elif self.check_win(self.crosses):
            return ['W', 'L']
        elif self.check_win(self.noughts):
            return ['L', 'W']
        return ['D', 'D']

    def reset(self):
        self.crosses = 0
        self.noughts = 0


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
