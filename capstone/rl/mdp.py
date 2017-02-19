import abc
import six
from ..utils import utility


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


class GameMDP(MDP):
    '''
    A Markov Decision Process for a Game. Converts a game into an MPD by
    making an opponent with fixed behavior part of the environment.
    '''

    def __init__(self, game):
        self._game = game
        self._states = {}

    def actions(self, state):
        return [None] if state.is_over() else state.legal_moves()

    def is_terminal(self, state):
        return state.is_over()

    def reward(self, state, action, next_state):
        # return the utility from the point of view of the first player
        return utility(next_state, 0) if next_state.is_over() else 0

    def start_state(self):
        return self._game.copy()

    def states(self):
        if not self._states:
            def generate_states(game):
                '''Generates all the states for the game'''
                if game not in self._states:
                    self._states[game] = game
                for move in game.legal_moves():
                    new_game = game.copy().make_move(move)
                    generate_states(new_game)
            generate_states(self._game)
        return self._states

    def transitions(self, state, action):
        if state.is_over():
            return [(state, 1.0)]
        new_game = state.copy().make_move(action)
        return [(new_game, 1.0)]


class FixedGameMDP(GameMDP):

    def __init__(self, game, opp_player, opp_idx):
        '''
        opp_player: the opponent player
        opp_idx: the idx of the opponent player in the game
        '''
        super(FixedGameMDP, self).__init__(game)
        self._opp_player = opp_player
        self._opp_idx = opp_idx
        self._agent_idx = opp_idx ^ 1

    def reward(self, game, move, next_game):
        return utility(next_game, self._agent_idx) if next_game.is_over() else 0

    def start_state(self):
        new_game = self._game.copy()
        if not new_game.is_over() and new_game.cur_player() == self._opp_idx:
            chosen_move = self._opp_player.choose_move(new_game)
            new_game.make_move(chosen_move)
        return new_game

    def transitions(self, game, move):
        if game.is_over():
            return []
        new_game = game.copy().make_move(move)
        if not new_game.is_over() and new_game.cur_player() == self._opp_idx:
            chosen_move = self._opp_player.choose_move(new_game)
            new_game.make_move(chosen_move)
        return [(new_game, 1.0)]
