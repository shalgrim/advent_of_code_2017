def main(num_steps):
    buffer = [0]
    location = 0

    for i in range(1, 2018):
        new_location = (location + num_steps) % len(buffer)
        buffer.insert(new_location + 1, i)
        new_location += 1
        assert buffer[new_location] == i

    return buffer[new_location + 1]


if __name__ == '__main__':
    print(main(386))
