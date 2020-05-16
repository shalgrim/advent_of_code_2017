from unittest import TestCase
from day13_1 import calculate_penalty
from day13_2 import calc_delay


class TestDay13(TestCase):
    def setUp(self) -> None:
        with open('./data/test13.txt') as f:
            self.test_lines = [line.strip() for line in f.readlines()]

        with open('./data/input13.txt') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def test_calculate_penaty(self):
        self.assertEqual(calculate_penalty(self.test_lines), 24)

    def test_calc_delay(self):
        self.assertEqual(calc_delay(self.test_lines), 10)

    def test_part_one(self):
        self.assertEqual(calculate_penalty(self.lines), 1876)
