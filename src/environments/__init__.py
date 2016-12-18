from abc import ABCMeta, abstractmethod


class Environment(object):

    '''An environment for reinforcement learning interactions.'''

    __metaclass__ = ABCMeta

    @abstractmethod
    def cur_state(self):
        '''Returns the current state'''
        pass

    @abstractmethod
    def actions(self, state):
        '''Returns the possible actions from the given state'''
        pass

    @abstractmethod
    def do_action(self, action):
        '''Performs the given action in the current state'''
        pass

    @abstractmethod
    def reset(self):
        '''Resets the current state to the start state'''
        pass

    def is_terminal(self):
        state = self.cur_state()
        actions = self.actions(state)
        return len(actions) == 0


from .tictactoe import TicTacToeEnv
