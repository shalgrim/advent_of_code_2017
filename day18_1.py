import sys
from collections import defaultdict


last_played = None


def run_instruction(instruction, registers):
    global last_played

    if instruction[0] == 'snd':
        last_played = registers[instruction[1]]
    elif instruction[0] == 'set':
        val = instruction[2] if isinstance(instruction[2], int) else registers[instruction[2]]
        registers[instruction[1]] = val
    elif instruction[0] == 'add':
        val = instruction[2] if isinstance(instruction[2], int) else registers[instruction[2]]
        registers[instruction[1]] += val
    elif instruction[0] == 'mul':
        val = instruction[2] if isinstance(instruction[2], int) else registers[instruction[2]]
        registers[instruction[1]] *= val
    elif instruction[0] == 'mod':
        val = instruction[2] if isinstance(instruction[2], int) else registers[instruction[2]]
        registers[instruction[1]] %= val
    elif instruction[0] == 'rcv':
        if registers[instruction[1]] != 0:
            print(f'{last_played=}')
            sys.exit()
    elif instruction[0] == 'jgz':
        if registers[instruction[1]] > 0:
            return instruction[2] if isinstance(instruction[2], int) else registers[instruction[2]]
    return 1


def main(instructions):
    registers = defaultdict(lambda: 0)
    instruction_pointer = 0
    instruction = instructions[instruction_pointer]
    global last_played
    last_played = None

    while 0 <= instruction_pointer < len(instructions):
        jump = run_instruction(instruction, registers)
        instruction_pointer += jump
        instruction = instructions[instruction_pointer]

    return last_played


if __name__ == '__main__':
    with open('data/input18.txt') as f:
        instructions = [line.strip().split() for line in f.readlines()]

    for instruction in instructions:
        for i, part in enumerate(instruction):
            try:
                instruction[i] = int(part)
            except ValueError:
                continue

    main(instructions)
