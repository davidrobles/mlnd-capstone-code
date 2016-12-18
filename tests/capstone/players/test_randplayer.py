import unittest
from capstone.players import RandPlayer


class TestRandPlayer(unittest.TestCase):

    def setUp(self):
        self.ab = RandPlayer()

    def test_has_name(self):
        self.assertEqual(RandPlayer.name, "Random Player")

    def test_can_instantiate(self):
        pass
