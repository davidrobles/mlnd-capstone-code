import random
from capstone.player import RandPlayer


class RandomPolicy(object):

    def action(self, env, vf=None, qf=None):
        return random.choice(env.actions(env.cur_state()))


class QLearning(object):

    def __init__(self, env, policy=RandomPolicy(), qf={}, alpha=0.1,
                 gamma=0.99, n_episodes=1000):
        self.env = env
        self.policy = policy
        self.qf = qf
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes

    def max_q_value(self, state):
        actions = self.env.actions(state)
        if not actions:
            return 0
        best_value = -100000
        for next_action in actions:
            temp_value = self.qf.get((state, next_action), random.random() - 0.5)
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
                action = self.policy.action(self.env, self.qf)
                reward, next_state = self.env.do_action(action)
                max_q_value = self.max_q_value(next_state)
                q_value = self.qf.get((state, action), random.random() - 0.5)
                update_value = reward + (self.gamma * max_q_value) - q_value
                self.qf[(state, action)] = q_value + (self.alpha * update_value)
                step += 1
        print('Results:')
        for (state, action), value in self.qf.iteritems():
            print('State:\n\n{}'.format(state))
            print('Action:\n\n{}\n'.format(action))
            print('Value:\n\n{}'.format(value))
            print('*' * 60)
