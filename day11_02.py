from enum import Enum, auto


class Direction(Enum):
    N = auto()
    NE = auto()
    SE = auto()
    S = auto()
    SW = auto()
    NW = auto()

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError(
                f"'+' not supporrted between instances of 'Direction' and '{type(other)}'"
            )
        raise NotImplementedError("haven't done this yet")


class Hex(object):
    def __init__(self, from_direction=None, from_hex=None):
        if from_direction:
            self.__setattr__(from_direction.name, from_hex)
        self._assign_neighbors()
        self.distance = min([n.radius for n in self.get_known_neighbors()]) + 1

    def get_known_neighbors(self):
        known_neighbors = {}
        for d in Direction:
            if self.__getattribute__(d.name):
                known_neighbors[d] = self.__getattribute__(d.name)

        return known_neighbors

    def _assign_neighbors(self):
        old_known_neighbors = None
        known_neighbors = self.get_known_neighbors()

        while known_neighbors != old_known_neighbors:
            new_known_neighbors = {
                k: v for k, v in known_neighbors.items() if k not in old_known_neighbors
            }
