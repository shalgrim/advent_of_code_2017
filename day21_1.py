from copy import copy

START_GRID = '.#./..#/###'


def line_to_grid(gridline):
    return gridline.split('/')


def grid_to_line(grid):
    return '/'.join(grid)


def flip(line):
    return '/'.join([s[::-1] for s in line.split('/')])


def rotate(line):
    if len(line) == 5:
        return line[3] + line[0] + '/' + line[4] + line[1]
    else:
        return f'{line[8]}{line[4]}{line[0]}/{line[9]}{line[5]}{line[1]}/{line[10]}{line[6]}{line[2]}'


def find_rule_by_rotating(line, rules):
    line = copy(line)
    for _ in range(4):
        if line in rules:
            return rules[line]
        line = rotate(line)
    return None


def find_rule(ingridline, rules):
    assert len(ingridline) in (
        5,
        11,
    ), f'{ingridline=} of wrong length to match any rule'

    gridline = copy(ingridline)
    if answer := find_rule_by_rotating(gridline, rules):
        return answer
    else:
        return find_rule_by_rotating(flip(gridline), rules)


def iterate(gridline, rules):
    first_slash = gridline.index('/')
    grid = line_to_grid(gridline)
    newgrid = []
    if first_slash % 2 == 0:
        for y in range(0, len(grid[0]), 2):
            newgrid += ['', '', '']
            for x in range(0, len(grid[0]), 2):
                subsquare = [grid[y][x : x + 2], grid[y + 1][x : x + 2]]
                lhs = grid_to_line(subsquare)
                rhs = find_rule(lhs, rules)
                new_subsquare = line_to_grid(rhs)
                for yoffset, nss in enumerate(new_subsquare):
                    newgrid[-3 + yoffset] += nss
    else:
        assert first_slash % 3 == 0, f'{gridline=} not divisible by 2 or 3'
        for y in range(0, len(grid[0]), 3):
            newgrid += ['', '', '', '']
            for x in range(0, len(grid[0]), 3):
                subsquare = [
                    grid[y][x : x + 3],
                    grid[y + 1][x : x + 3],
                    grid[y + 2][x : x + 3],
                ]
                lhs = grid_to_line(subsquare)
                rhs = find_rule(lhs, rules)
                new_subsquare = line_to_grid(rhs)
                for yoffset, nss in enumerate(new_subsquare):
                    newgrid[-4 + yoffset] += nss

    return newgrid


def main(rules, num_iterations):
    grid = iterate(START_GRID, rules)
    for _ in range(num_iterations-1):
        gridline = grid_to_line(grid)
        grid = iterate(gridline, rules)

    gridline = grid_to_line(grid)
    return gridline.count('#')


def get_rules_from_file(filename):
    with open('data/input21.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    rules = {}
    for line in lines:
        lhs, rhs = line.split(' => ')
        rules[lhs] = rhs
    return rules


if __name__ == '__main__':
    rules = get_rules_from_file('data/input21.txt')
    print(main(rules, 5))
