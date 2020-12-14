import util
import re
import itertools

all_lines = util.read_lines("inputs/day14.txt")


def mask_value(value, mask):
    result_bits = []
    for value_bit, mask_bit in zip(value, mask):
        if mask_bit == "X":
            result_bits.append(value_bit)
        else:
            result_bits.append(mask_bit)
    return "".join(result_bits)


def part1():
    mask_matcher = r"mask = (.+)$"
    mem_matcher = r"mem\[(\d+)\] = (\d+)$"

    memory = {}
    mask = None
    for line in all_lines:
        if (mask_groups := re.findall(mask_matcher, line)):
            mask = mask_groups[0]
        else:
            mem_loc, value = re.findall(mem_matcher, line)[0]
            value = format(int(value), "b").zfill(36)
            memory[mem_loc] = mask_value(value, mask)

    result = 0
    for v in memory.values():
        result += int(v, base=2)
    print(result)


def power_set(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(0, len(s)+1))


def set_floating(mem_loc, mask, value, memory):
    floating_indices = []
    for index, c in enumerate(mask):
        if c == "X":
            floating_indices.append(index)

    for current_set in power_set(floating_indices):
        new_address = list(mem_loc)
        for index in range(len(mem_loc)):
            if mask[index] == "1":
                new_address[index] = str(1)
        for index in floating_indices:
            if index in current_set:
                new_address[index] = str(1)
            else:
                new_address[index] = str(0)

        new_address = "".join(new_address)
        memory[new_address] = value


def part2():
    memory = {}
    mask = None

    mask_matcher = r"mask = (.+)$"
    mem_matcher = r"mem\[(\d+)\] = (\d+)$"

    for line in all_lines:
        if (mask_groups := re.findall(mask_matcher, line)):
            mask = mask_groups[0]
        else:
            mem_loc, value = re.findall(mem_matcher, line)[0]
            value = format(int(value), "b").zfill(36)
            set_floating(format(int(mem_loc), "b").zfill(36), mask, value, memory)

    result = 0
    for v in memory.values():
        result += int(v, base=2)
    print(result)
