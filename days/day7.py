import util
import re
import collections


all_lines = util.read_lines("inputs/day7.txt")


def to_forward_graph(lines):
    graph = collections.defaultdict(lambda: [])
    for line in lines:
        p = re.compile(r"(\w+ \w+) bag")
        (parent, *children) = p.findall(line)
        for child in children:
            graph[child].append(parent)
    return graph


def to_backward_graph(lines):
    graph = collections.defaultdict(lambda: [])
    for line in lines:
        p = re.compile(r"(\w+ \w+) bag")
        (parent, *children) = p.findall(line)
        p = re.compile(r"(\d)")
        amounts = p.findall(line)
        for amount, child in zip(amounts, children):
            for _ in range(int(amount)):
                graph[parent].append(child)
    return graph


def dfs(graph, node, visited, count_duplicates=False):
    if node not in visited:
        if not count_duplicates:
            visited.add(node)
        num_visited = 1
        for neighbour in graph[node]:
            num_visited += dfs(graph, neighbour, visited, count_duplicates)
        return num_visited
    return 0


def part1():
    visited = set()
    graph = to_forward_graph(all_lines)
    num = dfs(graph, "shiny gold", visited)
    print(num - 1)


def part2():
    visited = set()
    graph = to_backward_graph(all_lines)
    num = dfs(graph, "shiny gold", visited, True)
    print(num - 1)
