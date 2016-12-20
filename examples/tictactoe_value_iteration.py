'''
To implement Value Iteration in a game I need to have the deterministic
policy passed.

Value iteration is an offline planner (dynamic programming), not a
reinforcement agent.

To be able to use the Value Iteration algorithm we need an mdp with
a function to get all the states. For example: it is possible to have
the MDP for Tic Tac Toe where the opponent ALWAYS makes the same move.
However, is not possible for Connect 4 because the state is too large.
'''
from capstone.game import TicTacToe
from copy import copy

# class ValueIteration(object):

#     def __init__(self, mdp, policy, theta, gamma):
#         self.mdp = mdp
#         self.policy = policy
#         self.theta = theta
#         self.gamma = gamme
#         self.table = {}

    # def learn(self):
    #     delta = 0
    #     while True:
    .copy()#         for move in game.legal_moves():
    #             new_game = copy(game)
    #             new_game.make_move(move)
    #             old_value = self.table[zobrist_hash(new_game)]
    #             new_value = -1000000
    #         if delta < theta:
    #             break
    #     print('DP Value Iteration finished')
