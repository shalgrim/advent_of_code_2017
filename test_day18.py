from unittest import TestCase

from day18_1 import clean_instructions
from day18_2 import main


class TestDay18(TestCase):
    def test_part_two(self):
        lines = ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']
        instructions = [line.split() for line in lines]
        clean_instructions(instructions)
        self.assertEqual(main(instructions), 3)
