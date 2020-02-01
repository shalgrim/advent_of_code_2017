from unittest import TestCase

from day17_01 import main


class TestDay17(TestCase):
    def test_part_1(self):
        self.assertEqual(main(3), 638)
