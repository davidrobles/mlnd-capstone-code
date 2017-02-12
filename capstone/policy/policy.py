import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Policy(object):
    
    '''
    A policy is a mapping from perceived states of the environment
    to actions to be taken when in those states.
    '''

    @abc.abstractmethod
    def action(self, vf, state, actions=None):
        pass
