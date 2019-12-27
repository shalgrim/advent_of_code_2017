def main(number):
    digits = [int(c) for c in number]
    matching_digits = [c for i, c in enumerate(digits[:-1]) if c == digits[i+1]]
    if digits[-1] == digits[0]:
        matching_digits.append(digits[-1])
    return sum(matching_digits)


if __name__ == '__main__':
    with open('data/input01.txt') as f:
        data = f.read().strip()
    print(main(data))
