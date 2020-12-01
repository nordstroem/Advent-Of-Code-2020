import util
import itertools as it

all_lines = util.read_lines("inputs/day1.txt", int)


def part1():
    (x, y) = next(filter(lambda v: (v[0] + v[1]) == 2020, it.combinations(all_lines, 2)))
    print(x * y)


def part2():
    (x, y, z) = next(filter(lambda v: (v[0] + v[1] + v[2]) == 2020, it.combinations(all_lines, 3)))
    print(x * y * z)
