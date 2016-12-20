import unittest
from capstone.player import RandPlayer


class TestRandPlayer(unittest.TestCase):

    def setUp(self):
        self.rand_player = RandPlayer()

    def test_has_name(self):
        self.assertEqual(RandPlayer.name, "RandPlayer")
        self.assertEqual(self.rand_player.name, "RandPlayer")
