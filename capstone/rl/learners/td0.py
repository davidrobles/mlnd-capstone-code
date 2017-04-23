from ..learner import Learner
from ..utils import max_qvalue, min_qvalue


class TabularTD0(Learner):

    def __init__(self, env, policy, vfunction, learning_rate=0.1, discount_factor=1.0):
        super(TabularTD0, self).__init__(env)
        self.policy = policy
        self.vfunction = vfunction
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def step(self):
        state = self.env.cur_state()
        action = self.policy.action(state)
        reward, next_state = self.env.do_action(action)
        target = reward + (self.discount_factor * self.vfunction[next_state])
        td_error = target - self.vfunction[next_state, action]
        self.vfunction[state] += self.learning_rate * td_error
        # TODO: fix issue of afterstates

    ###########
    # Learner #
    ###########

    def episode(self):
        while not self.env.is_terminal():
            self.step()
