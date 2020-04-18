from day13_01 import build_scanners, calculate_penalty_helper
from copy import deepcopy


def gets_caught(scanners):
    firewall_length = max([s.depth for s in scanners]) + 1
    location = -1

    while location < firewall_length:
        location += 1
        for scanner in scanners:
            if scanner.depth == location and scanner.location == 0:
                return True
            scanner.tick()

    return False


# I think I need to do it a different way, this takes too long
# Should be possible with mods?
def calc_delay(lines):
    base_scanners = build_scanners(lines)
    delay = 0

    while True:
        scanners = deepcopy(base_scanners)

        if not gets_caught(scanners):
            return delay

        delay += 1
        for bs in base_scanners:
            bs.tick()


if __name__ == '__main__':
    with open('./data/input13.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(calc_delay(lines))
