from ..learner import Learner


class Sarsa(Learner):

    def __init__(self, env, policy, qfunction, learning_rate=0.1,
                 discount_factor=0.99, **kwargs):
        super(Sarsa, self).__init__(env, **kwargs)
        self.policy = policy
        self.qfunction = qfunction
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    ###########
    # Learner #
    ###########

    def episode(self):
        state = self.env.cur_state()
        action = self.policy.action(state)
        while not self.env.is_terminal():
            reward, next_state = self.env.do_action(action)
            next_action = self.policy.action(next_state)
            target = reward + (self.discount_factor * self.qfunction[next_state, next_action])
            td_error = target - self.qfunction[state, action]
            self.qfunction[state, action] += self.learning_rate * td_error
            state, action = next_state, next_action


class SarsaSelfPlay(Sarsa):

    def best_qvalue(self, state):
        best_qvalue = max_qvalue if state.cur_player() == 0 else min_qvalue
        return best_qvalue(state, self.env.actions(state), self.qfunction)
