'''
To implement Value Iteration in a game I need to have the deterministic
policy passed.

To be able to use the Value Iteration algorithm we need an mdp with
a function to get all the states. For example: it is possible to have
the MDP for Tic Tac Toe where the opponent ALWAYS makes the same move.
However, is not possible for Connect 4 because the state is too large.
'''
from games import TicTacToe
from utils import ZobristHashing


class TicTacToeMDP(object):

    def __init__(self):
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

    def transitions(self, state, action):
        '''Returns a dictionary of
        This function is not available for a reinforcement learning agent.
        '''
        pass

    def actions(self, state):
        '''Returns a list of possible actions in the given state'''
        pass

    def reward(state, action, next_state):
        '''Returns the reward of being in 'state', taking 'action',
        and moving to the 'next_state'. This function is not available
        for a reinforcement learning agent.
        '''
        pass


class ValueIteration(object):

    def __init__(self, mdp, policy, theta, gamma):
        self.mdp = mdp
        self.policy = policy
        self.theta = theta
        self.gamma = gamme
        self.table = {}

    # def learn(self):
    #     delta = 0
    #     while True:
    #         for move in game.legal_moves():
    #             new_game = game.copy()
    #             new_game.make_move(move)
    #             old_value = self.table[zobrist_hash(new_game)]
    #             new_value = -1000000
    #         if delta < theta:
    #             break
    #     print('DP Value Iteration finished')

mdp = TicTacToeMDP()
print(mdp)
