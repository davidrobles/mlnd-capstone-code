from ..policy import Policy
from ..utils import max_qvalue, min_qvalue

# TODO rename as minimax q
class QLearner(Policy):
    '''
    Tabular Q-learning.

    # Arguments
        env: environment.
        policy: behavior policy.
        qfunction: a state-action value function.
        learning_rate: float >= 0.
        discount_factor: float >= 0.
        selfplay: boolean. Whether to use the same policy 
    '''

    def __init__(self, action_space, policy, qfunction, learning_rate=0.1,
                 discount_factor=1.0):
        self.action_space = action_space
        self.policy = policy
        self.qfunction = qfunction
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    #######################
    # RLLearner Interface #
    #######################

    def update(self, experience, max_or_min):
        '''This is called after an action was taken'''
        state, action, reward, next_state, done = experience
        # assert state.cur_player() == 0
        if done:
            target = reward
        else:
            next_actions = self.action_space(next_state)
            qvalues = [self.qfunction[next_state, next_action] for next_action in next_actions]
            # best_qvalue = max_or_min(qvalues)
            # best_func = max if state.cur_player() == 0 else min
            best_qvalue = max_or_min(qvalues)
            target = reward + (self.discount_factor * best_qvalue)
        td_error = target - self.qfunction[state, action]
        self.qfunction[state, action] += self.learning_rate * td_error

    # A learner interface needs an update policy

    ####################
    # Policy Interface # 
    ####################

    def get_action(self, state):
        return self.policy.get_action(state)
