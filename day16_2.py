from day16_1 import run_program_string


def rotate(s):
    """Bad solution because https://www.reddit.com/r/adventofcode/comments/7k572l/2017_day_16_solutions/drbotu7/"""
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


def discover_loop(instructions, s):
    seen = {s: 0}
    rotated = run_program_string(instructions, s)
    rotations = 1

    while rotated not in seen:
        seen[rotated] = rotations
        rotated = run_program_string(instructions, rotated)
        rotations += 1

    print(f'found loop on {rotated}. Seen on rotations {seen[rotated]} and {rotations}')
    print(seen)


if __name__ == '__main__':
    with open('./data/input16.txt') as f:
        content = f.read()

    instructions = content.split(',')
    discover_loop(instructions, 'abcdefghijklmnop')

    # abndekfhijglmpoc is incorrect
    # ioplbgkeajfdmchn is incorrect
    # ieclhfgoajkdmnbp is incorrect
    # klpceabfighdnmjo is incorrect
    # fdnphiegakolcmjb is correct
