import random
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
        self.table = {}

    def max_q_value(self, state):
        actions = self.env.actions(state)
        if not actions:
            return 0
        best_value = -100000
        for next_action in actions:
            temp_value = self.table.get((state, next_action), random.random() - 0.5)
            if temp_value > best_value:
                best_value = temp_value
        return best_value

    def learn(self):
        for episode in range(self.n_episodes):
            print('Episode {}'.format(episode))
            self.env.reset()
            step = 0
            while not self.env.is_terminal():
                print('Step {}'.format(step))
                state = self.env.cur_state()
                action = random.choice(self.env.actions(state))
                reward, next_state = self.env.do_action(action)
                max_q_value = self.max_q_value(next_state)
                q_value = self.table.get((state, action), 0.1)
                update_value = reward + (self.gamma * max_q_value) - q_value
                self.table[(state, action)] = q_value + (self.alpha * update_value)
                step += 1
        print('Results:')
        for key, value in self.table.iteritems():
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
