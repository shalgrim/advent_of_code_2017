from unittest import TestCase
from day12_01 import main


class TestDay12(TestCase):
    def setUp(self) -> None:
        with open('./data/test12.txt') as f:
            self.lines = [line.strip() for line in f.readlines()]

    def test_main(self):
        self.assertEqual(main(self.lines, '0'), 6)
