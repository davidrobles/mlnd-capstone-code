from . import Policy


class GreedyPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        state = env.cur_state()
        actions = env.actions()
        if not actions:
            print('called with no actions')
            return 0
        best_value = -100000
        best_action = None
        for next_action in actions:
            value = qf[(state, next_action)]
            if value > best_value:
                best_value = value
                best_action = next_action
        return best_action
