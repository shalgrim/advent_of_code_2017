from unittest import TestCase
from day15_1 import main, FACTOR_A, FACTOR_B


class TestDay15(TestCase):
    def test_main(self):
        self.assertEqual(main(FACTOR_A, 65, FACTOR_B, 8921, 2), 0)
        self.assertEqual(main(FACTOR_A, 65, FACTOR_B, 8921, 3), 1)
        self.assertEqual(main(FACTOR_A, 65, FACTOR_B, 8921, 5), 1)

    def test_main_long_running(self):
        self.assertEqual(main(FACTOR_A, 65, FACTOR_B, 8921, 40_000_000), 588)
