from collections import Counter


def is_valid(phrase):
    counters = [Counter(p) for p in phrase.split()]
    hashable_counters = [tuple(sorted([(k, v) for k, v in c.items()])) for c in counters]
    return len(hashable_counters) == len(set(hashable_counters))


if __name__ == '__main__':
    with open('data/input04.txt') as f:
        phrases = [line.strip() for line in f.readlines()]
    print(sum([is_valid(phrase) for phrase in phrases]))
