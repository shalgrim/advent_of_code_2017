from unittest import TestCase

from day19_1 import get_letters_on_path


class TestDay19(TestCase):
    def test_part_one(self):
        with open('data/test19.txt') as f:
            lines = [line[:-1] for line in f.readlines()]
        self.assertEqual(get_letters_on_path(lines), 'ABCDEF')
