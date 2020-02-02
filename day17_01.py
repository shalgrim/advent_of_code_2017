def main(num_steps):
    buffer = [0]
    location = 0

    for i in range(1, 2018):
        location = (location + num_steps) % len(buffer)
        buffer.insert(location + 1, i)
        location += 1
        assert buffer[location] == i

    return buffer[location + 1]


if __name__ == '__main__':
    print(main(386))
