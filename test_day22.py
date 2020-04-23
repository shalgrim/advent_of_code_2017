from unittest import TestCase

from day22_1 import main


class Day22(TestCase):
    def setUp(self):
        self.lines = ['..#', '#..', '...']

    def test_part_one(self):
        self.assertEqual(main(self.lines, 7), 5)
        # self.assertEqual(main(self.lines, 70), 41)  # dubious
        self.assertEqual(main(self.lines), 5587)
