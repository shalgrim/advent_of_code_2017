from day06_1 import hashify
from day06_1 import main as part_one
from day06_1 import reallocate, select_bank


def main(memory):
    first_repeated_state = part_one(memory)[1]
    seen_states = set()

    while hashify(memory) not in seen_states:
        seen_states.add(hashify(memory))
        bank = select_bank(memory)
        reallocate(memory, bank)

    return len(seen_states)


if __name__ == '__main__':
    with open('data/input06.txt') as f:
        memory = [int(n) for n in f.read().split()]
    print(main(memory))
