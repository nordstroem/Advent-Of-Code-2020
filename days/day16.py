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


def part2():
    fields, my_ticket, tickets = parse()
    valid_tickets = [ticket for ticket in tickets if valid_ticket(ticket, fields)]
    invalid_positions = dict()
    for i in range(len(my_ticket)):
        invalid_positions[i] = set()

    for ticket in valid_tickets:
        for index, value in enumerate(ticket):
            for field_name, field_range in fields.items():
                if not in_range(value, field_range):
                    invalid_positions[index].add(field_name)

    valid_positions = {}
    fields_to_check = set(fields.keys())
    positions_to_check = set(range(len(my_ticket)))

    while len(fields_to_check) > 0:
        for field_name, field_range in fields.items():
            if field_name in fields_to_check:
                possible_positions = []
                for index in positions_to_check:
                    if field_name not in invalid_positions[index]:
                        possible_positions.append(index)

                if len(possible_positions) == 1:
                    valid_positions[field_name] = possible_positions[0]
                    fields_to_check.remove(field_name)
                    positions_to_check.remove(possible_positions[0])

    product = 1
    for field in [field for field in fields.keys() if field.startswith("departure")]:
        product *= my_ticket[valid_positions[field]]

    print(product)
