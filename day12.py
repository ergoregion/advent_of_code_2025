with open('data/day12_test.txt', 'r') as file:
    test_data = file.read()

with open('data/day12.txt', 'r') as file:
    real_data = file.read()

data = test_data
data = real_data
sections = data.split('\n\n')

print(len(sections))

shapes = {}

for s in sections[:-1]:
    ss = s.split('\n')
    key = int(ss[0][0])
    shape = []
    for i, l in enumerate(ss[1:]):
        for j, c in enumerate(l):
            if c == '#':
                shape.append((i, j))
    shapes[key] = shape
print(shapes)

problems = []
for l in sections[-1].split('\n'):
    a, b = l.split(': ')
    length, width = a.split('x')
    presents = list(map(int, b.split(' ')))

    problems.append((int(length), int(width), presents))
print(problems)


def shape_reflections(shape):

    keys = shapes[shape]
    yield keys
    yield [(x, 2-y) for x, y in keys]


def rotate_keys(keys):
    return [
        keys

    ]


def shape_orientations(shape):

    # normal
    keys = shapes[shape]
    yield keys


def try_to_add(shape, size, used_spaces, orientation, x, y):
    pass


def is_possible(remaining_shapes, remaining_slots):
    pass

# Give up, there's no way that this is what you're supposed to do!


valid_count = 0
invalid_count = 0
remaining_problems = []

for p in problems:
    length, width, presents = p
    number_of_shapes = sum(presents)

    # problems which just fit in easily
    if (length//3*width//3 >= number_of_shapes):
        valid_count = valid_count+1
        continue

    # problems which can never fit trivially
    number_of_squares = 0
    for shape, number in enumerate(presents):
        number_of_squares += len(shapes[shape])*number
    if number_of_squares > length*width:
        invalid_count = invalid_count+1
        continue

    # edge cases
    remaining_problems.append(p)


print(valid_count)
print(invalid_count)
print(len(remaining_problems))

for r in remaining_problems:
    length, width, presents = r
    # Do check here


# REALLY, this was a null problem?
assert (len(remaining_problems) == 0)

print(f"result part 1: {valid_count}")
