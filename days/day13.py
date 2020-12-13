import util
from sympy.ntheory.modular import crt

all_lines = util.read_lines("inputs/day13.txt")
timestamp = int(all_lines[0])


def part1():
    bus_ids = all_lines[1].split(",")
    bus_ids = filter(lambda x: x != "x", bus_ids)
    bus_ids = map(int, bus_ids)

    min_id = None
    min_time_to_wait = timestamp

    for bus_id in bus_ids:
        best_match = (timestamp // bus_id + 1) * bus_id
        if best_match - timestamp < min_time_to_wait:
            min_id = bus_id
            min_time_to_wait = best_match - timestamp

    print(min_id * min_time_to_wait)


def part2():
    bus_ids = map(int, all_lines[1].replace("x", "-1").split(","))
    ids = [(bus_id, -offset) for offset, bus_id in enumerate(bus_ids) if bus_id != -1]
    ids = zip(*ids)
    m = list(next(ids))
    v = list(next(ids))
    (x, _) = crt(m, v, check=False)
    print(x)
