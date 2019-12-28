from collections import defaultdict


def get_next_xy(x, y, values):
    if x == 0 and y == 0:
        return 1, 0
    elif values[(x - 1, y)] and not values[(x, y - 1)]:
        return x, y - 1
    elif values[(x, y+1)] and not values[(x-1, y)]:
        return x-1, y
    elif values[(x+1, y)] and not values[(x, y+1)]:
        return x, y+1
    elif values[(x, y-1)] and not values[(x+1, y)]:
        return x+1, y


def set_xy(x, y, values):
    values[(x, y)] = (
        values[(x - 1, y)]
        + values[(x + 1, y)]
        + values[(x, y - 1)]
        + values[(x, y + 1)]
        + values[(x - 1, y - 1)]
        + values[(x - 1, y + 1)]
        + values[(x + 1, y - 1)]
        + values[(x + 1, y + 1)]
    )
    return values[(x, y)]


def main(innum):
    values = defaultdict(lambda: 0)
    thisval = 0
    x = 0
    y = 0
    values[(x, y)] = 1
    while thisval < innum:
        x, y = get_next_xy(x, y, values)
        thisval = set_xy(x, y, values)

    return thisval


if __name__ == '__main__':
    print(main(368078))
