import unittest
from capstone.policy import GreedyPolicy
from capstone.util import play_match


class FakeEnv(object):

    def __init__(self):
        self._actions = []

    def cur_state(self):
        return 'FakeState'

    def actions(self, state):
        return self._actions


class TestGreedy(unittest.TestCase):

    def setUp(self):
        self.policy = GreedyPolicy()
        self.env = FakeEnv()

    def test_max_action(self):
        state = 1
        actions = [1, 5, 8]
        fake_qf = {
            (state, 1): 5,
            (state, 5): 33,
            (state, 8): 23,
        }
        action = self.policy.action(fake_qf, state, actions)
        self.assertEqual(action, 5)

    def test_raises_value_error_if_no_actions_available(self):
        state = 1
        actions = []
        with self.assertRaises(ValueError):
            self.policy.action({}, state, actions)
