import util
import operator

all_lines = util.read_file("inputs/day6.txt").strip()


def count_answers(operator):
    result = 0
    groups = all_lines.split("\n\n")
    for group in groups:
        person_answers = group.split("\n")
        answers = set(person_answers[0])
        for answer in person_answers[1:]:
            answers = operator(answers, set(answer))
        result += len(answers)
    return result


def part1():
    print(count_answers(operator.or_))


def part2():
    print(count_answers(operator.and_))
