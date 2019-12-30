from unittest import TestCase
from day06_1 import main as part_one
from day06_2 import main as part_two


class TestDay06(TestCase):
    def test_part_one(self):
        self.assertEqual(part_one([0, 2, 7, 0])[0], 5)

    def test_part_two(self):
        self.assertEqual(part_two([0, 2, 7, 0]), 4)
