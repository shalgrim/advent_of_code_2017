from unittest import TestCase

from day21_1 import START_GRID, grid_to_line, iterate, line_to_grid, rotate, flip, main, get_rules_from_file


class TestDay21(TestCase):
    def setUp(self):
        self.test_lines = ['../.# => ##./#../...', '.#./..#/### => #..#/..../..../#..#']
        self.test_rules = {}
        for line in self.test_lines:
            lhs, rhs = line.split(' => ')
            self.test_rules[lhs] = rhs

    def test_line_to_grid(self):
        self.assertEqual(line_to_grid('../.#'), ['..', '.#'])
        self.assertEqual(line_to_grid('.#./..#/###'), ['.#.', '..#', '###'])
        self.assertEqual(
            line_to_grid('#..#/..../#..#/.##.'), ['#..#', '....', '#..#', '.##.']
        )

    def test_grid_to_line(self):
        self.assertEqual(grid_to_line(['..', '.#']), '../.#')
        self.assertEqual(grid_to_line(['.#.', '..#', '###']), '.#./..#/###')
        self.assertEqual(
            grid_to_line(['#..#', '....', '#..#', '.##.']), '#..#/..../#..#/.##.'
        )

    def test_iterate(self):
        self.assertEqual(
            iterate(START_GRID, self.test_rules), ['#..#', '....', '....', '#..#']
        )

    def test_rotate(self):
        self.assertEqual(rotate(START_GRID), '#../#.#/##.')
        self.assertEqual(rotate('.#/.#'), '../##')

    def test_flip(self):
        self.assertEqual(flip(START_GRID), '.#./#../###')

    def test_part_one(self):
        self.assertEqual(main(get_rules_from_file('data/input21.txt'), 5), 120)
