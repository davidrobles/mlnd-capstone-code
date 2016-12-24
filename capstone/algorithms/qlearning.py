import random
from capstone.policy import GreedyPolicy, RandomPolicy


class QLearning(object):

    def __init__(self, env, policy=RandomPolicy(), qf={}, alpha=0.1,
                 gamma=0.99, n_episodes=1000):
        self.env = env
        self.behaviour_policy = policy
        self.max_policy = GreedyPolicy()
        self.qf = qf
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes

    def init(self):
        '''Initializes the q-value if unvisited'''
        state = self.env.cur_state()
        actions = self.env.actions(state)
        for action in actions:
            if (state, action) not in self.qf:
                self.qf[(state, action)] = random.random() - 0.5

    def learn(self):
        for episode in range(self.n_episodes):
            print('Episode {}'.format(episode))
            self.env.reset()
            step = 0
            while not self.env.is_terminal():
                print('Step {}'.format(step))
                self.init()
                state = self.env.cur_state()
                action = self.behaviour_policy.action(self.env, self.qf)
                reward, next_state = self.env.do_action(action)
                self.init()
                max_qvalue = self.max_policy.action(self.env, qf=self.qf)
                # max_q_value = self.max_q_value(next_state)
                q_value = self.qf[(state, action)]
                update_value = reward + (self.gamma * max_qvalue) - q_value
                self.qf[(state, action)] = q_value + (self.alpha * update_value)
                step += 1
