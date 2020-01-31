from day15_1 import Generator


class CarefulGenerator(Generator):
    def __init__(self, factor, initial_value, multiple):
        # TODO: make it super
        self.factor = factor
        self.value = initial_value
        self.multiple = multiple

    def update_value(self):
        while super.update_value() %4 != 0:  # TODO: get this right
            pass
        return self.value
