with open('data/day02_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day02.txt', 'r') as file:
    real_lines = file.readlines()

# print(test_lines)
# print(real_lines)

lines = real_lines


id_pairs = lines[0].split(',')

ids = [l.split('-') for l in id_pairs]
print(ids)


def test_valid(id):
    id = str(id)
    l = len(id)
    if (l % 2 != 0):
        return True
    half_l = l//2
    if (id[:half_l] == id[half_l:]):
        return False
    return True





result = 0

for a, b in ids:
    for i in range(int(a), int(b)+1):

        if not test_valid(i):
            print(i)
            result += i

print(f"result part 1 {result}")



def test_valid_part_2(id):
    id = str(id)
    length = len(id)
    for batch_size in range(1, length):
        if (length % batch_size == 0):
            times = length//batch_size
            batches = [id[i*batch_size:(i+1)*batch_size] for i in range(times)]
            if len(set(batches))==1:
                return False      

    return True


result = 0

for a, b in ids:
    for i in range(int(a), int(b)+1):

        if not test_valid_part_2(i):
            print(i)
            result += i

print(f"result part 2 {result}")
