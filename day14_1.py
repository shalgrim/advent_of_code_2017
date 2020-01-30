from day10_2 import main as knot_hash


def bitify(hash_string):
    intval = int(hash_string, 16)
    as_binary = bin(intval)
    binary_part = as_binary[2:]
    missing_zeros = 128 - len(binary_part)
    answer = '0' * missing_zeros + binary_part
    return answer


def make_grid(instring):
    grid = []
    for i in range(128):
        hash_input = f'{instring}-{i}'
        hash_output = knot_hash(hash_input)
        bitstring = bitify(hash_output)
        grid.append(bitstring)

    return grid


def get_used_squares(instring):
    grid = make_grid(instring)
    return get_kind_squares(grid, 1)


def get_kind_squares(grid, square_type):
    used_squares = 0
    for row in grid:
        used_squares += sum([int(c) for c in row])
    if square_type == 1:
        return used_squares
    else:
        return len(grid) * len(grid[0]) - used_squares


if __name__ == '__main__':
    print(get_used_squares('ffayrhll'))
