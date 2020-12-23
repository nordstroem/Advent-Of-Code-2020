import util
import regex as re


class Node:
    def __init__(self):
        self.regex = ""
        self.left = []
        self.right = []


def parse_regexes():
    inp = util.read_file("inputs/day19.txt").strip()
    nodes, regexes = inp.split("\n\n")

    # Build graph
    graph = {}
    for line in nodes.split("\n"):
        index, rest = line.split(":")
        node = Node()

        rest = rest.split("|")
        if len(rest) == 1:
            values = rest[0].strip()
            values = values.split(" ")
            if len(values) == 1:
                if values[0].isdigit():
                    node.left = [values[0]]
                else:
                    # Character
                    node.regex = values[0].replace("\"", "")

            else:
                # Left children
                node.left = values
        else:
            # Left and right children
            node.left = rest[0].strip().split(" ")
            node.right = rest[1].strip().split(" ")

        graph[index] = node

    return graph, regexes.split("\n")


def build_regex(graph, index):
    current_node = graph[index]
    left_regex = "".join([build_regex(graph, node_index) for node_index in current_node.left])
    right_regex = "".join([build_regex(graph, node_index) for node_index in current_node.right])

    if left_regex and right_regex:
        return "({}|{})".format(left_regex, right_regex)

    if left_regex:
        return "{}".format(left_regex)

    return current_node.regex


def fill_regex(graph):
    visited = []
    for node_id in graph.keys():
        node = graph[node_id]
        if node_id not in visited:
            if not node.regex:
                node.regex = build_regex(graph, node_id)
                visited.append(node_id)


def part1():
    graph, patterns = parse_regexes()
    fill_regex(graph)
    regex = graph["0"].regex + "$"
    count = 0
    for pattern in patterns:
        if re.match(regex, pattern):
            count += 1

    print(count)


def part2():
    graph, patterns = parse_regexes()
    fill_regex(graph)

    # Modify 8 and 11 regexes
    reg_42 = graph["42"].regex
    reg_31 = graph["31"].regex

    graph["8"].regex = "{}+".format(reg_42)
    combined_regex = []
    for i in range(1, 10):
        combined_regex.append("({1}{{{0}}}{2}{{{0}}})".format(i, reg_42, reg_31))
    combined_regex = "|".join(combined_regex)

    new_regex = graph["8"].regex + "(" + combined_regex + ")" + "$"
    count = 0
    for pattern in patterns:
        if re.match(new_regex, pattern):
            count += 1

    print(count)
