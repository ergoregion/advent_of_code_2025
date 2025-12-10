with open('data/day09_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day09.txt', 'r') as file:
    real_lines = file.readlines()


lines = test_lines
lines = real_lines


split_lines = [l.split(',') for l in lines]

split_lines = [[int(j) for j in l] for l in split_lines]

split_lines = [(l[0],l[1]) for l in split_lines]
print(split_lines)

class CornerContraction:
    def __init__(self, coords):
        xs = list(set((x for x,_ in coords)))
        ys = list(set((y for _,y in coords)))
        xs.sort()
        ys.sort()
        self.contracted_x = dict((x, 2*i) for i, x in enumerate(xs))
        self.contracted_y = dict((y, 2*i) for i, y in enumerate(ys))

    def contract(self, a):
        return self.contracted_x[a[0]], self.contracted_y[a[1]]
    
cc =  CornerContraction(split_lines)


from itertools import combinations, pairwise

areas=[]
def area(a,b):
    ai, aj= a
    bi, bj = b
    return (abs(ai-bi)+1)*(abs(aj-bj)+1)

max_area=0
for c in combinations(split_lines,2):
    a,b = c
    ar = area(a,b)
    areas.append((ar,cc.contract(a),cc.contract(b)))
    if(ar>max_area):
        max_area= ar

print(f"result part 1: {max_area}")

areas.sort(reverse=True)


red_tiles = [cc.contract(l) for l in split_lines]

#find the perimeter
perimeter_tiles = []
for r1, r2 in pairwise(red_tiles+[red_tiles[0]]):
    for x in range(min(r1[0],r2[0]), max(r1[0],r2[0])+1):
        for y in range(min(r1[1],r2[1]), max(r1[1],r2[1])+1):
            perimeter_tiles.append((x,y))



red_tiles.sort()
start = red_tiles[0]
first_internal_node = (start[0]+1,start[1]+1)

# Flood fill into the bulk
bulk = set()
possible_bulk = set()
possible_bulk.add(first_internal_node)

while len(possible_bulk)!=0:
    node = possible_bulk.pop()
    bulk.add(node)
    for n in [(node[0]+1,node[1]), (node[0]-1,node[1]), (node[0],node[1]+1), (node[0],node[1]-1)]:
        if n not in bulk and n not in perimeter_tiles:
            possible_bulk.add(n)

good_tiles = set(red_tiles)
good_tiles = good_tiles.union(perimeter_tiles)
good_tiles = good_tiles.union(bulk)

def is_valid(ac,bc):
    if (ac[0],bc[1]) not in good_tiles:
                return False
    if (bc[0],ac[1]) not in good_tiles:
                return False
    for x in range(min(ac[0],bc[0]), max(ac[0],bc[0])):
        for y in range(min(ac[1],bc[1]), max(ac[1],bc[1])):
            if (x,y) not in good_tiles:
                return False
    return True

for ar,ac,bc in areas:
            
    if is_valid(ac,bc):
        print(f"result part 2: {ar}")
        break
