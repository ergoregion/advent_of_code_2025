with open('data/day10_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day10.txt', 'r') as file:
    real_lines = file.readlines()


lines = test_lines
lines = real_lines

import re

splits = [re.findall(r'\[(.*?)\]|\((.*?)\)|\{(.*?)\}', text) for text in lines]

print(splits)

obvectives = [re.findall(r'\[(.*?)\]', text) for text in lines]

schematics  = [re.findall(r'\((.*?)\)', text) for text in lines]

requirements  = [re.findall(r'\{(.*?)\}', text) for text in lines]

import numpy as np

problems = []
for i in range(len(splits)):
    o = np.array([1 if c =='#' else -1  for c in obvectives[i][0]], dtype=int)
    size = len(o)
    s = [list(map(int,l.split(','))) for l in schematics[i]]
    s1 = [np.array([-1 if d in item else 1 for d in range(size)], dtype=int) for item in s]
    s2 = [np.array([1 if d in item else 0 for d in range(size)], dtype=int) for item in s]

    problems.append(( o,s1 ,list(map(int,requirements [i][0].split(','))), s2))

print(problems)









from z3 import *

total = 0

for p in problems:

    target = np.array(p[2])
    options=p [3]


    # Create integer variables
    ints = [Int(io) for io, _ in enumerate(options)]
    
    cost = Int('cost')

    constraints = []
    for it, _ in enumerate(target):
        c= sum([ints[j]*o[it] for j, o in enumerate(options)])== target[it]
        constraints.append(c)

    
    c= sum([ints[j]*1 for j, o in enumerate(options)])== cost
    constraints.append(c)

    for i in ints:
        constraints.append(i>=0)
    # Create a solver
    solver = Optimize()
    solver.minimize(cost)

    solver.add(constraints)
        
    print (solver.check())

    m = solver.model()

    for d in m.decls():
        print ("%s = %s" % (d.name(), m[d]))
    total += m[cost].as_long()

print(f"result part 2: {total}")

#16360 - too low

#16758 - too high