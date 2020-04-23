from day23_1 import Runner, get_day_23_instructions

if __name__ == '__main__':
    instructions = get_day_23_instructions()
    runner = Runner(instructions)
    runner.run()
    print(runner.registers['h'])  # 1 is wrong, unsurprisingly
