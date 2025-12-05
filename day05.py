with open('data/day05_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day05.txt', 'r') as file:
    real_lines = file.readlines()

with open('data/day05_a_test.txt', 'r') as file:
    test_ing = file.readlines()

with open('data/day05_a.txt', 'r') as file:
    real_ing = file.readlines()


lines = test_lines
lines = real_lines
ing = test_ing
ing = real_ing

print(lines)
print(ing)

ranges = [[int(i) for i in l.strip().split('-')]for l in lines]
print(ranges)

def is_valid(ing):
    for r in ranges:
        if(r[0]<=ing<=r[1]):
            return True
    return False

result = 0
valid = [i for i in ing if is_valid(int(i))]
print(valid)
print(f"result part 1: {len(valid)}")

ranges = [(r[0],r[1]) for r in ranges]

def ranges_overlap(r1, r2):
    overlap = max(0, min(r1[1]+1, r2[1]+1) - max(r1[0], r2[0]))
    return overlap>0

def consolidate_ranges(r1, r2):
    return min(r1[0], r2[0]), max(r1[1], r2[1])

def add_range(r,existing_ranges):
    for re in existing_ranges:
        if ranges_overlap(r,re):
            existing_ranges.remove(re)
            existing_ranges.add(consolidate_ranges(r, re))
            return
    existing_ranges.add(r)

consolidated_ranges = set()
for r in ranges:
    add_range(r, consolidated_ranges)
print(len(consolidated_ranges))
old_count = len(ranges)
new_count = len(consolidated_ranges)
while new_count<old_count:
    old_count = len(consolidated_ranges)
    old_ranges = consolidated_ranges
    consolidated_ranges = set()
    for r in old_ranges:
        add_range(r, consolidated_ranges)
    print(len(consolidated_ranges))
    new_count = len(consolidated_ranges)



result = 0
for r in consolidated_ranges:
    result += r[1]+1-r[0]
print(f"result part 2: {result}")
    