from unittest import TestCase

from day09_1 import count_groups, find_garbage_end, find_group_end, score_groups


class TestDay09(TestCase):
    def test_find_garbage_end(self):
        examples = [
            '<>',
            '<random characters>',
            '<<<<>',
            '<{!>}>',
            '<!!>',
            '<!!!>>',
            '{o"i!a,<{i<a>',
        ]
        for example in examples:
            self.assertEqual(find_garbage_end(example[1:]), len(example) - 1)

    def test_count_groups(self):
        self.assertEqual(count_groups('{}'), 1)
        self.assertEqual(count_groups('{{{}}}'), 3)
        self.assertEqual(count_groups('{{},{}}'), 3)
        self.assertEqual(count_groups('{{{},{},{{}}}}'), 6)
        self.assertEqual(count_groups('{<{},{},{{}}>}'), 1)
        self.assertEqual(count_groups('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(count_groups('{{<a>},{<a>},{<a>},{<a>}}'), 5)
        self.assertEqual(count_groups('{{<!>},{<!>},{<!>},{<a>}}'), 2)

    def test_find_group_end(self):
        self.assertEqual(find_group_end('{}'), 1)
        self.assertEqual(find_group_end('{{{}}}'), 5)

    def test_score_groups(self):
        self.assertEqual(score_groups('{}'), 1)
        self.assertEqual(score_groups('{{{}}}'), 6)
        self.assertEqual(score_groups('{{},{}}'), 5)
        self.assertEqual(score_groups('{{{},{},{{}}}}'), 16)
        self.assertEqual(score_groups('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(score_groups('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual(score_groups('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(score_groups('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)
