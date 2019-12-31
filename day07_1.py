from collections import defaultdict


def get_supports(lines):
    rv = defaultdict(list)

    for line in lines:
        if '->' in line:
            supporter = line.split()[0]
            supported = line.split('>')[1].strip()
            supported = supported.split(', ')
            rv[supporter] = set(supported)

    return rv


def get_bottom_program(lines):
    support_dict = get_supports(lines)
    all_supported = set()
    for v in support_dict.values():
        all_supported.update(v)

    for k in support_dict.keys():
        if k not in all_supported:
            return k


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(get_bottom_program(lines))
