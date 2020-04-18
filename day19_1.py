from enum import Enum, auto


class Direction(Enum):
    DOWN = auto()
    LEFT = auto()
    UP = auto()
    RIGHT =  auto()


def get_starting_x(line):
    return line.index('|')


def move(lines, x, y, direction):
    if direction == Direction.DOWN:
        if y == len(lines) - 1:
            return x, y, Direction.DOWN, ''
        elif lines[y+1][x] == '|':
            return x, y+1, Direction.DOWN, ''
        elif lines[y+1][x] == '+':
            if lines[y+1][x-1] in ('+', '-'):
                return x, y+1, Direction.LEFT
            elif lines[y+1][x+1] in ('+', '-'):
                return x, y+1, Direction.RIGHT
            else:
                raise Exception(f'should I turn right or left here? {x=} {y=} {direction=}')
        elif lines[y+1][x] == '-':
            return x, y+1, Direction.DOWN, ''
        elif ord('A') <= ord(lines[y+1][x]) <= ord('Z'):
            return x, y+1, Direction.DOWN, lines[y+1][x]
        else:
            raise Exception(f'did not expect to be here {x=} {y=} {direction=}')
    else:
        raise NotImplementedError(f'Not Implemented yet {x=} {y=} {direction=}')


def get_letters_on_path(lines):
    y = 0
    x = get_starting_x(lines[0])
    direction = Direction.DOWN
    new_x, new_y = None
    answer = ''

    while (x, y) != (new_x, new_y):
        x, y = new_x, new_y
        new_x, new_y, direction, letter = move(lines, x, y, direction)
        answer += letter

    return answer


if __name__ == '__main__':
    with open('data/input19.txt') as f:
        lines = [line[:-1] for line in f.readlines()]
    print(get_letters_on_path(lines))
