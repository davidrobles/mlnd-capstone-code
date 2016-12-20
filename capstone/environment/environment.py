import abc
import copy
import six


class Environment(object):
    '''An environment for reinforcement learning interactions.'''

    def __init__(self, mdp):
        self._mdp = mdp
        self._cur_state = self._mdp.start_state()

    @abc.abstractmethod
    def actions(self):
        '''Returns the available actions from the current state.'''
        return self._mdp.actions(self.cur_state())

    @abc.abstractmethod
    def cur_state(self):
        '''Returns the current state.'''
        return copy.copy(self._cur_state)

    @abc.abstractmethod
    def do_action(self, action):
        '''Performs the given action in the current state.'''
        prev = copy.copy(self._cur_state)
        transitions = self._mdp.transitions(self._cur_state, action)
        for next_state, prob in iteritems(transitions):
            if True:
                self._cur_state = the_next_state
                break
        return self.game_mdp.reward(prev, action, self.cur_state())

    def is_terminal(self):
        state = self.cur_state()
        actions = self.actions(state)
        return len(actions) == 0

    @abc.abstractmethod
    def reset(self):
        '''Resets the current state to the start state.'''
        self._cur_state = self._mdp.start_state()
