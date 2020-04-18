def main(num_steps):
    buffer = [0]
    location = 0

    for i in range(1, 50_000_000):
        location = (location + num_steps) % len(buffer)
        buffer.insert(location + 1, i)
        location += 1
        assert buffer[location] == i

    zero_index = buffer.index(0)

    return buffer[zero_index - 1]


if __name__ == '__main__':
    print(main(386))
