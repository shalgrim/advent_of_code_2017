from unittest import TestCase

from day24_1 import main


class TestDay24(TestCase):
    def test_part_one(self):
        with open('data/test24.txt') as f:
            lines = [line.strip() for line in f.readlines()]
        self.assertEqual(main(lines), 31)
