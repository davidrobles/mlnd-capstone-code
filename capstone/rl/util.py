def _min_or_max_action_value(self, qf, state, actions, min_or_max):
    return min_or_max([self.qf[(state, action)] for action in actions])

def max_action_value(self, qf, state, actions):
    return _min_or_max_action_value(qf, state, actions, max)

def min_action_value(self, qf, state, actions):
    return _min_or_max_action_value(qf, state, actions, min)
