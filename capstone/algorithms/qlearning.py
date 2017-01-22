import random
from capstone.policy import RandomPolicy


class QLearning(object):

    def __init__(self, env, policy=RandomPolicy(), qf={}, alpha=0.1,
                 gamma=0.99, n_episodes=1000):
        self.env = env
        self.behaviour_policy = policy
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

    def max_qvalue(self):
        if self.env.is_terminal():
            return 0
        state = self.env.cur_state()
        actions = self.env.actions(state)
        return max([self.qf[(state, action)] for action in actions])

    def learn(self):
        for episode in range(1, self.n_episodes + 1):
            print('Episode %d / %d)' % (episode, self.n_episodes))
            self.env.reset()
            step = 1
            while not self.env.is_terminal():
                print('  Step %d' % step)
                self.init()
                state = self.env.cur_state()
                action = self.behaviour_policy.action(self.env, qf=self.qf)
                reward, next_state = self.env.do_action(action)
                self.init()
                td_error = reward + (self.gamma * self.max_qvalue()) - self.qf[(state, action)]
                self.qf[(state, action)] += self.alpha * td_error
                step += 1
