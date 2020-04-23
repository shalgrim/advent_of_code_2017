from day22_1 import initalize_location, turn, move


def tick(lines, location, initial_direction):
    x, y = location
    did_infect = 0
    if lines[y][x] == '#':  # infected
        final_direction = turn(initial_direction, 1)
        replace_char = 'f'
    elif lines[y][x] == 'w':  # weakened
        final_direction = initial_direction
        replace_char = '#'
        did_infect = 1
    elif lines[y][x] == 'f':  # flagged (for cleanup I guess)
        final_direction = (initial_direction + 2) % 4
        replace_char = '.'
    elif lines[y][x] == '.':  # clean
        final_direction = turn(initial_direction, -1)
        replace_char = 'w'
    else:
        raise Exception('wut')

    lines[y] = lines[y][:x] + replace_char + lines[y][x+1:]
    lines, final_location = move(lines, location, final_direction)

    return lines, final_location, final_direction, did_infect


def main(lines, num_ticks=10_000_000):
    location = initalize_location(lines)
    direction = 0
    infection_ticks = 0

    for underscore in range(num_ticks):
        lines, location, direction, did_infect = tick(lines, location, direction)
        infection_ticks += did_infect

    return infection_ticks


if __name__ == '__main__':
    with open('data/input22.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'{main(lines)=}')
