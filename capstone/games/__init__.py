import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Game(object):
    '''Interface for abstract strategy games'''

    @abc.abstractmethod
    def copy(self):
        '''Returns a copy of the game'''
        pass

    @abc.abstractmethod
    def cur_player(self):
        '''Returns the index of the player in turn: 0 (Player 1) or 1 (Player 2)'''
        pass

    @abc.abstractmethod
    def is_over(self):
        '''Returns true if the game is over'''
        pass

    @abc.abstractmethod
    def legal_moves(self):
        '''Returnst a list of the legal moves'''
        pass

    @abc.abstractmethod
    def make_move(self, move):
        '''Makes one move for the player in turn'''
        pass

    @abc.abstractmethod
    def make_moves(self, *moves):
        '''Makes a series of moves'''
        pass

    @abc.abstractmethod
    def outcomes(self, moves):
        '''Returns a list of outcomes for each player at the end of the game'''
        pass

    @abc.abstractmethod
    def outcomes(self, moves):
        '''Returns a list of outcomes for each player at the end of the game'''
        pass

    @abc.abstractmethod
    def reset(self):
        pass


from .connect4 import Connect4
from .tictactoe import TicTacToe
