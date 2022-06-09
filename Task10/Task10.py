
with open('data.txt', 'r') as data:
    lines = data.readlines()

int_list = []
for line in lines:
    line = int(line.strip())
    int_list.append(line)

highest_jolts = max(int_list)
current_jolts = 0
one_jolt = 0
three_jolt = 0
done = 0
while done != 1:
    print(current_jolts)
    if current_jolts + 1 in int_list:
        current_jolts += 1
        one_jolt += 1
    elif current_jolts + 2 in int_list:
        current_jolts += 2
    elif current_jolts + 3 in int_list:
        current_jolts += 3
        three_jolt += 1
    if current_jolts == highest_jolts:
        three_jolt += 1
        done = 1

print(f'one_jolt {one_jolt} three jolt {three_jolt}')
print(one_jolt*three_jolt)