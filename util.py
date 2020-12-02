
def read_lines(path, fun=lambda x: x):
    with open(path, 'r') as inp:
        lines = inp.readlines()
        return [fun(l.strip()) for l in lines]


def read_file(path):
    with open(path, 'r') as inp:
        return inp.read()


def count_if(container, predicate):
    count = 0
    for element in container:
        if predicate(element):
            count = count + 1
    return count
