"""
 step 1: Combine the string
 step 2: set that string
 step 3: count string length
"""

with open('data.txt', 'r') as data:
    lines = data.readlines()

print(lines)
location = 0
instruction_list =[]
loop_flag = 0
acc = 0
while loop_flag != 1:
    if instruction_list.count(location) == 2:
        loop_flag = 1
    else:
        parameter = int(lines[location].strip().split()[1])
        print(f'{location}  {acc} {instruction_list} {lines[location]}')
        if 'acc' in lines[location]:
            acc += parameter
            location += 1
        elif 'jmp' in lines[location]:
            location += parameter
        else:  # nop
            location += 1
    instruction_list.append(location)
else:
    print(f'Accumulate before loop is: {acc}')
