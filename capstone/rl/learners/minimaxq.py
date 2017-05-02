import abc
import six
from ..policy import Policy


@six.add_metaclass(abc.ABCMeta)
class RLAgent(Policy):
    '''
    A reinforcement learning agent that learns by interacting with an environment.
    '''

    @abc.abstractmethod
    def update(self, experience, max_or_min):
        pass


class MinimaxQ(RLAgent):
    '''
    Minimax-Q algorithm.

    # Arguments
        action_space: action space.
        policy: behavior policy.
        qfunction: a state-action value function.
        learning_rate: float >= 0.
        discount_factor: float >= 0.

    # References
        - Michael L. Littman. 1994.
          Markov games as a framework for multi-agent reinforcement learning.
          Proc. 11th International Conference on Machine Learning. 157-163.
    '''

    def __init__(self, action_space, policy, qfunction, learning_rate=0.1, discount_factor=1.0):
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
        if done:
            target = reward
        else:
            next_actions = self.action_space(next_state)
            qvalues = [self.qfunction[next_state, next_action] for next_action in next_actions]
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
