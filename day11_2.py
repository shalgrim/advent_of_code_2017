from enum import Enum, auto

from day11_1 import get_final_steps_away


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
            # I believe this is the bug. It doesn't work when you're out on a limb dangling
            # So at the second se in my directions, I think I may be getting that one wrong
            # And it's also not asking the distance anyway, it's asking the fewest steps
            # So maybe the trick is to re-evaluate distance every time you pass through a hex?
            # No that doesn't work because in the example 'ne,ne,s,s,' they say two steps away at 'se,se'
            # But the first se never got visited
            # So they do want the radius but I have to assume the whole map exists
            self.distance = (
                min([n.distance for n in self.get_known_neighbors().values()]) + 1
            )

    def __repr__(self):
        formatted_directions = [
            f'{d.name}: {self.__getattribute__(d.name)}'
            for d in Direction
            if self.__getattribute__(d.name)
        ]
        neighbor_string = ', ' + '; '.join(formatted_directions) if self.get_known_neighbors() else ''
        return f'Hex: id: {id(self)}; distance: {self.distance}{neighbor_string}'

    def __str__(self):
        line0 = f'  {self.N.distance}  ' if self.N else ''

        nw = str(self.NW.distance) if self.NW else ' '
        ne = str(self.NE.distance) if self.NE else ' '
        line1 = f'{nw}/-\{ne}'

        line2 = f'  {self.distance}  '

        sw = str(self.SW.distance) if self.SW else ' '
        se = str(self.SE.distance) if self.SE else ' '
        line3 = f'{sw}\_/{se}'

        line4 = f'  {self.S.distance}  ' if self.S else ''

        return '\n'.join([line0, line1, line2, line3, line4])

    def create_new_neighbor(self, direction):
        """
        Creates a new hex at this Hex's direction
        :param direction: the direction of this Hex where to put the new neighbor
        :return: the new hex created
        """
        assert (
            self.__getattribute__(direction.name) is None
        ), f"Can't create a neighbor at {direction} because one is already there"
        other_direction = direction + 3
        new_hex = Hex(other_direction, self)
        return new_hex

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
                        clockwise.__setattr__((direction - 2).name, self)

                if not self.__getattribute__(
                    (direction - 1).name
                ):  # If I don't already know the ccw hex
                    # check if my known neighbor knows about it
                    ccw = neighbor.__getattribute__((direction - 2).name)
                    if ccw:
                        self.__setattr__((direction - 1).name, ccw)
                        ccw.__setattr__((direction + 2).name, self)

            old_known_neighbors = known_neighbors
            known_neighbors = self.get_known_neighbors()


def some_tests():
    h = Hex()
    h2 = h.create_new_neighbor(Direction.N)
    h3 = h2.create_new_neighbor(Direction.SE)
    print(h.get_known_neighbors(), h.distance)
    print(h2.get_known_neighbors(), h2.distance)
    print(h3.get_known_neighbors(), h3.distance)


def build_graph(directions):
    root_hex = Hex()
    all_hexes = set()
    all_hexes.add(root_hex)
    curr_hex = root_hex

    for lower_case_direction in directions:
        # is there a better way than using __members__?
        print(lower_case_direction)
        print(curr_hex)
        direction = Direction.__members__[lower_case_direction.upper()]
        dir_name = direction.name
        if curr_hex.__getattribute__(dir_name):  # could I try walrus operator here?
            curr_hex = curr_hex.__getattribute__(dir_name)
        else:
            curr_hex = curr_hex.create_new_neighbor(direction)
            all_hexes.add(curr_hex)

    return root_hex, all_hexes


def get_furthest_away(directions):
    furthest = 0
    for i in range(len(directions)):
        steps = get_final_steps_away(directions[:i])
        if steps > furthest:
            furthest = steps
            print(f'{i=}, {furthest=}')
    return furthest


def main(content):
    directions = content.split(',')
    return get_furthest_away(directions)


if __name__ == '__main__':
    with open('data/input11.txt') as f:
        content = f.read().strip()
    print(main(content))  # 1830 is too high
