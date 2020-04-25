from copy import deepcopy


class Bridge:
    def __init__(self):
        self.needs = [0]
        self.pipes = []

    def eligible_pipes(self, pipes):
        answer = []
        unused = [p for p in pipes if p not in self.pipes]
        has_need = [p for p in unused if self.needs[-1] in (p.e1, p.e2)]
        return has_need

    def attach(self, pipe):
        assert self.needs[-1] in [pipe.e1, pipe.e2], "Can't attach this pipe according to needs"
        assert pipe not in self.pipes, 'This pipe already in bridge'
        self.pipes.append(pipe)
        if pipe.e1 == pipe.e2:
            self.needs.append(pipe.e1)
        else:
            ends = set([pipe.e1, pipe.e2])
            used = set([self.needs[-1]])
            self.needs.append(ends.difference(used).pop())

    @property
    def value(self):
        return sum(p.value for p in self.pipes)


class Pipe:
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    @property
    def value(self):
        return self.e1 + self.e2


def lines_to_pipes(lines):
    splits = [line.split('/') for line in lines]
    intsplits = [[int(s1) for s1 in s] for s in splits]

    pipes = {}

    for i, numbers in enumerate(intsplits):
        pipes[i] = Pipe(*numbers)

    return pipes


def extend_bridges(bridges, pipes):
    new_bridges = []

    for b in bridges:
        eligible_pipes = b.eligible_pipes(pipes.values())
        for ep in eligible_pipes:
            newb = deepcopy(b)
            newb.attach(ep)
            new_bridges.append(newb)

    return new_bridges


def main(lines):
    pipes = lines_to_pipes(lines)
    bridges = [Bridge()]
    new_bridges = extend_bridges(bridges, pipes)

    while not new_bridges:
        bridges += new_bridges
        new_bridges = extend_bridges(new_bridges, pipes)

    return max(b.value for b in bridges)


if __name__ == '__main__':
    with open('data/input24.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))