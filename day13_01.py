class Scanner(object):
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.location = 0
        self.descending = True

    def __repr__(self):
        return f'{self.location=}, {self.descending=}, {self.range=}, {self.depth=}'

    def tick(self):
        if self.descending:
            self.location += 1

            if self.location + 1 == self.range:
                self.descending = False
        else:
            self.location -= 1

            if self.location == 0:
                self.descending = True

def build_scanners(lines):
    scanners = []

    for line in lines:
        depth = int(line.split(':')[0].strip())
        range = int(line.split(':')[1].strip())
        scanners.append(Scanner(depth, range))

    return scanners


def calculate_penalty_helper(lines, scanners):
    firewall_length = max([s.depth for s in scanners]) + 1
    location = -1
    penalty = 0

    while location < firewall_length:
        location += 1
        for scanner in scanners:
            if scanner.depth == location and scanner.location == 0:
                penalty += scanner.depth * scanner.range
            scanner.tick()

    return penalty


def calculate_penalty(lines):
    scanners = build_scanners(lines)
    return calculate_penalty_helper(lines, scanners)


if __name__ == '__main__':
    with open('./data/input13.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(calculate_penalty(lines))
