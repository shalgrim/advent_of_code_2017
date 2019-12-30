def hashify(memory):
    return ','.join([str(count) for count in memory])


def select_bank(memory):
    most = max(memory)
    first_index = memory.index(most)
    return first_index


def reallocate(memory, bank):
    pile = memory[bank]
    current = bank
    memory[bank] = 0

    while pile:
        current = (current + 1) % len(memory)
        memory[current] += 1
        pile -= 1


def main(memory):
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
