from collections import Counter
with open('data/day07_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day07.txt', 'r') as file:
    real_lines = file.readlines()


lines = test_lines
lines = real_lines

print(lines)

split_lines = [l.split() for l in lines]

start_beam = lines[0].index('S')
print(start_beam)
start_beams = [start_beam,]
print(start_beams)
splits = 0
beams = start_beams
for l in lines:
    next_beams = set()
    for b in beams:
        if l[b] == '^':
            splits = splits+1
            next_beams.add(b-1)
            next_beams.add(b+1)
        else:
            next_beams.add(b)

    beams = next_beams

print(f"result part 1: {splits}")

routes = Counter()
routes[start_beam] += 1

for l in lines:
    next_routes = Counter()
    for b in routes.keys():
        if l[b] == '^':
            next_routes[b-1] += routes[b]
            next_routes[b+1] += routes[b]
        else:
            next_routes[b] += routes[b]

    routes = next_routes

route_count = sum(routes[r] for r in routes.keys())

print(f"result part 2: {route_count}")
