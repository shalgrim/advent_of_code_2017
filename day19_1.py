import logging
import sys
from enum import Enum, auto
from logging import StreamHandler

logger = logging.getLogger('advent_ov_code_2017.day19_1')
logging.basicConfig(
    filename='day19_1.log',
    level=logging.DEBUG,
    format='%(levelname) -10s %(asctime)s %(module)s at line %(lineno)d: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger.addHandler(StreamHandler(sys.stdout))


class Direction(Enum):
    DOWN = auto()
    LEFT = auto()
    UP = auto()
    RIGHT = auto()


def get_starting_x(line):
    return line.index('|')


def move(lines, x, y, direction):
    if direction == Direction.DOWN:
        if y == len(lines) - 1:
            return x, y, Direction.DOWN, ''
        elif lines[y + 1][x] in ('|', '-'):
            return x, y + 1, Direction.DOWN, ''
        elif lines[y + 1][x] == '+':
            if x == 0:
                return x, y + 1, Direction.RIGHT, ''
            elif x == len(lines[y + 1]) - 1:
                return x, y + 1, Direction.LEFT, ''
            elif lines[y + 1][x - 1] in ('+', '-') or ord('A') <= ord(
                lines[y + 1][x - 1]
            ) <= ord('Z'):
                return x, y + 1, Direction.LEFT, ''
            elif lines[y + 1][x + 1] in ('+', '-') or ord('A') <= ord(
                lines[y + 1][x + 1]
            ) <= ord('Z'):
                return x, y + 1, Direction.RIGHT, ''
            else:
                raise Exception(
                    f'should I turn right or left here? {x=} {y=} {direction=}'
                )
        elif ord('A') <= ord(lines[y + 1][x]) <= ord('Z'):
            return x, y + 1, Direction.DOWN, lines[y + 1][x]
        else:
            return x, y, Direction.DOWN, ''
    elif direction == Direction.UP:
        if y == 0:
            return x, y, Direction.UP, ''
        elif lines[y - 1][x] in ('|', '-'):
            return x, y - 1, Direction.UP, ''
        elif lines[y - 1][x] == '+':
            if x == 0:
                return x, y - 1, Direction.RIGHT, ''
            elif x == len(lines[y - 1]) - 1:
                return x, y - 1, Direction.LEFT, ''
            if lines[y - 1][x - 1] in ('+', '-') or ord('A') <= ord(
                lines[y - 1][x - 1]
            ) <= ord('Z'):
                return x, y - 1, Direction.LEFT, ''
            elif lines[y - 1][x + 1] in ('+', '-') or ord('A') <= ord(
                lines[y - 1][x + 1]
            ) <= ord('Z'):
                return x, y - 1, Direction.RIGHT, ''
            else:
                raise Exception(
                    f'should I turn right or left here? {x=} {y=} {direction=}'
                )
        elif ord('A') <= ord(lines[y - 1][x]) <= ord('Z'):
            return x, y - 1, Direction.UP, lines[y - 1][x]
        else:
            return x, y, Direction.UP, ''

    elif direction == Direction.RIGHT:
        if x == len(lines[y]) - 1:
            return x, y, Direction.RIGHT, ''
        elif lines[y][x + 1] in ('|', '-'):
            return x + 1, y, Direction.RIGHT, ''
        elif lines[y][x + 1] == '+':
            if y == len(lines) - 1 or x >= len(lines[y + 1]):
                return x + 1, y, Direction.UP, ''
            elif y == 0 or x >= len(lines[y - 1]):
                return x + 1, y, Direction.DOWN, ''
            elif lines[y - 1][x + 1] in ('+', '|') or ord('A') <= ord(
                lines[y - 1][x + 1]
            ) <= ord('Z'):
                return x + 1, y, Direction.UP, ''
            elif lines[y + 1][x + 1] in ('+', '|') or ord('A') <= ord(
                lines[y + 1][x + 1]
            ) <= ord('Z'):
                return x + 1, y, Direction.DOWN, ''
            else:
                raise Exception(
                    f'should I turn right or left here? {x=} {y=} {direction=}'
                )
        elif ord('A') <= ord(lines[y][x + 1]) <= ord('Z'):
            return x + 1, y, Direction.RIGHT, lines[y][x + 1]
        else:
            return x, y, Direction.RIGHT, ''

    elif direction == Direction.LEFT:
        if x == 0:
            return x, y, Direction.LEFT, ''
        elif lines[y][x - 1] in ('|', '-'):
            return x - 1, y, Direction.LEFT, ''
        elif lines[y][x - 1] == '+':
            if y == len(lines) - 1 or x >= len(lines[y + 1]):
                return x - 1, y, Direction.UP, ''
            elif y == 0 or x >= len(lines[y - 1]):
                return x - 1, y, Direction.DOWN, ''
            elif lines[y + 1][x - 1] in ('+', '|') or ord('A') <= ord(
                lines[y + 1][x - 1]
            ) <= ord('Z'):
                return x - 1, y, Direction.DOWN, ''
            elif lines[y - 1][x - 1] in ('+', '|') or ord('A') <= ord(
                lines[y - 1][x - 1]
            ) <= ord('Z'):
                return x - 1, y, Direction.UP, ''
            else:
                raise Exception(
                    f'should I turn right or left here? {x=} {y=} {direction=}'
                )
        elif ord('A') <= ord(lines[y][x - 1]) <= ord('Z'):
            return x - 1, y, Direction.LEFT, lines[y][x - 1]
        else:
            return x, y, Direction.LEFT, ''

    else:
        raise Exception(f'Unexpected {x=} {y=} {direction=}')


def get_letters_on_path(lines):
    y = 0
    x = get_starting_x(lines[0])
    direction = Direction.DOWN
    logger.debug(f'{x=}, {y=}, {direction=}')
    new_x, new_y, direction, letter = move(lines, x, y, direction)
    answer = letter

    while (x, y) != (new_x, new_y):
        x, y = new_x, new_y
        logger.debug(f'{x=}, {y=}, {direction=}')
        new_x, new_y, direction, letter = move(lines, x, y, direction)
        answer += letter

    return answer


if __name__ == '__main__':
    with open('data/input19.txt') as f:
        lines = [line[:-1] for line in f.readlines()]
    print(get_letters_on_path(lines))
