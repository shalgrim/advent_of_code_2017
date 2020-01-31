def spin(data, programs):
    cycle = -int(data)
    programs = programs[cycle:] + programs[:cycle]


def partner(data, programs):
    p1, p2 = data.split('/')
    i1 = programs.index(p1)
    i2 = programs.index(p2)
    tmp = programs[i2]
    programs[i2] = programs[i1]
    programs[i1] = tmp


def exchange(data, programs):
    i1, i2 = [int(d) for d in data.split('/')]
    tmp = programs[i2]
    programs[i2] = programs[i1]
    programs[i1] = tmp


PROGRAMS = {
    'x': exchange,
    'p': partner,
    's': spin,
}


def run_program(instructions, programs):
    for instruction in instructions:
        program = instruction[0]
        data = instruction[1:]
        PROGRAMS[program](data, programs)


if __name__ == '__main__':
    with open('./data/input16.txt') as f:
        content = f.read()

    instructions = content.split(',')
    programs = [chr(i) for i in range(97, 97+16)]
    run_program(instructions, programs)
    print(''.join(programs))  # pbglcmjfedhanoik is not right
