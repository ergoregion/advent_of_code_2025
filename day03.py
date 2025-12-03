with open('data/day03_test.txt', 'r') as file:
    test_lines = file.readlines()

with open('data/day03.txt', 'r') as file:
    real_lines = file.readlines()


#lines = test_lines
lines = real_lines


print(test_lines)

banks = lines

result=0
for bank in banks:
    batteries = [int(i) for i in list(bank.strip())]
    print(batteries)
    biggest_tens_value = max(batteries[:-1])
    biggest_tens_index = batteries.index(biggest_tens_value)
    biggest_units_value = max(batteries[biggest_tens_index+1:])
    biggest_units_index = batteries.index(biggest_units_value)
    print(biggest_tens_value, biggest_units_value)
    output = 10*biggest_tens_value+biggest_units_value
    result =result+output
print(f"result part 1 {result}")

total_times=12


result=0
for bank in banks:
    batteries = [int(i) for i in list(bank.strip())]
    used_index= 0
    for i in range(total_times):
        reemaining_digets = total_times-i-1
        new_array = batteries[used_index:] if reemaining_digets==0 else batteries[used_index:-reemaining_digets]
        biggest_value  = max(new_array)
        at_index =new_array.index(biggest_value)
        used_index = used_index+1+at_index

        print(biggest_value)
        output = pow(10,reemaining_digets) *biggest_value
        result =result+output
print(f"result part 2 {result}")