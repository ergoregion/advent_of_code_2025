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



def solve(current, options, target, total):
     if (target==current).all():
        return total
     if len(options) ==0:
         return None
     
     solve_without_option_1 = solve(current, options[1:], target, total)
     solve_with_option_1 = solve(current*options[0], options[1:], target, total+1)
     if solve_without_option_1 is not None and solve_with_option_1 is not None:
         return min(solve_without_option_1,solve_with_option_1)
     elif solve_without_option_1 is not None:
         return solve_without_option_1
     elif solve_with_option_1 is not None:
         return solve_with_option_1
     else:
         return None
     
sum =0 

for p in problems:
    target = p[0]
    options=p [1]
    current = [-1 for i in target]
    s = solve(current, options, target, 0)
    sum += s
print(f"result part 1: {sum}")


from scipy.optimize import linprog

sum =0 


for p in problems:
    target = np.array(p[2])
    options=p [3]

    minimise =np.array([1 for i in options])
        
    A = np.array(options).T
    bounds = [(0,None) for _ in options]
    res = linprog(minimise, A_eq=A, b_eq=target, bounds=bounds, integrality=1)
    sum += res.fun
print(f"result part 2: {int(sum)}")