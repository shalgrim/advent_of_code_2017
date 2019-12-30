from unittest import TestCase
from day06_1 import main


class TestDay06(TestCase):
    def test_main_1(self):
        self.assertEqual(main([0, 2, 7, 0]), 5)
