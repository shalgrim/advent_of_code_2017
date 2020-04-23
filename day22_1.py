NUM_TICKS = 10000


def turn(initial_direction, right_or_left):
    if right_or_left == 1 and initial_direction == 3:
        return 0
    if right_or_left == -1 and initial_direction == 0:
        return 3
    else:
        return initial_direction + right_or_left


def move(lines, location, direction):
    x, y = location
    linelen = len(lines[0])
    if direction == 0:
        if y == 0:
            newlines = ['.' * linelen] + lines
            newloc = location
        else:
            newlines = lines
            newloc = x, y - 1
    elif direction == 1:
        if x == linelen - 1:
            newlines = []
            for line in lines:
                newlines.append(line + '.')
        else:
            newlines = lines
        newloc = x + 1, y
    elif direction == 2:
        if y == len(lines) - 1:
            newlines = lines + ['.' * linelen]
        else:
            newlines = lines
        newloc = x, y + 1
    elif direction == 3:
        if x == 0:
            newlines = []
            for line in lines:
                newlines.append('.' + line)
            newloc = location
        else:
            newlines = lines
            newloc = x - 1, y

    return newlines, newloc


def show_map(lines, location):
    lines_to_print = []
    for y, line in enumerate(lines):
        if y == location[1]:
            newline = line[: location[0]] + '*' + line[location[0] + 1 :]
            lines_to_print.append(newline)
        else:
            lines_to_print.append(line)

    print('\n'.join(lines_to_print))


def tick(lines, location, initial_direction):
    x, y = location
    if lines[y][x] == '#':
        final_direction = turn(initial_direction, 1)
        replace_char = '.'
        did_infect = 0
    else:
        final_direction = turn(initial_direction, -1)
        replace_char = '#'
        did_infect = 1

    lines[y] = lines[y][:x] + replace_char + lines[y][x + 1 :]
    lines, final_location = move(lines, location, final_direction)

    return lines, final_location, final_direction, did_infect


def main(lines, num_ticks=NUM_TICKS):
    location = initalize_location(lines)
    direction = 0
    infection_ticks = 0

    for underscore in range(num_ticks):
        lines, location, direction, did_infect = tick(lines, location, direction)
        infection_ticks += did_infect

    return infection_ticks


def initalize_location(lines):
    assert len(lines) % 2 == 1
    assert len(lines[0]) % 2 == 1
    midy = len(lines) // 2
    midx = len(lines[0]) // 2
    location = midx, midy

    return location


if __name__ == '__main__':
    with open('data/input22.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'{main(lines)=}')
