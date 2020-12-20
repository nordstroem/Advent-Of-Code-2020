import util


def shunting_yard(string, precedence_map):
    tokens = [c for c in string]
    output_queue = []
    operator_stack = []
    while (len(tokens) > 0):
        current = tokens.pop(0)
        if current.isdigit():
            output_queue.append(current)
        elif current == "+" or current == "*":
            while operator_stack and operator_stack[-1] != "(" and precedence_map[operator_stack[-1]] >= precedence_map[current]:
                output_queue.append(operator_stack.pop(-1))
            operator_stack.append(current)
        elif current == "(":
            operator_stack.append(current)
        elif current == ")":
            while operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop(-1))
            if operator_stack[-1] == "(":
                operator_stack.pop(-1)

    while operator_stack:
        output_queue.append(operator_stack.pop(-1))

    rpn_stack = []
    for token in output_queue:
        if token.isdigit():
            rpn_stack.append(token)
        else:
            right = int(rpn_stack.pop(-1))
            left = int(rpn_stack.pop(-1))
            if token == "+":
                rpn_stack.append(left + right)
            else:
                rpn_stack.append(left * right)

    return rpn_stack[0]


def solve(precedence_map):
    all_lines = util.read_lines("inputs/day18.txt")
    result = 0
    for line in all_lines:
        result += shunting_yard(line.replace(" ", ""), precedence_map)
    return result


def part1():
    presedence_map = {"+": 1, "*": 1}
    print(solve(presedence_map))


def part2():
    presedence_map = {"+": 2, "*": 1}
    print(solve(presedence_map))
