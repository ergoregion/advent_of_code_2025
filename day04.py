with open('data/day04_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day04.txt', 'r') as file:
    real_lines = file.readlines()


# lines = test_lines
lines = real_lines



roll_locations = set()

for row, l in enumerate(lines):
    for col, c in enumerate(l):
        if c=='@':
            roll_locations.add((col, row))

def surrounded_by_count(location, current_locations):
    count =0
    if (location[0]-1, location[1]-1) in current_locations:
        count=count+1
        
    if (location[0]-1, location[1]) in current_locations:
        count=count+1
        
    if (location[0]-1, location[1]+1) in current_locations:
        count=count+1
        
    if (location[0], location[1]-1) in current_locations:
        count=count+1
        
    if (location[0], location[1]+1) in current_locations:
        count=count+1
    if (location[0]+1, location[1]-1) in current_locations:
        count=count+1
        
    if (location[0]+1, location[1]) in current_locations:
        count=count+1
        
    if (location[0]+1, location[1]+1) in current_locations:
        count=count+1

    return count

unblocked_locations = [r for r in roll_locations if surrounded_by_count(r, roll_locations)<4]

print(len(unblocked_locations))
print(f"result part 1: {len(unblocked_locations)}")

unremoved_locations = set(r for r in roll_locations)
for r in unblocked_locations:
    unremoved_locations.remove(r)
improvement = len(unremoved_locations)
while improvement>0:
    unblocked_locations = [r for r in unremoved_locations if surrounded_by_count(r, unremoved_locations)<4]
    print(len(unblocked_locations))
    for r in unblocked_locations:
        unremoved_locations.remove(r)
    improvement = len(unblocked_locations)


print(len(unremoved_locations))
print(f"result part 2: {len(roll_locations)-len(unremoved_locations)}")
