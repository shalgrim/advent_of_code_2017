if __name__ == '__main__':
    with open('data/input05.txt') as f:
        instructions = [int(line.strip()) for line in f.readlines()]

    steps = 0
    ip = 0
    while 0 <= ip < len(instructions):
        steps += 1
        jump = instructions[ip]
        change = 1 if jump < 3 else -1
        instructions[ip] += change
        ip += jump

    print(steps)
