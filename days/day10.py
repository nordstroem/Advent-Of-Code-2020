import util
import numpy as np
from collections import Counter
from collections import defaultdict

jolts = np.array(util.read_lines("inputs/day10.txt", int))
jolts = np.append(jolts, 0)
jolts = np.append(jolts, np.max(jolts) + 3)
jolts.sort()


def part1():
    occurences = Counter(np.diff(jolts))
    print(occurences[1] * occurences[3])


def build_graph():
    graph = defaultdict(list)
    for i in range(len(jolts)):
        current_number = jolts[i]
        graph[current_number] = [number for number in jolts[:i] if current_number - number <= 3]
    return graph


dp_map = {0: 1}


def arrangements(graph, number):
    if number in dp_map:
        return dp_map[number]

    result = 0
    for neighbor in graph[number]:
        result += arrangements(graph, neighbor)

    dp_map[number] = result
    return result


def part2():
    graph = build_graph()
    print(arrangements(graph, max(jolts)))
