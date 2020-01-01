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


def find_group_end(param):
    return 1


def score_groups(s, outer_score=0):
    assert s[0] == '{'
    assert s[-1] == '}'

    this_score = outer_score + 1
    tracking_score = this_score
    chars_to_skip = 1

    for i, c in enumerate(s):
        if chars_to_skip:
            chars_to_skip -= 1
        elif c == '{':
            chars_to_skip = find_group_end(s[i:])
            tracking_score += score_groups(s[i:i + chars_to_skip])

    return this_score


