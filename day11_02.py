from enum import Enum, auto


class Direction(Enum):
    N = auto()
    NE = auto()
    SE = auto()
    S = auto()
    SW = auto()
    NW = auto()

    def __add__(self, other):
        """should write some tests"""
        if isinstance(other, int):
            zero_indexed = self.value - 1 + other
            zi_mod = zero_indexed % 6
            return Direction(zi_mod + 1)
        raise TypeError(
            f"'+' not supported between instances of 'Direction' and '{type(other)}'"
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        return self.__sub__(other)


class Hex(object):
    def __init__(self, from_direction=None, from_hex=None):
        for d in Direction:
            self.__setattr__(d.name, None)

        if from_direction:
            self.__setattr__(from_direction.name, from_hex)
            from_hex.__setattr__((from_direction + 3).name, self)

        self._assign_neighbors()
        if not self.get_known_neighbors():
            self.distance = 0
        else:
            self.distance = min([n.distance for n in self.get_known_neighbors().values()]) + 1

    def get_known_neighbors(self):
        known_neighbors = {}
        for d in Direction:
            neighbor_hex = self.__getattribute__(d.name)
            if neighbor_hex:
                known_neighbors[d] = neighbor_hex

        return known_neighbors

    def _assign_neighbors(self):
        old_known_neighbors = None
        known_neighbors = self.get_known_neighbors()

        while known_neighbors != old_known_neighbors:
            for direction, neighbor in known_neighbors.items():
                if not self.__getattribute__(
                    (direction + 1).name
                ):  # If I don't already know the clockwise hex
                    # check if my known neighbor knows about it
                    clockwise = neighbor.__getattribute__((direction + 2).name)
                    if clockwise:
                        self.__setattr__((direction + 1).name, clockwise)

                if not self.__getattribute__(
                    (direction - 1).name
                ):  # If I don't already know the ccw hex
                    # check if my known neighbor knows about it
                    ccw = neighbor.__getattribute__((direction - 2).name)
                    if ccw:
                        self.__setattr__((direction - 1).name, ccw)

            old_known_neighbors = known_neighbors
            known_neighbors = self.get_known_neighbors()


if __name__ == '__main__':
    h = Hex()
    h2 = Hex(Direction.S, h)
    print(h.get_known_neighbors(), h.distance)
    print(h2.get_known_neighbors(), h2.distance)

