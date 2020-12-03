import util

all_lines = util.read_lines("inputs/day3.txt")


def encounters(slope, down):
    count = 0
    for (row, line) in enumerate(all_lines[::down]):
        cols = len(line)
        if line[(row * slope) % cols] == "#":
            count += 1
    return count


def part1():
    print(encounters(3, 1))


def part2():
    configurations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for (down, slope) in configurations:
        result *= encounters(down, slope)
    print(result)
