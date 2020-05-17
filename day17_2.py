import logging
import sys
from logging import StreamHandler

logger = logging.getLogger('advent_of_code_2017.day17_2')
logging.basicConfig(filename='day17_2.log',
                    level=logging.INFO,
                    format='%(levelname) -10s %(asctime)s %(module)s at line %(lineno)d: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger.addHandler(StreamHandler(sys.stdout))


def get_next(x, num_steps):
    """x is at position 1, list is x+1 long"""
    location = (num_steps + 1) % (x+1) + 1

    while location != 1:
        x += 1
        location = (num_steps + location) % (x + 1) + 1

    return x + 1


def main_v2(num_steps):
    prev_x = 0
    curr_x = 1
    while curr_x < 50_000_000:
        prev_x = curr_x
        curr_x = get_next(curr_x, num_steps)
        print(f'{curr_x=}')

    return prev_x


def main(num_steps):
    buffer = [0]
    location = 0
    zero_index = 0

    for i in range(1, 50_000_000):
        location = (location + num_steps) % len(buffer)
        buffer.insert(location + 1, i)
        location += 1
        assert buffer[location] == i
        zero_index = buffer.index(0)
        logger.debug(f'inserted value {i=} at location {location=}; {len(buffer)=}; {zero_index=}')
        if location == zero_index + 1:
            logger.info(f'NEW VALUE {i} AFTER 0')
            continue  # only here for breakpoint

    zero_index = buffer.index(0)

    return buffer[zero_index - 1]


if __name__ == '__main__':
    # print(main(386))
    print(main_v2(386))
