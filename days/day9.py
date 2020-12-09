import collections
import util
import itertools
import sys


sys.setrecursionlimit(1500)

numbers = util.read_lines("inputs/day9.txt", int)


def is_sum(value, container):
    combinations = itertools.combinations(container, r=2)
    for (a, b) in combinations:
        if a + b == value:
            return True
    return False


def get_invalid(container, preamble_size):
    preamble = collections.deque(maxlen=preamble_size)
    preamble.extend(numbers[:preamble_size])

    for number in numbers[preamble_size:]:
        if not is_sum(number, preamble):
            return number
        preamble.append(number)
    return None


dp_map = {}
nums = len(numbers)


def dp(start, end, value):
    key = (start, end)
    if key in dp_map:
        return dp_map[(start, end)]

    if end - start < 2 or start >= end or end > nums:
        dp_map[key] = None
        return None

    if sum(numbers[start:end]) == value:
        dp_map[key] = (start, end)
        return key

    interval_1 = dp(start + 1, end, value)
    interval_2 = dp(start, end - 1, value)

    if interval_1:
        dp_map[key] = interval_1
        return interval_1

    if interval_2:
        dp_map[key] = interval_2
        return interval_2

    dp_map[key] = None
    return None


def part1():
    print(get_invalid(numbers, 25))


def part2():
    (low, high) = dp(0, nums, get_invalid(numbers, 25))
    print(min(numbers[low:high]) + max(numbers[low:high]))
