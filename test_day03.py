from collections import defaultdict
from unittest import TestCase

from day03_2 import get_next_xy, set_xy


class TestDay03(TestCase):
    def setUp(self):
        self.values = defaultdict(lambda: 0)
        self.values[(0, 0)] = 1

    def test_get_next_xy(self):
        self.assertEqual(get_next_xy(0, 0, self.values), (1, 0))
        self.assertEqual(set_xy(1, 0, self.values), 1)
        self.assertEqual(get_next_xy(1, 0, self.values), (1, -1))
        self.assertEqual(set_xy(1, -1, self.values), 2)
        self.assertEqual(get_next_xy(1, -1, self.values), (0, -1))
        self.assertEqual(set_xy(0, -1, self.values), 4)
        self.assertEqual(get_next_xy(0, -1, self.values), (-1, -1))
        self.assertEqual(set_xy(-1, -1, self.values), 5)
        self.assertEqual(get_next_xy(-1, -1, self.values), (-1, 0))
        self.assertEqual(set_xy(-1, 0, self.values), 10)
        self.assertEqual(get_next_xy(-1, 0, self.values), (-1, 1))
        self.assertEqual(set_xy(-1, 1, self.values), 11)
        self.assertEqual(get_next_xy(-1, 1, self.values), (0, 1))
        self.assertEqual(set_xy(0, 1, self.values), 23)
        self.assertEqual(get_next_xy(0, 1, self.values), (1, 1))
        self.assertEqual(set_xy(1, 1, self.values), 25)
        self.assertEqual(get_next_xy(1, 1, self.values), (2, 1))
        self.assertEqual(set_xy(2, 1, self.values), 26)
        self.assertEqual(get_next_xy(2, 1, self.values), (2, 0))
        self.assertEqual(set_xy(2, 0, self.values), 54)
