with open('input.txt') as f:
    puzzle_input = f.readline()

print(sum(int(n1) for n1, n2 in zip(puzzle_input, puzzle_input[1:]+puzzle_input[0]) if n1 == n2))

half_len = len(puzzle_input) // 2

print(sum(int(n1) for n1, n2 in zip(puzzle_input, puzzle_input[half_len:] + puzzle_input[:half_len]) if n1 == n2))
