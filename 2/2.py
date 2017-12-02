def solve_p1(inp):
    sum = 0
    for line in inp:
        line = list(map(int, line.split('\t')))
        sum += max(line) - min(line)
    return sum


def solve_p2(inp):
    ret = 0
    for line in inp:
        line = list(map(int, line.split('\t')))
        for i, num in enumerate(line):
            for j in range(len(line)):
                if i == j: continue
                if line[i] % line[j] == 0:
                    ret += num // line[j]
    return ret


def main():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()

    print(solve_p1(puzzle_input))
    print(solve_p2(puzzle_input))


if __name__ == '__main__':
    main()