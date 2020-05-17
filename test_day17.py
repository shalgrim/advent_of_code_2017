from unittest import TestCase

from day17_1 import main
from day17_2 import get_next


class TestDay17(TestCase):
    def test_part_1(self):
        self.assertEqual(main(3), 638)

    def test_get_next_0(self):
        self.assertEqual(get_next(0, 386), 1)

    def test_get_next_1(self):
        self.assertEqual(get_next(1, 386), 4)

    def test_get_next_4(self):
        self.assertEqual(get_next(4, 386), 7)

    def test_get_next_7(self):
        self.assertEqual(get_next(7, 386), 10)

    def test_get_next_10(self):
        self.assertEqual(get_next(10, 386), 39)

    def test_get_next_39(self):
        self.assertEqual(get_next(39, 386), 50)
