from collections import defaultdict

from day18_1 import run_instruction as ri1, clean_instructions


class Program(object):
    def __init__(self, instructions, pid):
        self.registers = defaultdict(lambda: 0)
        self.pid = pid
        self.registers['p'] = pid
        self.iptr = 0
        self.instructions = instructions
        self.partner = None
        self.inbox = []
        self.num_sent = 0
        self.waitflag = False

    @property
    def waiting(self):
        return self.waitflag and not self.inbox

    @property
    def finished(self):
        return self.iptr < 0 or self.iptr >= len(self.instructions)

    def run_instruction(self, instruction):
        if instruction[0] == 'snd':
            self.partner.inbox.append(self.registers[instruction[1]])
            # print(f'pid {self.pid} sending')
            self.num_sent += 1
            return 1
        elif instruction[0] == 'rcv':
            try:
                self.registers[instruction[1]] = self.inbox.pop(0)
            except IndexError:
                self.waitflag = True
                # print(f'pid {self.pid} unable to receive')
                return 0
            else:
                # print(f'pid {self.pid} receiving')
                self.waitflag = False
                return 1
        else:
            return ri1(instruction, self.registers)

    def tick(self):
        # print(f'{self.pid=}', f'{self.iptr=}')
        if 0 <= self.iptr < len(self.instructions):
            instruction = self.instructions[self.iptr]
            self.iptr += self.run_instruction(instruction)
        else:
            self.finished = True


def done_or_deadlock(p1, p2):
    if (p1.waiting or p1.finished) and (p2.waiting or p2.finished):
        return True
    return False


def main(instructions):
    p0 = Program(instructions, 0)
    p1 = Program(instructions, 1)
    p0.partner = p1
    p1.partner = p0

    while not done_or_deadlock(p0, p1):
        print(f'{p1.num_sent=}')
        while not (p0.waiting or p0.finished):
            p0.tick()

        print(f'{p0.num_sent=}')
        while not (p1.waiting or p1.finished):
            p1.tick()

    return p1.num_sent


if __name__ == '__main__':
    with open('data/input18.txt') as f:
        instructions = [line.strip().split() for line in f.readlines()]
    clean_instructions(instructions)
    print(main(instructions))
