import util

all_lines = util.read_file("inputs/day4.txt")

def parse(batch):
    passport = {}
    for prop in batch.replace(" ", "\n").split("\n"):
        (field, value) = prop.split(":")
        passport[field] = value
    return passport

entries = map(parse, all_lines.strip().split("\n\n"))

def has_all_fields(entry):
    necessary_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all([field in entry for field in necessary_fields])


def valid_number(value, low, high):
    if not value.isdigit():
        return False
    year = int(value)
    return year >= low and year <= high  


def valid_height(value):
    if len(value) < 4:
        return False
    suffix = value[-2:]
    height = value[:-2]
    if suffix == "cm":
        return valid_number(height, 150, 193)
    if suffix == "in":
        return valid_number(height, 59, 76)
    return False


def valid_hair_color(value):
    if len(value) != 7:
        return False
    if value[0] != "#":
        return False
    for char in value[1:]:
        if not (char.isdigit() or (char.isalpha() and char.islower())):
            return False
    return True


def valid_eye_color(value):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in valid_colors


def valid_password_id(value):
    return len(value) == 9 and value.isdigit()


def part1():
    count = 0
    for entry in entries:
        if has_all_fields(entry):
            count += 1
    print(count)


def part2():
    valid_map = {
        "byr": lambda x: valid_number(x, 1920, 2002),
        "iyr": lambda x: valid_number(x, 2010, 2020),
        "eyr": lambda x: valid_number(x, 2020, 2030),
        "hgt": lambda x: valid_height(x),
        "hcl": lambda x: valid_hair_color(x),
        "ecl": lambda x: valid_eye_color(x),
        "pid": lambda x: valid_password_id(x),
        "cid": lambda x: True
    }

    count = 0
    for entry in entries:
        if has_all_fields(entry):
            all_valid = True
            for (field, value) in entry.items():
                if not valid_map[field](value):
                    all_valid = False
            if all_valid:
                count += 1
    print(count)
