
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


def invalid_ids_in_batch(batch_length, batch_number):
    for batch in range(pow(10, batch_length-1), pow(10, batch_length)):
        r = int(str(batch)*batch_number)
        yield r


def invalid_ids_of_length(number_of_digets, batch_number_limit):
    for batch_length in range(1, number_of_digets):
        batch_number, m = divmod(number_of_digets, batch_length)
        if m == 0 and (batch_number_limit is None or batch_number <= batch_number_limit):
            for item in invalid_ids_in_batch(batch_length, batch_number):
                yield item


def invalid_ids(lower_limit, upper_limit, batch_number_limit):
    min_digets = len(str(lower_limit))
    max_digets = len(str(upper_limit))
    for number_of_digets in range(min_digets, max_digets+1):
        for r in invalid_ids_of_length(number_of_digets, batch_number_limit):
            if r > upper_limit:
                continue
            if (lower_limit <= r):
                yield r


result_1 = sum(sum(set(invalid_ids(int(a), int(b), 2))) for a, b in ids)

print(f"result part 1 {result_1}")


result_2=sum(sum(set(invalid_ids(int(a), int(b), None))) for a, b in ids)

print(f"result part 2 {result_2}")

