def checksum(lines):
    grid = [line.split() for line in lines]
    rv = 0
    for line in grid:
        nums = [int(n) for n in line]
        rv += max(nums) - min(nums)

    return rv


if __name__ == '__main__':
    with open('data/input02.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(checksum(lines))
