from unittest import TestCase
from day13_01 import calculate_penalty


class TestDay13(TestCase):
    def setUp(self) -> None:
        with open('./data/test13.txt') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def test_calculate_penaty(self):
        self.assertEqual(calculate_penalty(self.lines), 24)
