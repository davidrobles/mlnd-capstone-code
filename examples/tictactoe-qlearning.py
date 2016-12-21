from capstone.environment import Environment
from capstone.game import TicTacToe
from capstone.mdp import GameMDP
from capstone.player import AlphaBeta, RandPlayer
from capstone.util import ZobristHashing


class TabularQLearning(object):

    def __init__(self, env, policy=RandPlayer(), alpha=0.1, gamma=0.99, n_episodes=1000):
        self.env = env
        self.policy = RandPlayer()
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self._table = {}

    def learn(self):
        import random
        for episode in range(self.n_episodes):
            print('Episode {}'.format(episode))
            self.env.reset()
            step = 0
            while not self.env.is_terminal():
                print('Step {}'.format(step))
                state = self.env.cur_state()
                action = random.choice(self.env.actions())
                reward = self.env.do_action(action)
                next_state = self.env.cur_state()
                best_value = -100000
                if not env.actions():
                    best_value = 0
                else:
                    for next_action in self.env.actions():
                        temp_value = self._table.get((next_state, next_action), 0.1)
                        if temp_value > best_value:
                            best_value = temp_value
                q_value = self._table.get((state, action), 0.1)
                update_value = reward + (self.gamma * best_value) - q_value
                self._table[(state, action)] = q_value + (self.alpha * update_value)
                step += 1
        print('Results:')
        for key, value in self._table.iteritems():
            print(key)
            print(value)
            print('*' * 60)

game = TicTacToe(
    'X-O'
    'XO-'
    '-XO'
)
ab = AlphaBeta()
mdp = GameMDP(game, ab, 1)
env = Environment(mdp)
td0 = TabularQLearning(env)
td0.learn()
