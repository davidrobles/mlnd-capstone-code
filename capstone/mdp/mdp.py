import abc
import six


@six.add_metaclass(abc.ABCMeta)
class MDP(object):
    '''
    Markov Decision Process

    This interface is based on the one used in:
    UC Berkeley CS188 (Intro to AI)
    http://ai.berkeley.edu/
    '''

    @abc.abstractmethod
    def states(self):
        '''
        Returns a list of all states.
        Not generally possible for large MDPs.
        '''
        pass

    @abc.abstractmethod
    def start_state(self):
        '''Returns the initial state.'''
        pass

    @abc.abstractmethod
    def actions(self, state):
        '''Returns a list of possible actions in the given state.'''
        pass

    @abc.abstractmethod
    def transitions(self, state, action):
        '''
        Returns a dict of (next_state: probability) key/values, where
        'next_state' is reachable from 'state' by taking 'action'. The sum of
        all probabilities should be 1.0.
        Note that in Q-Learning and reinforcment learning in general, we do
        not know these probabilities nor do we directly model them.
        '''
        pass

    @abc.abstractmethod
    def reward(self, state, action, next_state):
        '''
        Returns the reward of being in 'state', taking 'action', and ending up
        in 'next_state'.
        Not available in reinforcement learning.
        '''
        pass

    @abc.abstractmethod
    def is_terminal(self, state):
        '''
        Returns true if the given state is terminal. By convention, a terminal
        state has zero future rewards. Sometimes the terminal state(s) may have
        no possible actions. It is also common to think of the terminal state
        as having a self-loop action 'pass' with zero reward; the formulations
        are equivalent.
        '''
        pass
