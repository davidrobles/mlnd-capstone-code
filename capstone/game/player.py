import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Player(object):
    '''Interface for a Player of a Game'''

    @abc.abstractmethod
    def choose_move(self, game):
        '''Returns the chosen move from game.legal_moves().'''
        pass
