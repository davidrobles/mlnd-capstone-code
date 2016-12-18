from abc import ABCMeta, abstractmethod, abstractproperty


class MDP(object):

    '''Markov Decision Process'''

    __metaclass__ = ABCMeta

    @abstractproperty
    def states(self):
        pass

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def transitions(self, state, action):
        pass

    @abstractmethod
    def reward(self, state, action, next_state):
        pass

from .tictactoe import TicTacToeMDP
