from unittest import TestCase

from day11_1 import get_final_steps_away
from day11_2 import get_furthest_away


class TestDay11(TestCase):
    def setUp(self):
        with open('data/input11.txt') as f:
            content = f.read().strip()
        self.all_directions = content.split(',')

    def test_part_1_a(self):
        self.assertEqual(get_final_steps_away(['ne', 'ne', 'ne']), 3)
        self.assertEqual(get_final_steps_away(['ne', 'ne', 'sw', 'sw']), 0)

    def test_part_1_b(self):
        """pulled these out of examples because they fail"""
        self.assertEqual(get_final_steps_away(['ne', 'ne', 's', 's']), 2)
        self.assertEqual(get_final_steps_away(['se', 'sw', 'se', 'sw', 'sw']), 3)

    def test_part_1(self):
        self.assertEqual(get_final_steps_away(self.all_directions), 824)

    def test_early_steps(self):
        self.assertEqual(get_final_steps_away([]), 0)
        self.assertEqual(get_final_steps_away(self.all_directions[:1]), 1)

    def test_part_2(self):
        self.assertEqual(get_furthest_away(self.all_directions), 1548)
