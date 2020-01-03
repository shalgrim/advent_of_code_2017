from day09_1 import find_garbage_end


def count_uncanceled_chars(s):
    assert s[0] == '<' and s[-1] == '>', 'bad assumption'
    count = 0
    canceled = False
    for c in s[1:-1]:
        if canceled:
            canceled = False
        elif c == '!':
            canceled = True
        else:
            count += 1
    return count


def count_garbage(s):
    count = 0
    garbage_skip = 0

    for i, c in enumerate(s):
        if garbage_skip:
            garbage_skip -= 1
        elif c == '<':
            garbage_start = i
            garbage_skip = find_garbage_end(s[i:])
            count += count_uncanceled_chars(s[i:i+garbage_skip])

    return count


if __name__ == '__main__':
    with open('data/input09.txt') as f:
        content = f.read().strip()

    print(count_garbage(content))
