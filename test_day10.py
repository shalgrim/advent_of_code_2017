from unittest import TestCase

from day10_1 import hash_string


class TestDay10(TestCase):
    def test_hash_string(self):
        self.assertEqual(hash_string(5, [3, 4, 1, 5])[:2], [3, 4])