from abc import ABCMeta, abstractmethod, abstractproperty


class Player(object):

    '''Player'''

    __metaclass__ = ABCMeta

    @abstractproperty
    def choose_move(self, move):
        pass


from .alphabeta import AlphaBeta
from .randplayer import RandPlayer
