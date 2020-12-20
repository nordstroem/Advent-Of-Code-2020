import util
from collections import defaultdict
from itertools import product


def parse_grid(dims):
    grid = defaultdict(bool)
    all_lines = util.read_lines("inputs/day17.txt")
    for row, line in enumerate(all_lines):
        for col, char in enumerate(line):
            if char == "#":
                pad = (0,)*(dims - 2)
                grid[(col, row, *pad)] = True
    return grid


def neighbours(point):
    n = []
    dims = len(point)
    for dp in product([-1, 0, 1], repeat=dims):
        if dp != (0,)*dims:
            n.append(tuple(map(sum, zip(point, dp))))
    return n


def num_active_neighbors(point, grid):
    num = 0
    for n in neighbours(point):
        if n in grid and grid[n]:
            num += 1
    return num


def cycle(grid):
    tmp_grid = grid.copy()
    # Make sure neigbours of all active points are in the set
    for point, active in grid.items():
        if active:
            ns = neighbours(point)
            for n in ns:
                if n not in grid:
                    tmp_grid[n] = False

    for point, active in tmp_grid.items():
        na = num_active_neighbors(point, tmp_grid)
        if active and not (na == 2 or na == 3):
            grid[point] = False
        if not active and na == 3:
            grid[point] = True

    return grid


def part1():
    grid = parse_grid(3)

    for _ in range(6):
        grid = cycle(grid)

    num_active = 0
    for active in grid.values():
        if active:
            num_active += 1

    print(num_active)


def part2():
    grid = parse_grid(4)

    for _ in range(6):
        grid = cycle(grid)

    num_active = 0
    for active in grid.values():
        if active:
            num_active += 1

    print(num_active)
