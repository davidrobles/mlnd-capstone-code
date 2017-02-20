from ..tabularf import TabularF
from ..policies import RandomPolicy
from ...utils import check_random_state


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

