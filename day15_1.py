DIVISOR = 2147483647
FACTOR_A = 16807
FACTOR_B = 48271


class Generator(object):
    def __init__(self, factor, initial_value):
        self.factor = factor
        self.value = initial_value

    def update_value(self):
        self.value = self.value * self.factor % DIVISOR
        return self.value


def main(factor_a, initial_a, factor_b, initial_b, num_iterations):
    matches = 0
    generator_a = Generator(factor_a, initial_a)
    generator_b = Generator(factor_b, initial_b)

    for i in range(num_iterations):
        if generator_a.update_value() % 256 == generator_b.update_value() % 256:
            matches += 1

    return matches


if __name__ == '__main__':
    INITIAL_A = 516
    INITIAL_B = 190
    # 156059 is too high, which is what i get with test data...with real input I get even higher 156946
    print(main(FACTOR_A, INITIAL_A, FACTOR_B, INITIAL_B, 40_000_000))
