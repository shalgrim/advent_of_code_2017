import re
from collections import defaultdict


def process_instruction(instruction):
    tokens = instruction.split()
    reg_to_update = tokens[0]
    operation = tokens[1]
    amount = tokens[2]
    reg_to_check = tokens[4]
    condition = tokens[5]
    value = tokens[6]
    return reg_to_update, operation, amount, reg_to_check, condition, value


def matches(condition, registers, reg_to_check, value):
    if condition == '==' and registers[reg_to_check] == value:
        return True
    elif condition == '<=' and registers[reg_to_check] <= value:
        return True
    elif condition == '>=' and registers[reg_to_check] >= value:
        return True
    elif condition == '!=' and registers[reg_to_check] != value:
        return True
    elif condition == '<' and registers[reg_to_check] < value:
        return True
    elif condition == '>' and registers[reg_to_check] > value:
        return True
    return False


def run_program(instructions):
    registers = defaultdict(lambda: 0)

    for instruction in instructions:
        (
            reg_to_update,
            operation,
            amount,
            reg_to_check,
            condition,
            value,
        ) = process_instruction(instruction)

        if matches(condition, registers, reg_to_check, int(value)):
            if operation == 'inc':
                registers[reg_to_update] += int(amount)
            else:
                registers[reg_to_update] -= int(amount)

    return registers


if __name__ == '__main__':
    with open('data/input08.txt') as f:
        instructions = [line.strip() for line in f.readlines()]

    registers = run_program(instructions)
    print(max(registers.values()))
