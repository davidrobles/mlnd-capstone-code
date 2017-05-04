from .utils import CallbackList, Experience


class EpisodicInteraction(object):

    def train(self, n_episodes, callbacks=None):
        '''Trains the model for a fixed number of episodes.'''
        callbacks = CallbackList(callbacks)
        callbacks.on_train_begin()
        for episode in range(n_episodes):
            callbacks.on_episode_begin(episode)
            # self.env.reset()
            print('Episode {}'.format(episode))
            self.episode()
            callbacks.on_episode_end(episode)
        callbacks.on_train_end()

    def episode(self):
        pass


class MDPInteraction(EpisodicInteraction):
    '''
    Interaction between an MDP and a policy.
    '''
    def episode(self):
        state = self.amg.start_state()
        while not self.amg.is_terminal(state):
            action = self.policy.get_action(state)
            for ns, prob in self.amg.transitions(state, action):
                next_state = ns
            reward = self.amg.reward(state, action, next_state)
            done = self.amg.is_terminal(next_state)
            if hasattr(policy, 'update'):
                experience = Experience(state, action, reward, next_state, done)
                policy.update(experience, max if next_state.cur_player() == 0 else min)
            state = next_state


class AMGInteraction(EpisodicInteraction):
    '''
    Interaction between an Alternating Markov Game and two policies.
    '''

    def __init__(self, amg, policies):
        self.amg = amg
        self.policies = policies

    def episode(self):
        state = self.amg.start_state()
        while not self.amg.is_terminal(state):
            cur_player = self.amg.cur_player(state)
            policy = self.policies[cur_player]
            action = policy.get_action(state)
            for ns, prob in self.amg.transitions(state, action):
                next_state = ns
            reward = self.amg.reward(state, action, next_state)
            done = self.amg.is_terminal(next_state)
            if hasattr(policy, 'update'):
                experience = Experience(state, action, reward, next_state, done)
                policy.update(experience, max if next_state.cur_player() == 0 else min)
            state = next_state
