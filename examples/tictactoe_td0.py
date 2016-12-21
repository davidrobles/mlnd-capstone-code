from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta, RandPlayer
from capstone.util import ZobristHashing


class TabularTD0(object):

    def __init__(self, env, policy=RandPlayer(), alpha=0.01, gamma=0.99, n_episodes=1000):
        self.env = env
        self.policy = RandPlayer()
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self.zobrist_hash = ZobristHashing(n_positions=9, n_pieces=2)
        self._table = {}
        self._boards = {}

    def learn(self):
        import random
        for episode in range(self.n_episodes):
            print('Episode {}'.format(episode))
            self.env.reset()
            step = 0
            while not self.env.is_terminal():
                print('Step {}'.format(step))
                cur_state = self.env.cur_state()
                action = random.choice(self.env.actions())
                reward = self.env.do_action(action)
                # print('Reward {}'.format(reward))
                next_state = self.env.cur_state()
                cur_state_hash = self.zobrist_hash(cur_state.board)
                # print('cur_state_value_hash: {}'.format(cur_state_hash))
                cur_state_value = self._table.get(cur_state_hash, 0.1)
                next_state_hash = self.zobrist_hash(next_state.board)
                # print('next_state_value_hash: {}'.format(next_state_hash))
                next_state_value = self._table.get(next_state_hash, 0.3)
                new_value = cur_state_value + (self.alpha * (reward + (self.gamma * next_state_value) -  cur_state_value))
                # print('new_value {}'.format(new_value))
                self._table[cur_state_hash] = new_value
                self._boards[cur_state_hash] = cur_state
                # print('cur_state_hash' + str(cur_state_hash))
                # print(env.cur_state())
                step += 1
                if env.is_terminal():
                    self._table[next_state_hash] = reward;
        print('Results:')
        print(self._table)
        print(self._boards)

game = TicTacToe(
    'X-O'
    'XO-'
    '-XO'
)
ab = AlphaBeta()
mdp = GameMDP(game, ab, 1)
env = Environment(mdp)
td0 = TabularTD0(env)
td0.learn()
