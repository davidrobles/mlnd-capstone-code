from games import TicTacToe
from utils import ZobristHashing


class TicTacToeMDP(object):

    '''
    A Markov Decision Process for Tic Tac Toe based on a deterministic player.
    '''

    def __init__(self, player):
        self.player = player
        self.hashed_states = {}
        self.zobrist_hash = ZobristHashing(n_positions=9, n_pieces=2)
        self._generate_states(TicTacToe())

    def _generate_states(self, game):
        '''Generates all the states for the game'''
        board_hash = self.zobrist_hash(game.board)
        if board_hash not in self.hashed_states:
            self.hashed_states[board_hash] = game
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
        '''Returns a list of all states'''
        return self.hashed_states.values()

    def transitions(self, game, move):
        '''Returns a dictionary of.
        This function is not available for a reinforcement learning agent.
        '''
        chosen_move = self.player.choose_move(game)
        if chosen_move != move:
            return {}
        new_game = game.copy()
        new_game.make_move(move)
        hashed = self.zobrist_hash(new_game.board)
        return {hashed: 1.0}

    def actions(self, game):
        '''Returns a list of possible moves in the game'''
        return game.legal_moves()

    def reward(self, state, action, next_state):
        '''Returns the reward of being in 'state', taking 'action',
        and moving to the 'next_state'. This function is not available
        for a reinforcement learning agent.
        '''
        from utils import default_util_func
        if not next_state.is_over():
            return 0
        return default_util_func(next_state, state.cur_player)
