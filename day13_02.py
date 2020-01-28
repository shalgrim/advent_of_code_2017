from day13_01 import build_scanners, calculate_penalty_helper
from copy import deepcopy


def calc_delay(lines):
    base_scanners = build_scanners(lines)
    delay = 0

    while True:
        scanners = deepcopy(base_scanners)
        penalty = calculate_penalty_helper(lines, scanners)

        if penalty == 0:
            return delay

        delay += 1
        for bs in base_scanners:
            bs.tick()


if __name__ == '__main__':
    with open('./data/input13.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(calc_delay(lines))
