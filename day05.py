with open('data/day05_test.txt', 'r') as file:
    test_data = file.read()

with open('data/day05.txt', 'r') as file:
    real_data = file.read()


data = test_data
data = real_data

sections = data.split("\n\n")

lines = sections[0].split("\n")
ingredients = sections[1].split("\n")

# print(lines)
# print(ingredients)

inclusive_ranges = [[int(i) for i in l.strip().split('-')]for l in lines]
ranges = [[r[0], r[1]+1] for r in inclusive_ranges]
# print(ranges)


def is_valid(ing):
    for r in ranges:
        if (r[0] <= ing < r[1]):
            return True
    return False


result = 0
valid = [i for i in ingredients if is_valid(int(i))]
# print(valid)
print(f"result part 1: {len(valid)}")

# sorting by start condition, means we can look for overlaps in adjacent ranges
ranges.sort(key=lambda r: r[0])


result = 0
active_range = ranges[0]
for r in ranges[1:]:
    if r[0] <= active_range[1]:
        # make the current active range bigger
        active_range[1] = max(r[1], active_range[1])
    else:
        # add the current active range to the result & start a new one
        result += active_range[1]-active_range[0]
        active_range = r
# add the final range
result += active_range[1]-active_range[0]

print(f"result part 2: {result}")
