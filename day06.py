with open('data/day06_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day06.txt', 'r') as file:
    real_lines = file.readlines()


lines = test_lines
lines = real_lines
split_lines = [l.split() for l in lines]

def product(iter):
    result = 1
    for i in iter:
        result *= i
    return result


print(split_lines)

length = len(split_lines[-1])

result = 0
for item in range(length):
    operation = split_lines[-1][item]
    if operation == '+' :
        items = [int(l[item]) for l in split_lines[:-1]]
        print(items)
        result += sum(int(l[item]) for l in split_lines[:-1])
    if operation == '*' :
         result += product(int(l[item]) for l in split_lines[:-1])

print(f"result part 1: {result}")


def score_of_block(block):
    length = len(block[-1])
    operator = block[-1][0]
    items = [int("".join(b[i] for b in block[:-1])) for i in range(length)]
    print(items)
    if operator == '+' :
        return sum(items)
    if operator == '*' :
         return product(items)

keynotes = []
for i,sym in enumerate(lines[-1]):
    if sym != ' ':
        keynotes.append(i)
keynotes.append(len(lines[-1])+1)
print(keynotes)

result =0 
for i in range(len(keynotes)-1):
    k1=keynotes[i]
    k2=keynotes[i+1]-1
    block = [l[k1:k2] for l in lines]
    s = score_of_block(block)
    print(s)
    result += s

print(f"result part 2: {result}")
