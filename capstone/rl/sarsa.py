from .tabularf import TabularF
from ..policy import RandomPolicy
from ..utils import check_random_state


class Sarsa(object):

    def __init__(self, env, policy=None, qf=None, alpha=0.1, gamma=0.99,
                 n_episodes=1000, random_state=None):
        self.env = env
        self.policy = policy
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self.random_state = check_random_state(random_state)
        self.policy = policy or RandomPolicy(self.random_state)
        self.qf = qf or TabularF(self.random_state)
        self.cur_episode = 1

    def learn(self):
        for _ in range(self.n_episodes):
            self.episode()

    def episode(self):
        print('Episode {self.cur_episode} / {self.n_episodes}'.format(self=self))
        self.env.reset()
        step = 1
        state, actions = self.env.cur_state_and_actions()
        action = self.policy.action(self.qf, state, actions)
        while not self.env.is_terminal():
            print('Step {}'.format(step))
            reward, next_state, next_actions = self.env.do_action(action)
            next_action = self.policy.action(self.qf, next_state, next_actions)
            td_error = reward + (self.gamma * self.qf[next_state, next_action]) - self.qf[state, action]
            self.qf[state, action] += self.alpha * td_error
            state, action = next_state, next_action
            step += 1
        self.cur_episode += 1
