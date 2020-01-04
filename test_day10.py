from unittest import TestCase

from day10_1 import hash_string
from day10_2 import main


class TestDay10(TestCase):
    def test_hash_string(self):
        hs_result = hash_string(5, [3, 4, 1, 5])
        self.assertEqual(hs_result[0], [3, 4, 2, 1, 0])
        self.assertEqual(hs_result[1], 4)
        self.assertEqual(hs_result[2], 4)

    def test_part_two(self):
        self.assertEqual(main(''), 'a2582a3a0e66e6e86e3812dcb672a272')
        self.assertEqual(main('AoC 2017'), '33efeb34ea91902bb2f59c9920caa6cd')
