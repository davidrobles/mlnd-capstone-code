from .callbacks import Callback, CallbackList
from .plot import EpisodicWLDPlotter


def max_qvalue(state, actions, qf):
    if not actions or actions[0] is None:
        return 0
    return max([qf[state, action] for action in actions])


def min_qvalue(state, actions, qf):
    if not actions or actions[0] is None:
        return 0
    return min([qf[state, action] for action in actions])
