def _min_or_max_action_value(qf, state, actions, min_or_max):
    if not actions:
        return 0
    return min_or_max([qf[(state, action)] for action in actions])


def max_action_value(qf, state, actions):
    return _min_or_max_action_value(qf, state, actions, max)


def min_action_value(qf, state, actions):
    return _min_or_max_action_value(qf, state, actions, min)
