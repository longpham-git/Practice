
with open('data.txt', 'r') as data:
    lines = data.readlines()

# print(lines)
done = 0
i = 25
shift = 0
ok_flag = 0
error_location = 0
while done != 1:
    target_num = int(lines[i].strip())
    ok_flag = 0
    for number in lines[shift:i]:
        second_number = target_num - int(number)
        if (str(second_number)+'\n' in lines[shift:i]) and second_number != int(number):
            ok_flag = 1
            break
    # print(f'target = {target_num} number = {number.strip()} second {second_number} ok flag {ok_flag}')
    if ok_flag != 1:
        done = 1
        print(f"Part 1: {target_num}")
        error_location = i
    if i < len(lines) - 1:
        i += 1
    shift += 1
done = 0
shift = 0
contiguous_set = []
total = 0
while done != 1:
    for n, number in enumerate(lines[shift:error_location]):
        total = total + int(number)
        contiguous_set.append(int(number))
        if total == target_num:
            done = 1
            break
        elif total > target_num:
            total = 0
            contiguous_set = []
            shift += 1
            break

print(f'Part 2:{min(contiguous_set) + max(contiguous_set)}')