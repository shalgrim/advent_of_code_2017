from collections import Counter
from enum import Enum, auto


class Direction(Enum):
    N = auto()
    NE = auto()
    SE = auto()
    S = auto()
    SW = auto()
    NW = auto()

    def __sub__(self, other):
        if not isinstance(other, Direction):
            raise TypeError(f'unsupported right-hand operator for -: {type(other)}')

        small, big = sorted([self.value, other.value])
        diff = big - small

        if diff == 0:
            return 0
        elif diff in (1, 5):
            return 1
        elif diff in (2, 4):
            return 2
        return 3


DIRECTION_MAP = {
    'n': Direction.N,
    'ne': Direction.NE,
    'se': Direction.SE,
    's': Direction.S,
    'sw': Direction.SW,
    'nw': Direction.NW,
}


def do_easy_cancels(counter, d1, d2):
    big = d1 if counter[d1] > counter[d2] else d2
    little = d1 if big == d2 else d2
    counter[big] -= counter[little]
    counter[little] = 0


def do_hard_cancel(counter):
    """
    After taking out the easy cancels on all three axes, figure out the remaining steps. NB: This moves things into
    potentially the wrong counter spots, this is just meant to give an accurate count at the end
    :param counter: dict counting number of moves by direction
    :return: None (but there are side effects on counter
    """
    leftovers = [k for k in counter.keys() if counter[k]]
    assert len(leftovers) <= 3, f'{leftovers=}'

    if len(leftovers) <= 1:
        return
    elif len(leftovers) == 2:
        if counter[leftovers[0]] > counter[leftovers[1]]:
            big_key, small_key = leftovers
        else:
            small_key, big_key = leftovers

        spaces_apart = DIRECTION_MAP[leftovers[0]] - DIRECTION_MAP[leftovers[1]]

        if spaces_apart == 3:  # just straight up cancellation
            # should never be here, this should be covered in easy cancels
            counter[big_key] -= counter[small_key]
            counter[small_key] = 0
        elif spaces_apart == 2:
            counter[small_key] = 0
        elif spaces_apart == 1:
            pass  # noop
        else:
            raise AssertionError(f'{spaces_apart=}')
    else:
        leftovers_with_values = [(k, counter[k]) for k in leftovers]
        leftovers_with_values.sort(key=lambda x: x[1])
        small_key, mid_key, big_key = [tpl[0] for tpl in leftovers_with_values]
        counter[big_key] -= counter[small_key]
        counter[mid_key] += counter[small_key]
        counter[small_key] = 0


def main():
    with open('data/input11.txt') as f:
        content = f.read().strip()
    directions = content.split(',')
    return get_final_steps_away(directions)


def get_final_steps_away(directions):
    counter = Counter(directions)
    do_easy_cancels(counter, 'n', 's')
    do_easy_cancels(counter, 'ne', 'sw')
    do_easy_cancels(counter, 'nw', 'se')
    do_hard_cancel(counter)
    return sum(counter.values())


if __name__ == '__main__':
    print(main())
