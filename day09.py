with open('data/day09_test.txt', 'r') as file:
    test_split_lines = [i.split() for i in file.readlines()]

with open('data/day09.txt', 'r') as file:
    real_split_lines = [i.split() for i in file.readlines()]

print(test_split_lines)
print(real_split_lines)

split_lines = test_split_lines
# split_lines = real_split_lines
