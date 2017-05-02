import abc
import six
from .policy import Policy


@six.add_metaclass(abc.ABCMeta)
class RLAgent(Policy):
    '''
    A reinforcement learning agent that learns by interacting with an environment.
    '''

    @abc.abstractmethod
    def update(self, experience):
        pass
