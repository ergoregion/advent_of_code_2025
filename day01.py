with open('data/day01_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day01.txt', 'r') as file:
    real_lines = file.readlines()

# print(test_split_lines)
# print(real_split_lines)

lines = real_lines


print(test_lines)

count = 0
dial = 50
for n in lines:
    sign = -1 if n[0] == 'L' else 1
    value = int(str(n[1:]))

    dial = (dial + (sign * value)) % 100
    if (dial == 0):
        count = count+1

print(count)

count = 0
dial = 50
for n in lines:
    sign = -1 if n[0] == 'L' else 1
    value = int(str(n[1:]))
    for _ in range(value):
        dial = (dial + (sign * 1)) % 100
        if (dial == 0):
            count = count+1

print(count)
