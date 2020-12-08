import util
import collections

all_lines = util.read_lines("inputs/day8.txt")


def parse(source_code):
    instructions = []
    for line in all_lines:
        splitted = line.split()
        op = splitted[0]
        arg = int(splitted[1])
        instructions.append((op, arg))
    return instructions


def run_program(program):
    acc = 0
    row = 0
    visited = set()
    while True:
        if row in visited:
            return (acc, False)
        if row == len(program) - 1:
            return (acc, True)
        visited.add(row)
        (op, arg) = program[row]
        if op == "nop":
            row += 1
        elif op == "acc":
            acc += arg
            row += 1
        elif op == "jmp":
            row += arg


def part1():
    program = parse(all_lines)
    print(run_program(program)[0])


def part2():
    corrupted_program = parse(all_lines)
    swaps = {
        "nop": "jmp",
        "jmp": "nop"
    }
    for row_to_change in range(0, len(corrupted_program)):
        modified_program = corrupted_program.copy()
        (op, arg) = modified_program[row_to_change]
        if op in swaps:
            modified_program[row_to_change] = (swaps[op], arg)
            (acc, valid) = run_program(modified_program)
            if valid:
                print(acc)
