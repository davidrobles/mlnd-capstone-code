import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Player(object):
    '''Interface for a Player of a Game'''


    @abc.abstractmethod
    def choose_move(self, move):
        pass


from .alphabeta import AlphaBeta
from .randplayer import RandPlayer
