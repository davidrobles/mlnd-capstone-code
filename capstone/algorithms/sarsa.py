import random
from capstone.policy import EGreedyPolicy
from capstone.policy import RandomPolicy


class Sarsa(object):

    def __init__(self, env, policy=EGreedyPolicy(epsilon=0.1), qf={}, alpha=0.1,
                 gamma=0.99, n_episodes=1000):
        self.env = env
        self.policy = policy
        self.qf = qf
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes

    def init(self):
        '''Initializes the q-value if unvisited'''
        state = self.env.cur_state()
        actions = self.env.actions(state)
        for action in actions:
            if self.env.is_terminal():
                self.qf[(state, action)] = 0
            elif (state, action) not in self.qf:
                self.qf[(state, action)] = random.random() - 0.5

    def learn(self):
        for episode in range(1, self.n_episodes + 1):
            print('Episode {}'.format(episode))
            self.env.reset()
            step = 1
            self.init()
            action = self.policy.action(self.env, qf=self.qf)
            while True:
                print('Step {}'.format(step))
                state = self.env.cur_state()
                reward, next_state = self.env.do_action(action)
                self.init()
                next_action = self.policy.action(self.env, qf=self.qf)
                update_value = reward + (self.gamma * self.qf[(next_state, next_action)]) - self.qf[(state, action)]
                self.qf[(state, action)] += self.alpha * update_value
                step += 1
                if self.env.is_terminal():
                    break
