import util


def parse():
    all_lines = util.read_file("inputs/day16.txt")
    (fields, my_ticket, tickets) = all_lines.split("\n\n")

    # parse fields
    field_ranges = {}
    for line in fields.split("\n"):
        (field, tmp_ranges) = line.split(":")
        field_range = []
        for r in tmp_ranges.split("or"):
            (low,  high) = r.strip().split("-")
            field_range.append((int(low), int(high)))
        field_ranges[field] = field_range

    # parse my ticket
    my_ticket = tuple(map(int, my_ticket.split("\n")[1].split(",")))

    # parse other tickets
    all_tickets = []
    for ticket in tickets.strip().split("\n")[1:]:
        all_tickets.append(tuple(map(int, ticket.split(","))))
    return field_ranges, my_ticket, all_tickets


def in_range(value, ranges):
    in_any_range = False
    for low, high in ranges:
        if value >= low and value <= high:
            in_any_range = True
    return in_any_range


def valid_ticket(ticket, fields):
    for value in ticket:
        in_any_range = False
        for field_range in fields.values():
            if in_range(value, field_range):
                in_any_range = True
        if not in_any_range:
            return False
    return True


def part1():
    fields, my_ticket, tickets = parse()
    error_sum = 0
    for ticket in tickets:
        for value in ticket:
            in_any_range = False
            for field_range in fields.values():
                if in_range(value, field_range):
                    in_any_range = True
            if not in_any_range:
                error_sum += value

    print(error_sum)
