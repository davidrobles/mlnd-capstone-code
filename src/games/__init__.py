from abc import ABCMeta, abstractmethod, abstractproperty


class Game(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def copy(self):
        pass

    @abstractproperty
    def cur_player(self):
        pass

    @abstractmethod
    def is_over(self):
        pass

    @abstractmethod
    def legal_moves(self):
        pass

    @abstractmethod
    def make_move(self, move):
        pass

    @abstractmethod
    def make_moves(self, moves):
        pass

    @abstractmethod
    def outcomes(self, moves):
        """Returns a list of outcomes for each player at the end of the game"""
        pass

    @abstractmethod
    def outcomes(self, moves):
        """Returns a list of outcomes for each player at the end of the game"""
        pass

    @abstractmethod
    def reset(self):
        pass










from .connect4 import Connect4
from .tictactoe import TicTacToe
