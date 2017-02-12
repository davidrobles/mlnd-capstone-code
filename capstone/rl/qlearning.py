import random
from capstone.policy import RandomPolicy
from .util import max_action_value


class QLearning(object):

    """

    Q-learning is a model-free reinforcement learning technique. Can be used
    to find an optimal action-selection policy for any given (finite) MDP by
    interacting with an environment.

    Parameters
    ----------
    env : Environment

    behavior_policy : the policy generating the trajectory data

    qf : the action-value function

    alpha : learning rate

    gamma : discount factor

    n_episodes : number of episodes

    best : the function used to select the best action-value (e.g. max)
    """

    def __init__(self, env, policy=RandomPolicy(), qf={}, alpha=0.1,
                 gamma=0.99, n_episodes=1000):
        self.env = env
        self.behavior_policy = policy
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

    def best_action_value(self, qf, state, actions):
        return max_action_value(qf, state, actions)

    def learn(self):
        self.n_episode = 1
        for _ in range(self.n_episodes):
            self.episode()

    def episode(self):
        print('Episode {self.n_episode} / {self.n_episodes}'.format(self=self))
        self.env.reset()
        step = 1
        while not self.env.is_terminal():
            print('  Step %d' % step)
            self.init()
            state = self.env.cur_state()
            action = self.behavior_policy.action(self.env, qf=self.qf)
            reward, next_state = self.env.do_action(action)
            self.init()
            next_actions = self.env.actions(next_state)
            best_action_value = self.best_action_value(self.qf, next_state, next_actions)
            td_error = reward + (self.gamma * best_action_value) - self.qf[(state, action)]
            self.qf[(state, action)] += self.alpha * td_error
            step += 1
        self.n_episode += 1
