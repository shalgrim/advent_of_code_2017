from day14_1 import make_grid


def get_used_coordinates(grid):
    coordinates = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '1':
                coordinates.add((x, y))

    return coordinates


def search_coordinate(coordinate, coordinates, visited=None):
    if visited is None:
        visited = set([coordinate])
    elif coordinate in visited:
        return
    else:
        visited.add(coordinate)

    x, y = coordinate

    if x > 0 and (x - 1, y) in coordinates:
        search_coordinate((x - 1, y), coordinates, visited)

    if x < 127 and (x + 1, y) in coordinates:
        search_coordinate((x + 1, y), coordinates, visited)

    if y > 0 and (x, y - 1) in coordinates:
        search_coordinate((x, y - 1), coordinates, visited)

    if y < 127 and (x, y + 1) in coordinates:
        search_coordinate((x, y + 1), coordinates, visited)

    return visited


def discover_region(unregioned_coords):
    starting_coordinate = unregioned_coords.pop()
    region = search_coordinate(starting_coordinate, unregioned_coords)
    return region


def count_regions(instring):
    grid = make_grid(instring)
    unregioned_coords = get_used_coordinates(grid)
    assert len(unregioned_coords) == 8190
    regions = set()

    while unregioned_coords:
        region = discover_region(unregioned_coords)
        regions.add(frozenset(region))
        unregioned_coords.difference_update(region)

    return len(regions)


if __name__ == '__main__':
    print(count_regions('ffayrhll'))
