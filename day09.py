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

from itertools import combinations

areas=[]
def area(a,b):
    ai, aj= a
    bi, bj = b
    return (abs(ai-bi)+1)*(abs(aj-bj)+1)

max_area=0
for c in combinations(split_lines,2):
    a,b = c
    ar = area(a,b)
    areas.append((ar,a,b))
    if(ar>max_area):
        max_area= ar

print(f"result part 1: {max_area}")

areas.sort(reverse=True)

black_listed_tiles = set()

N = len(split_lines)
for i in range(N):
    ai, aj= split_lines[(i)%N]
    bi, bj = split_lines[(i+1)%N]
    if ai==bi:
        if bj>aj:
            x= ai+1
            for y in range(aj+1, bj):
                black_listed_tiles.add((x,y))
        elif bj<aj:
            x= ai-1
            for y in range(bj+1, aj):
                black_listed_tiles.add((x,y))
    elif aj==bj:
        if bi>ai:
            y=aj-1
            for x in range(ai+1, bi):
                black_listed_tiles.add((x,y))
        elif bi<ai:
            y=aj+1
            for x in range(bi+1, ai):
                black_listed_tiles.add((x,y))


def inside_contains_key(a,b):
    for x in range(min(ai,bi)+1, max(ai,bi)):
        for y in range(min(aj,bj)+1, max(aj,bj)):
            if (x,y) in split_lines:
                return (x,y)
    return None        


def contains_bl_tile(a,b):
    ai, aj= a
    bi, bj = b
    for x in [min(ai,bi), max(ai,bi)+1]:
        for y in range(min(aj,bj), max(aj,bj)+1):
            if (x,y) in black_listed_tiles:
                return (x,y)
    for x in range(min(ai,bi), max(ai,bi)+1):
        for y in [min(aj,bj), max(aj,bj)+1]:
            if (x,y) in black_listed_tiles:
                return (x,y)
    for x in range(min(ai,bi), max(ai,bi)+1):
        for y in range(min(aj,bj), max(aj,bj)+1):
            if (x,y) in black_listed_tiles:
                return (x,y)
    return None



from tqdm import tqdm

excluded_already =  52526

for i in tqdm(range(len(areas))):
    ar,a,b = areas[i]
    if(i<excluded_already-20):
        continue
    if(inside_contains_key(a,b)is not None):
        continue
    if contains_bl_tile(a,b) is None:
        print(f"result part 2: {ar}")
        break


# max_area=0
#for c in combinations(split_lines,2):
#    a,b = c
#    print(a)
#    ar = area(a,b)
#    if(ar>max_area):
#        cbl = contains_bl_tile(a,b)
#        if cbl is None:
#            print(ar)
#            max_area= ar
#
#print(f"result part 1: {max_area}")
