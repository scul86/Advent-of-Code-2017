def solve(inp, offset):
    return sum(int(n1) for n1, n2 in zip(inp, inp[offset:] + inp[:offset]) if n1 == n2)


def main():
    with open('input.txt') as f:
        puzzle_input = f.readline()

    print(solve(puzzle_input, 1))
    print(solve(puzzle_input, len(puzzle_input)//2))


if __name__ == '__main__':
    main()
