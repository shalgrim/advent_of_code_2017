from day15_1 import Generator
from day15_1 import FACTOR_A, FACTOR_B


class CarefulGenerator(Generator):
    def __init__(self, factor, initial_value, multiple):
        super().__init__(factor, initial_value)
        self.multiple = multiple

    def update_value(self):
        while super().update_value() % self.multiple != 0:
            pass
        return self.value


def main(factor_a, initial_a, factor_b, initial_b, num_iterations):
    matches = 0
    generator_a = CarefulGenerator(factor_a, initial_a, 4)
    generator_b = CarefulGenerator(factor_b, initial_b, 8)

    for i in range(num_iterations):
        if generator_a.update_value() % 65536 == generator_b.update_value() % 65536:
            matches += 1

    return matches


if __name__ == '__main__':
    INITIAL_A = 516
    INITIAL_B = 190
    print(main(FACTOR_A, INITIAL_A, FACTOR_B, INITIAL_B, 5_000_000))
