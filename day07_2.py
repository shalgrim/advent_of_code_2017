import re

from day07_1 import get_bottom_program, get_supports

WEIGHT_PATT = re.compile('\d+')


def get_individual_weights(lines):
    rv = {}

    for line in lines:
        disc_name = line.split()[0]
        disc_weight = int(WEIGHT_PATT.search(line).group(0))
        rv[disc_name] = disc_weight

    return rv


def find_unbalanced_disc(support_dict, weight_dict, start_program):
    supported = support_dict[start_program]

    if not supported:
        return weight_dict[start_program]

    weights = [
        find_unbalanced_disc(support_dict, weight_dict, program) for program in supported
    ]

    if min(weights) == max(weights):
        return weight_dict[start_program] + sum(weights)
    else:
        raise Exception(f'{start_program=}, {weights=}')


def get_unbalanced_program(lines):
    support_dict = get_supports(lines)
    weight_dict = get_individual_weights(lines)
    bottom_program = get_bottom_program(lines)
    return find_unbalanced_disc(support_dict, weight_dict, bottom_program)


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(get_unbalanced_program(lines))
