from unittest import TestCase

from day16_2 import rotate


class TestDay16(TestCase):
    def test_rotate(self):
        self.assertEqual(rotate('abcdefghijklmnop'), 'ionlbkfeajgdmphc')