def main(number):
    digits = [int(c) for c in number]
    halfway = len(digits) // 2
    matching_digits = [2*c for i, c in enumerate(digits[:halfway]) if c == digits[i+halfway]]
    return sum(matching_digits)


if __name__ == '__main__':
    with open('data/input01.txt') as f:
        data = f.read().strip()
    print(main(data))
