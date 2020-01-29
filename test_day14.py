from unittest import TestCase
from day14_1 import get_free_squares


class TestDay14(TestCase):
    def test_part_1(self):
        self.assertEqual(get_free_squares('flqrgnkx'), 8108)
