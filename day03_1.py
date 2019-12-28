import math


def main(innum):
    i = 1
    while math.pow(i, 2) < innum:
        i += 2
    i -= 2
    print(i)  # should be 605

    midway = int(i // 2) + 1

    return i


if __name__ == '__main__':
    print(main(368078))  # 538 is too high but i think it's probably off by one...i made a bad, 371 is correct
