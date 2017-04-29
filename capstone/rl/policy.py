import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Policy(object):
    '''
    A policy is a mapping from perceived states of the environment
    to actions to be taken when in those states.
    '''

    @abc.abstractmethod
    def get_action(self, state):
        '''
        Returns one of the available actions from the given state.
        '''
        pass
