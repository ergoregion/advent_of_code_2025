with open('data/day11_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day11.txt', 'r') as file:
    real_lines = file.readlines()

lines = test_lines
lines = real_lines


split_lines = [l.split(':') for l in lines]

print(split_lines)

nodes = []
edges = []

for key, value in split_lines:
    nodes.append(key)

    outputs = value.split()
    for o in outputs:
        e = (key,o)
        edges.append(e)

nodes.append('out')


destinations_from_node = dict((n, []) for n in nodes)
for edge in edges:
    destinations_from_node[edge[0]].append(edge[1])



routes_to_out_cache ={}

def routes_to_out(start):
    if start == 'out':
        return 1
    if start not in routes_to_out_cache:
        r = sum(routes_to_out(n) for n in destinations_from_node[start])
        routes_to_out_cache[start] = r  
    return routes_to_out_cache[start] 

print(f"result part 1: {routes_to_out('you')}")


routes_to_fft_cache ={}

def routes_to_fft(start):
    if start == 'fft':
        return 1
    if start not in routes_to_fft_cache:
        r = sum(routes_to_fft(n) for n in destinations_from_node[start])
        routes_to_fft_cache[start] = r
    
    return routes_to_fft_cache[start] 

phase_1 = routes_to_fft('svr')

# This observation reduced the time
assert(routes_to_fft('dac') == 0)

routes_to_dac_cache ={}

def routes_to_dac(start):
    if start == 'dac':
        return 1
    if start not in routes_to_dac_cache:
        r = sum(routes_to_dac(n) for n in destinations_from_node[start])
        routes_to_dac_cache[start] = r
    
    return routes_to_dac_cache[start] 

phase_2 = routes_to_dac('fft')



phase_3 = routes_to_out('dac')



print(f"result part 2: {phase_1*phase_2*phase_3}")