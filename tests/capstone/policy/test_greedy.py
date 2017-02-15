import unittest
from capstone.policy import Greedy


class TestGreedy(unittest.TestCase):

    def setUp(self):
        self.policy = Greedy()

    def test_max_action(self):
        state = 1
        actions = [1, 5, 8]
        fake_qf = {
            (state, 1): 5,
            (state, 5): 33,
            (state, 8): 23,
        }
        action = self.policy.action(state, actions, fake_qf)
        self.assertEqual(action, 5)

    def test_raises_value_error_if_no_actions_available(self):
        state = 1
        actions = []
        with self.assertRaises(ValueError):
            self.policy.action(state, actions)
