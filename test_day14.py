from unittest import TestCase

from day14_1 import get_used_squares


class TestDay14(TestCase):
    def test_part_1(self):
        self.assertEqual(get_used_squares('flqrgnkx'), 8108)
