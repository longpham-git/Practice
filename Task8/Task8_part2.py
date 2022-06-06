"""
 step 1: Combine the string
 step 2: set that string
 step 3: count string length
"""

with open('test_data.txt', 'r') as data:
    lines = data.readlines()

location = 0
instruction_list = []
jmp_nop_list = []
loop_flag = 0
done = 0
acc = 0
while loop_flag != 1:
    parameter = int(lines[location].strip().split()[1])
    #print(f'{location}  {acc} {instruction_list} {lines[location]}')
    if 'acc' in lines[location]:
        acc += parameter
        location += 1
    elif 'jmp' in lines[location]:
        jmp_nop_list.append(location)
        location += parameter
    else:  # nop
        jmp_nop_list.append(location)
        location += 1
    instruction_list.append(location)
    if instruction_list.count(location) == 2:
        loop_flag = 1
else:
    print(f'Accumulate before loop is:{location} {acc}')
    print(jmp_nop_list)

location = 0
instruction_list = []
loop_flag = 0
done = 0
acc = 0
while done != 1:
    change_location = jmp_nop_list.pop()
    temp_lines = list(lines)
    print(temp_lines[change_location])
    if 'jmp' in temp_lines[change_location]:
        temp_lines[change_location] = temp_lines[change_location].replace('jmp', 'nop')
    else:
        temp_lines[change_location] = temp_lines[change_location].replace('nop', 'jmp')
    print(temp_lines[location])
    location = 0
    loop_flag = 0
    acc = 0
    instruction_list = []
    while loop_flag != 1:
        print(f'{location}  {acc} {instruction_list} {lines[location]}')
        parameter = int(temp_lines[location].strip().split()[1])
        if 'acc' in temp_lines[location]:
            acc += parameter
            location += 1
        elif 'jmp' in temp_lines[location]:
            location += parameter
        else:  # nop
            location += 1
        if location == len(lines):
            print(f'Accumulate at the end after change instruction at {change_location} is : {acc}')
            done = 1
            loop_flag = 1
        instruction_list.append(location)
        if instruction_list.count(location) == 2:
            loop_flag = 1
