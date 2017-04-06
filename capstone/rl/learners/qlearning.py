from ..learner import Learner
from ..utils import max_qvalue, min_qvalue


class QLearning(Learner):
    '''Tabular Q-learning'''

    def __init__(self, env, policy, qfunction, learning_rate=0.1,
                 discount_factor=1.0, selfplay=False):
        super(QLearning, self).__init__(env)
        self.policy = policy
        self.qfunction = qfunction
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.selfplay = selfplay

    def best_qvalue(self, state):
        if self.selfplay:
            best_func = max_qvalue if state.cur_player() == 0 else min_qvalue
            return best_func(state, self.env.actions(state), self.qfunction)
        return max_qvalue(state, self.env.actions(state), self.qfunction)

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            state = self.env.cur_state()
            action = self.policy.action(state)
            reward, next_state = self.env.do_action(action)
            best_qvalue = self.best_qvalue(next_state)
            target = reward + (self.discount_factor * best_qvalue)
            td_error = target - self.qfunction[state, action]
            self.qfunction[state, action] += self.learning_rate * td_error
