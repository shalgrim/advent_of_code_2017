from collections import defaultdict


class Runner(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.iptr = 0
        self.registers = defaultdict(lambda: 0)
        self.num_muls = 0

    def run_instruction(self):
        instruction = self.instructions[self.iptr]
        cmd, x, y = instruction
        iptr_incr = 1

        if cmd == 'set':
            self.registers[x] = y if isinstance(y, int) else self.registers[y]
        elif cmd == 'sub':
            self.registers[x] -= y if isinstance(y, int) else self.registers[y]
        elif cmd == 'mul':
            self.registers[x] *= y if isinstance(y, int) else self.registers[y]
            self.num_muls += 1
        elif cmd == 'jnz':
            ofinterest = x if isinstance(x, int) else self.registers[x]
            if ofinterest != 0:
                iptr_incr = y if isinstance(y, int) else self.registers[y]

        return iptr_incr

    def run(self):
        while 0 <= self.iptr < len(self.instructions):
            self.iptr += self.run_instruction()


def clean_instructions(instructions):
    for instruction in instructions:
        for i, part in enumerate(instruction):
            try:
                instruction[i] = int(part)
            except ValueError:
                continue

    return instructions


if __name__ == '__main__':
    with open('data/input23.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    instructions = [line.split() for line in lines]
    instructions = clean_instructions(instructions)
    runner = Runner(instructions)
    runner.run()
    print(runner.num_muls)  # 0 is incorrect, unsurprisingly
