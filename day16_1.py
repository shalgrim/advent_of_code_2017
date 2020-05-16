from copy import copy


def spin(data, programs):
    cycle = -int(data)
    return programs[cycle:] + programs[:cycle]


def partner(data, programs):
    p1, p2 = data.split('/')
    i1 = programs.index(p1)
    i2 = programs.index(p2)
    tmp = programs[i2]
    programs[i2] = programs[i1]
    programs[i1] = tmp
    return programs


def exchange(data, programs):
    i1, i2 = [int(d) for d in data.split('/')]
    tmp = programs[i2]
    programs[i2] = programs[i1]
    programs[i1] = tmp
    return programs


PROGRAMS = {
    'x': exchange,
    'p': partner,
    's': spin,
}


def run_program(instructions, programs):
    foo_programs = copy(programs)
    for instruction in instructions:
        program = instruction[0]
        data = instruction[1:]
        foo_programs = PROGRAMS[program](data, foo_programs)
    return foo_programs


def run_program_string(instructions, s):
    programs = list(s)
    output = run_program(instructions, programs)
    return ''.join(output)


if __name__ == '__main__':
    with open('./data/input16.txt') as f:
        content = f.read()

    instructions = content.split(',')
    programs = [chr(i) for i in range(97, 97+16)]
    bar_programs = run_program(instructions, programs)
    print(''.join(bar_programs))  # pbglcmjfedhanoik is not right
    print(run_program_string(instructions, ''.join(programs)))
