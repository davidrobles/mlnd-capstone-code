from ..policies import RandomPolicy
from ..util import max_action_value
from ..value_functions import TabularF
from ...utils import check_random_state


class QLearning(object):

    def __init__(self, env, policy=None, qf=None, alpha=0.1, gamma=0.99,
                 n_episodes=1000, random_state=None):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(self.random_state)
        self.qf = qf or TabularF(self.random_state)
        self.cur_episode = 1

    def best_action_value(self, state, actions):
        return max_action_value(self.qf, state, actions)

    def learn(self):
        for _ in range(self.n_episodes):
            self.episode()

    def episode(self):
        print('Episode {self.cur_episode} / {self.n_episodes}'.format(self=self))
        self.env.reset()
        step = 1
        while not self.env.is_terminal():
            print('  Step %d' % step)
            state, actions = self.env.cur_state_and_actions()
            action = self.policy.action(state, actions, self.qf)
            reward, next_state, next_actions = self.env.do_action(action)
            best_action_value = self.best_action_value(next_state, next_actions)
            td_error = reward + (self.gamma * best_action_value) - self.qf[state, action]
            self.qf[state, action] += self.alpha * td_error
            step += 1
        self.cur_episode += 1
