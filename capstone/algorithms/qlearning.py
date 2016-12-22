import random
from capstone.player import RandPlayer


class QLearning(object):

    def __init__(self, env, policy=RandPlayer(), vf={}, alpha=0.1,
                 gamma=0.99, n_episodes=1000):
        self.env = env
        self.policy = RandPlayer()
        self.alpha = alpha
        self.gamma = gamma
        self.n_episodes = n_episodes
        self.vf = vf

    def max_q_value(self, state):
        actions = self.env.actions(state)
        if not actions:
            return 0
        best_value = -100000
        for next_action in actions:
            temp_value = self.vf.get((state, next_action), random.random() - 0.5)
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
                q_value = self.vf.get((state, action), random.random() - 0.5)
                update_value = reward + (self.gamma * max_q_value) - q_value
                self.vf[(state, action)] = q_value + (self.alpha * update_value)
                step += 1
        print('Results:')
        for (state, action), value in self.vf.iteritems():
            print('State:\n\n{}'.format(state))
            print('Action:\n\n{}\n'.format(action))
            print('Value:\n\n{}'.format(value))
            print('*' * 60)
