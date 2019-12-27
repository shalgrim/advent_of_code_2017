from itertools import permutations


def checksum_evenly_divisible(lines):
    grid = [line.split() for line in lines]
    rv = 0
    for line in grid:
        nums = [int(n) for n in line]
        perms = permutations(nums, 2)
        for perm in perms:
            if perm[0] % perm[1] == 0:
                rv += perm[0] // perm[1]
                break

    return rv


if __name__ == '__main__':
    with open('data/input02.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(checksum_evenly_divisible(lines))
