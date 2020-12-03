import util
import collections
import functools

all_lines = util.read_lines("inputs/day2.txt")


def parse(string):
    (low, high, character, password) = string.replace(":", "").replace("-", " ").split(" ")
    return (int(low), int(high), character, password)


def valid_part1(string):
    (low, high, character, password) = parse(string)
    count = list(password).count(character)
    return count >= low and count <= high


def valid_part2(string):
    (low, high, character, password) = parse(string)
    return (password[low - 1] == character) != (password[high - 1] == character)


def part1():
    print(util.count_if(all_lines, valid_part1))


def part2():
    print(util.count_if(all_lines, valid_part2))
