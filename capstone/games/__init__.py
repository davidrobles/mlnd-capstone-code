import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Game(object):
    '''Interface for abstract strategy games'''


    @abc.abstractmethod
    def copy(self):
        pass

    @abc.abstractproperty
    def cur_player(self):
        pass

    @abc.abstractmethod
    def is_over(self):
        pass

    @abc.abstractmethod
    def legal_moves(self):
        pass

    @abc.abstractmethod
    def make_move(self, move):
        pass

    @abc.abstractmethod
    def make_moves(self, moves):
        pass

    @abc.abstractmethod
    def outcomes(self, moves):
        """Returns a list of outcomes for each player at the end of the game"""
        pass

    @abc.abstractmethod
    def outcomes(self, moves):
        """Returns a list of outcomes for each player at the end of the game"""
        pass

    @abc.abstractmethod
    def reset(self):
        pass

from .connect4 import Connect4
from .tictactoe import TicTacToe
