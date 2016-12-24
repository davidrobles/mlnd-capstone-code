from . import Policy


# add a parameter to maximise or minimize the value

class GreedyPolicy(Policy):

    def action(self, env, vf=None, qf=None):
        state = env.cur_state()
        actions = env.actions(state)
        try:
            return max([qf[(state, action)] for action in actions])
        except Exception as e:
            import pdb; pdb.set_trace()
        return 0

        # best_value = -100000
        # for next_action in actions:
        #     temp_value = qf[(state, next_action)]
        #     if temp_value > best_value:
        #         best_value = temp_value
        # return best_value
