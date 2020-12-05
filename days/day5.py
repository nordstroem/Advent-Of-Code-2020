import util

all_lines = util.read_lines("inputs/day5.txt")


def binary_partitition_search(string, lower_char, upper_char):
    low = 0
    high = 2**len(string) - 1
    for c in string:
        if c == lower_char:
            high = (high + low) // 2
        if c == upper_char:
            low = (high + low) // 2 + 1
    return low


def seat(string):
    row = binary_partitition_search(string[:-3], "F", "B")
    column = binary_partitition_search(string[-3:], "L", "R")
    return row * 8 + column


def part1():
    print(max([seat for seat in map(seat, all_lines)]))


def part2():
    all_seats = [seat for seat in map(seat, all_lines)]

    for r in range(1, 127):
        for c in range(0, 8):
            id = r * 8 + c
            if id not in all_seats and (id + 1) in all_seats and (id - 1) in all_seats:
                print(id)
