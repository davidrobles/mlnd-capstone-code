from .. import MDP
from ..games import TicTacToe
from ..util import ZobristHashing


class DeterministicOpponentMDP(MDP):
    '''
    A Markov Decision Process for Tic Tac Toe based on a deterministic opponent.
    '''

    def __init__(self, game, player, pix):
        '''
        player: the opponent player
        pix: the index of the agent that will interact with the environment
             that uses this MDP. It can be 0 or 1.
        '''
        self.game = game
        self.player = player
        self.pix = pix
        self._hashed_states = {}
        self._zobrist_hash = ZobristHashing(game.n_positions, game.n_pieces)
        self._generate_states(self.game)

    def _generate_states(self, game):
        '''Generates all the states for the game'''
        board_hash = self._zobrist_hash(game.board)
        if board_hash not in self._hashed_states:
            self._hashed_states[board_hash] = game
        for move in game.legal_moves():
            new_game = game.copy()
            new_game.make_move(move)
            self._generate_states(new_game)


    def __str__(self):
        return '<MDP states={}>'.format(len(self.states))

    #######
    # MDP #
    #######

    @property
    def states(self):
        return self._hashed_states.values()

    def transitions(self, game, move):
        '''Returns a dictionary of.
        This function is not available for a reinforcement learning agent.
        '''
        chosen_move = self.player.choose_move(game)
        if chosen_move != move:
            return {}
        new_game = game.copy()
        new_game.make_move(move)
        hashed = _zobrist_hash(new_game.board)
        return {hashed: 1.0}

    def actions(self, game):
        return game.legal_moves()

    def reward(self, state, action, next_state):
        from ..util import default_util_func
        if not next_state.is_over():
            return 0
        return default_util_func(next_state, self.pix)

    def is_terminal(self, state):
        return state.is_over()
