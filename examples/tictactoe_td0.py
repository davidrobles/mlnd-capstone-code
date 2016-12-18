from capstone.players import RandPlayer
from capstone.util import ZobristHashing

# class TabularTD0(object):

#     def __init__(self, env, policy, alpha, gamma, n_episodes):
#         self.env = env
#         self.policy = policy
#         self.alpha = alpha
#         self.gamma = gamme
#         self.n_episodes = n_episodes

#     def learn(self):
#         for episode in range(self.n_episodes):
#             pass

#     def step(self):
#         action = self.policy.choose_action(self.env)
#         cur_state = env.cur_state()
#         reward = env.make_action(action)
#         next_state = env.cur_state()
#         new_value = self.table[


class TabularTD0(object):

    def __init__(self, env, policy, alpha, gamma, n_episodes):
        self.env = env
        self.policy = RandPlayer()
        self.alpha = alpha
        self.gamma = gamme
        self.n_episodes = n_episodes
        self.zobrist_hash = ZobristHashing(n_positions=9, n_pieces=2)

    def learn(self):
        for episode in range(self.n_episodes):
            pass

    def step(self):
        move = self.policy.choose_move(self.game)
        cur_state = self.game.copy()
        cur_state_hash = self.zobrist_hash(cur_state)
        reward = self.game.make_move(action)
        next_state = env.cur_state()
        new_value = self.table[cur_state] + (alpha * (reward (gamme * table[next_state]) - table[cur_state]
