from day12_01 import create_pipes
from day12_01 import get_visitable_programs


def get_num_groups(lines):
    pipes = create_pipes(lines)
    groups = []
    grouped_programs = set()

    while len(grouped_programs) < len(pipes):
        ungrouped_programs = set(pipes.keys()).difference(grouped_programs)
        program = ungrouped_programs.pop()
        group = get_visitable_programs(pipes, program)
        groups.append(group)
        grouped_programs.update(set(group))

    return len(groups)


if __name__ == '__main__':
    with open('./data/input12.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(get_num_groups(lines))
