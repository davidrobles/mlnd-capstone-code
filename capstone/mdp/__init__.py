import abc
import six


@six.add_metaclass(abc.ABCMeta)
class MDP(object):
    '''Markov Decision Process'''

    @abc.abstractproperty
    def states(self):
        pass

    @abc.abstractmethod
    def actions(self, state):
        pass

    @abc.abstractmethod
    def transitions(self, state, action):
        pass

    @abc.abstractmethod
    def reward(self, state, action, next_state):
        pass


from .tictactoe import TicTacToeMDP
