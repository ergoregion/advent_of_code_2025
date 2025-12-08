with open('data/day08_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day08.txt', 'r') as file:
    real_lines = file.readlines()


lines = test_lines
lines = real_lines


split_lines = [l.split(',') for l in lines]


boxes = [tuple(int(i) for i in l) for l in split_lines]


def distancesd(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2


pairs = []
for i, a in enumerate(boxes):
    for j in range(i):
        b = boxes[j]
        distance = distancesd(a, b)
        pairs.append((distance, a, b))
pairs.sort(key=lambda p: p[0])

print(pairs[1])

circuits = []
unconnected_boxes = set(boxes)
connections = 0
for _, a, b in pairs:
    if a in unconnected_boxes and b in unconnected_boxes:
        circuits.append(set([a, b]))
        unconnected_boxes.remove(a)
        unconnected_boxes.remove(b)
        connections = connections+1
    elif (a in unconnected_boxes):
        b_circuit = [c for c in circuits if b in c]
        b_circuit[0].add(a)
        unconnected_boxes.remove(a)
        connections = connections+1
    elif (b in unconnected_boxes):
        a_circuit = [c for c in circuits if a in c]
        a_circuit[0].add(b)
        unconnected_boxes.remove(b)
        connections = connections+1
    else:
        a_circuit = [c for c in circuits if a in c][0]
        b_circuit = [c for c in circuits if b in c][0]
        if a_circuit == b_circuit:
            pass
            # The wording "nothing happens" is confusing me, does this constitute a connection?
            # I think it does otherwise there will be only a single circuit too early (after 999 connections)
            # and the result will always be 0
            connections = connections+1
        else:
            a_circuit.update(b_circuit)
            circuits.remove(b_circuit)
            connections = connections+1

    if connections == 10:
        sizes = [len(c) for c in circuits]
        sizes.sort(reverse=True)
        print(sizes)
        print(f"result after 10 connections: {sizes[0]*sizes[1]*sizes[2]}")

    if connections == 1000:
        sizes = [len(c) for c in circuits]
        sizes.sort(reverse=True)
        print(sizes)
        print(f"result part 1: {sizes[0]*sizes[1]*sizes[2]}")

    if (len(unconnected_boxes) == 0 and len(circuits) == 1):
        print("one circuit")
        print(a)
        print(b)
        print(f"result part 2: {a[0]*b[0]}")
        break
