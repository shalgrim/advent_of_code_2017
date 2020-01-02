def find_garbage_end(s):
    """Returns number of chars to skip to get to end of garbage"""
    canceled = False
    for i, c in enumerate(s):
        if canceled:
            canceled = False
            continue
        if c == '>' and not canceled:
            return i + 1
        if c == '!':
            canceled = True


def count_groups(s):
    count = 0
    chars_to_skip = 0
    for i, c in enumerate(s):
        if chars_to_skip:
            chars_to_skip -= 1
        elif c == '{':
            count += 1
        elif c == '<':
            chars_to_skip = find_garbage_end(s[i+1:])

    return count


def find_group_end(s):
    open_count = 1
    chars_to_skip = 0
    garbage_skip = 0
    canceled = False

    while open_count:
        chars_to_skip += 1
        if garbage_skip:
            garbage_skip -= 1
            continue

        if canceled:
            canceled = False
        elif s[chars_to_skip] == '!':
            canceled = True
        elif s[chars_to_skip] == '}':
            open_count -= 1
        elif s[chars_to_skip] == '{':
            open_count += 1
        elif s[chars_to_skip] == '<':
            garbage_skip = find_garbage_end(s[chars_to_skip+1:])

    return chars_to_skip


def score_groups(s, outer_score=0):
    assert s[0] == '{'
    assert s[-1] == '}'

    this_score = outer_score + 1
    tracking_score = this_score
    chars_to_skip = 1
    canceled = False

    for i, c in enumerate(s):
        if chars_to_skip:
            chars_to_skip -= 1
        elif canceled:
            canceled = False
        elif c == '!' and not canceled:
            canceled = True
        elif c == '{' and not canceled:
            chars_to_skip = find_group_end(s[i:]) + 1
            tracking_score += score_groups(s[i:i + chars_to_skip], this_score)
        elif c == '<' and not canceled:
            chars_to_skip = find_garbage_end(s[i+1:])

    return tracking_score


if __name__ == '__main__':
    with open('data/input09.txt') as f:
        content = f.read().strip()

    print(score_groups(content))
