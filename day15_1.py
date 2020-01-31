DIVISOR = 2147483647
FACTOR_A = 16807
FACTOR_B = 48271
INITIAL_A = 65
INITIAL_B = 8921


class Generator(object):
    def __init__(self, factor, initial_value):
        self.factor = factor
        self.value = initial_value

    def update_value(self):
        self.value = self.value * self.factor % DIVISOR
        return self.value


def main():
    matches = 0
    generator_a = Generator(FACTOR_A, INITIAL_A)
    generator_b = Generator(FACTOR_B, INITIAL_B)

    for i in range(40_000_000):
        if generator_a.update_value() % 256 == generator_b.update_value() % 256:
            matches += 1

    return matches


if __name__ == '__main__':
    print(main())  # 156059 is too high
