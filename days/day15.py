from collections import defaultdict


def get_last_spoken(number):
    last_spoken = {0: 1, 6: 2, 1: 3, 7: 4, 2: 5, 19: 6}
    last_number = 20
    current_index = 7

    while current_index < number:
        tmp_last_number = last_number
        if last_number in last_spoken:
            last_number = current_index - last_spoken[last_number]
        else:
            last_number = 0
        last_spoken[tmp_last_number] = current_index
        current_index += 1
    return last_number


def part1():
    print(get_last_spoken(2020))


def part2():
    print(get_last_spoken(30000000))
