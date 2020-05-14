from collections import Counter


def do_easy_cancels(counter, d1, d2):
    big = d1 if counter[d1] > counter[d2] else d2
    little = d1 if big == d2 else d2
    counter[big] -= counter[little]
    counter[little] = 0


def do_hard_cancel(counter):
    leftovers = [k for k in counter.keys() if counter[k]]

    if 's' in leftovers:
        if 'nw' and 'sw' in leftovers:
            if counter['nw'] < counter['s'] and counter['nw'] < counter['sw']:
                counter['s'] -= counter['nw']
                counter['sw'] += counter['nw']
                counter['nw'] -= counter['nw']


def main():
    with open('data/input11.txt') as f:
        content = f.read().strip()
    directions = content.split(',')
    return get_final_steps_away(directions)


def get_final_steps_away(directions):
    counter = Counter(directions)
    do_easy_cancels(counter, 'n', 's')
    do_easy_cancels(counter, 'ne', 'sw')
    do_easy_cancels(counter, 'nw', 'se')
    do_hard_cancel(counter)
    return sum(counter.values())


if __name__ == '__main__':
    print(main())
