import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Policy(object):
    
    '''
    A policy is a mapping from perceived states of the environment
    to actions to be taken when in those states.
    '''

    @abc.abstractmethod
    def action(self, env, vf=None, qf=None):
        '''
        Chooses an action for the current state of the environment
        based on the given value function.
        vf: state function V(s)
        qf: state-action value function Q(s, a)
        '''
        pass
