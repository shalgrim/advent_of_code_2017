def rotate(s):
    return (
        s[8]
        + s[14]
        + s[13]
        + s[11]
        + s[1]
        + s[10]
        + s[5]
        + s[4]
        + s[0]
        + s[9]
        + s[6]
        + s[3]
        + s[12]
        + s[15]
        + s[7]
        + s[2]
    )


def discover_loop(s):
    seen = {s: 0}
    rotated = rotate(s)
    rotations = 1

    while rotated not in seen:
        seen[rotated] = rotations
        rotated = rotate(rotated)
        rotations += 1

    print(f'found loop on {rotated}. Seen on rotations {seen[rotated]} and {rotations}')
    print(seen)


if __name__ == '__main__':
    discover_loop('abcdefghijklmnop')

    # abndekfhijglmpoc is incorrect
    # ioplbgkeajfdmchn is incorrect
    # ieclhfgoajkdmnbp is incorrect
