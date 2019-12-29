def is_valid(phrase):
    return len(phrase.split()) == len(set(phrase.split()))


if __name__ == '__main__':
    with open('data/input04.txt') as f:
        phrases = [line.strip() for line in f.readlines()]
    print(sum([is_valid(phrase) for phrase in phrases]))
