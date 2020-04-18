from collections import defaultdict


def create_pipes(lines):
    splits = [line.split('<->') for line in lines]
    assert all([',' not in s[0] for s in splits])  # assert lhs of every rule is one program
    pipes = defaultdict(set)

    for split in splits:
        l = split[0].strip()
        rs = [sub.strip() for sub in split[1].strip().split(',')]

        for r in rs:
            pipes[l].add(r)
            pipes[r].add(l)

    return pipes


def get_visitable_programs(pipes, program, visited=None):
    if visited is None:
        visited = set([program])
    else:
        visited.add(program)

    for neighbor in pipes[program]:
        if neighbor in visited:
            continue
        visited.update(get_visitable_programs(pipes, neighbor, visited))

    return visited


def main(lines, program):
    pipes = create_pipes(lines)
    return len(get_visitable_programs(pipes, program))


if __name__ == '__main__':
    with open('./data/input12.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines, '0'))