import numpy as np
import pandas as pd
import util
import itertools

all_lines = util.read_lines("inputs/day11.txt")
seats = np.array([util.split(line) for line in all_lines])
(rows, columns) = seats.shape


def occupied_part1(seats, row, column):
    occupied = 0
    for c in range(max(0, column - 1), min(columns, column + 2)):
        for r in range(max(0, row - 1), min(rows, row + 2)):
            if (row != r or column != c) and seats[r, c] == "#":
                occupied += 1
    return occupied


def occupied_part2(seats, row, column):
    dirs = set(itertools.product([1, -1, 0], repeat=2))
    dirs.remove((0, 0))
    occupied = 0
    for dr, dc in dirs:
        c = column
        r = row
        while True:
            c += dc
            r += dr
            if c < 0 or c >= columns or r < 0 or r >= rows:
                break
            if seats[r, c] == "#":
                occupied += 1
                break
            if seats[r, c] == "L":
                break
    return occupied


def count_occupied(occupy_function, max_neighbors):
    current_seats = seats.copy()
    (rows, columns) = current_seats.shape
    while True:
        next_seats = current_seats.copy()
        for r in range(0, rows):
            for c in range(0, columns):
                neighbors = occupy_function(current_seats, r, c)
                if current_seats[r, c] == "L" and neighbors == 0:
                    next_seats[r, c] = "#"
                if current_seats[r, c] == "#" and neighbors >= max_neighbors:
                    next_seats[r, c] = "L"

        if (current_seats == next_seats).all():
            break

        current_seats = next_seats.copy()
    return np.count_nonzero(current_seats == "#")


def part1():
    print(count_occupied(occupied_part1, 4))


def part2():
    print(count_occupied(occupied_part2, 5))
