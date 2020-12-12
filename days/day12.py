import util

instructions = util.read_lines("inputs/day12.txt")


class Ship:
    def __init__(self):
        self.position = 0 + 0j
        self.direction = 1 + 0j

    def apply(self, command, value):
        if command == "N":
            self.position += 1j * value
        if command == "S":
            self.position -= 1j * value
        if command == "E":
            self.position += 1 * value
        if command == "W":
            self.position -= 1 * value
        if command == "F":
            self.position += self.direction * value
        if command == "R":
            if value == 90:
                self.direction *= -1j
            if value == 180:
                self.direction *= -1
            if value == 270:
                self.direction *= 1j
        if command == "L":
            if value == 90:
                self.direction *= 1j
            if value == 180:
                self.direction *= -1
            if value == 270:
                self.direction *= -1j


class WaypointShip:
    def __init__(self):
        self.position = 0 + 0j
        self.waypoint_position = 10 + 1j

    def apply(self, command, value):
        direction = self.waypoint_position - self.position
        if command == "N":
            self.waypoint_position += 1j * value
        if command == "S":
            self.waypoint_position -= 1j * value
        if command == "E":
            self.waypoint_position += 1 * value
        if command == "W":
            self.waypoint_position -= 1 * value
        if command == "F":
            self.position += direction * value
            self.waypoint_position += direction * value
        if command == "R":
            if value == 90:
                direction *= -1j
            if value == 180:
                direction *= -1
            if value == 270:
                direction *= 1j
            self.waypoint_position = direction + self.position
        if command == "L":
            if value == 90:
                direction *= 1j
            if value == 180:
                direction *= -1
            if value == 270:
                direction *= -1j
            self.waypoint_position = direction + self.position


def run_ship(ship):
    for instr in instructions:
        command = instr[0]
        value = int(instr[1:])
        ship.apply(command, value)
    return(abs(ship.position.real) + abs(ship.position.imag))


def part1():
    ship = Ship()
    print(run_ship(ship))


def part2():
    ship = WaypointShip()
    print(run_ship(ship))
