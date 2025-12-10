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



#def solve_2(current, options, target, total):
#     
#     if (target==current).all():
#        return total
#     if (target<current).any():
#        return None
#     if len(options) ==0:
#         return None
#     
#     uppers = ((target-current)/options[0])
#     limit = min([u for u in uppers if not np.isnan(u)])
#
#     possibilities = [solve_2(current+i*options[0], options[1:], target, total+i) for i in reversed(range(int(limit)+1))]
#
#     possibilities = [p for p in possibilities if p is not None]
#
#     if(len(possibilities)==0):
#        return None
#
#     return min(possibilities)
#
#


#def can_solve(current, target, options, presses_left):
#    if (target==current).all():
#        return True
#    if presses_left == 0:
#        return False
#
#    for o in options:
#        if can_solve(current+o, target, options, presses_left-1):
#            return True
#    return False

from itertools import combinations, product

def solve2(target, options):

    t = len(options)
    mat = np.array(options).T

    size =target.sum()
    best = None

    def arrays_sum_to_m(N, M):
        if N == 1:
            yield [M]
            return
        for x in range(M + 1):
            for rest in arrays_sum_to_m(N - 1, M - x):
                yield [x] + rest

    def can_solve(s):

        for comb in arrays_sum_to_m(len(options), s):
            r = np.array(comb)
            if (np.matmul(mat,r)==target).all():
                return True


    for l in range(target.max(), target.sum()):
        if can_solve(l):
            return l
        else:
            print(l)



def solve_2(current, options, target, target_indecides):
     
    if (target==current).all():
       return 0
    if (target<current).any():
       return None
    if len(options) ==0:
        return None
    if len(target_indecides)==0:
        return None
    
    t= target_indecides[0]
     
    this_need = (target-current)[t]
    this_options = [o for o in options if o[t]==1]
    this_options.sort(key=lambda a:a.sum(), reverse=True)


    remaining_options = [o for o in options if o[t]==0]

    best = None
    for items in product(this_options, repeat=this_need):
        new_current = current.copy()
        for i in items:
            new_current+= i

        new_indicies = target_indecides[1:]
        new_indicies.sort(key=lambda t: (target-new_current)[t])
        a  = solve_2(new_current, remaining_options, target, new_indicies)
        if a is not None and (best is None or a<best):
            best =a
    return best+this_need if best is not None else None





sum =0 

from tqdm import tqdm

for p in tqdm(problems):
    target = np.array(p[2])
    options=p [3]
    current = np.array([0 for _ in target])
    target_indecides = list(range(len(target)))
    target_indecides.sort(key=lambda t: target[t])
    #sum += solve2(target, options)
    sum += solve_2(current, options, target, target_indecides)
    print(sum)
print(f"result part 2: {sum}")