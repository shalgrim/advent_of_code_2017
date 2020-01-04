from copy import copy

from day10_1 import hash_string

SUFFIX = [17, 31, 73, 47, 23]


def run_rounds(start_lengths, num_rounds=64):
    pos = 0
    skip_size = 0
    original_lengths = copy(start_lengths)
    the_input = list(range(256))
    for _ in range(num_rounds):
        working_lengths = copy(original_lengths)
        the_input, pos, skip_size = hash_string(the_input, working_lengths, pos, skip_size)

    return the_input


def densify(elements):
    answer = elements[0] ^ elements[1]
    for i in range(2, 16):
        answer ^= elements[i]

    return answer


def format_dense_hash(dense_hash):
    answer = ''
    for dh in dense_hash:
        answer += hex(dh)[-2:]

    return answer.replace('x', '0')


def main(content):
    byte_string = [ord(c) for c in content]
    byte_string += SUFFIX
    sparse_hash = run_rounds(byte_string)
    assert len(sparse_hash) == 16 * 16
    dense_hash = []
    for i in range(16):
        dense_hash.append(densify(sparse_hash[i * 16:(i + 1) * 16]))
    answer = format_dense_hash(dense_hash)
    assert len(answer) == 32
    return answer


if __name__ == '__main__':
    with open('data/input10.txt') as f:
        content = f.read().strip()
    print(main(content))
    # £OýÕ³ö²\':åÎ»w is not correct
    # a34ffdd58ab3f6b25c273ae5cebb1f77 is not correct
    # aac53f3dc43bd41f3c7e5f4498659a67 is not correct
