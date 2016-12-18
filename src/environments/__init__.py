from abc import ABCMeta, abstractmethod, abstractproperty


class Environment(object):

    '''An environment for reinforcement learning interactions.'''

    __metaclass__ = ABCMeta

    @abstractproperty
    def cur_state(self):
        pass

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def do_action(self, state, action):
        pass

    @abstractmethod
    def reset(self):
        pass

    def is_terminal(self):
        state = self.cur_state()
        actions = self.actions(state)
        return len(actions) == 0


from .tictactoe import TicTacToeEnv
