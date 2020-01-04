def hash_string(string_length, twist_lengths, start_pos=0, start_skip_size=0):
    curr_pos = start_pos
    skip_size = start_skip_size
    if isinstance(string_length, list):
        the_string = string_length
    else:
        the_string = list(range(string_length))

    for tl in twist_lengths:
        assert tl <= len(the_string), 'this should continue instead of failing'

        reverse_start = curr_pos
        reverse_stop = curr_pos + tl

        if reverse_stop <= len(the_string):
            the_string[reverse_start:reverse_stop] = reversed(the_string[reverse_start:reverse_stop])
        else:
            leftover = reverse_stop - len(the_string)
            string_to_reverse = the_string[reverse_start:] + the_string[:leftover]
            assert len(string_to_reverse) == tl
            reversed_string = list(reversed(string_to_reverse))
            the_string[reverse_start:] = reversed_string[:tl - leftover]
            the_string[:leftover] = reversed_string[tl-leftover:]
        assert len(the_string) == len(the_string)

        curr_pos = (curr_pos + tl + skip_size) % len(the_string)
        skip_size += 1

    return the_string, curr_pos, skip_size


if __name__ == '__main__':
    with open('data/input10.txt') as f:
        content = f.read().strip()
    the_string = [int(n) for n in content.split(',')]
    processed = hash_string(256, the_string)[0]
    print(processed[0] * processed[1])
