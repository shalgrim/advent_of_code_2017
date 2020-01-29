from day10_2 import main as knot_hash


def bitify(hash_string):
    raise NotImplementedError


def make_grid(instring):
    grid = []
    for i in range(128):
        hash_input = f'{instring}-{i}'
        hash_output = knot_hash(hash_input)
        bitstring = bitify(hash_output)
        grid.append(bitstring)

    return grid


def get_free_squares(instring):
    grid = make_grid(instring)
    free_squares = 0
    for row in grid:
        ints = [int(c) for c in row]
        free_squares += 128 - sum(ints)

    return free_squares

