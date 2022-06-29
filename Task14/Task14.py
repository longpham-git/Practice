def string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


with open('data.txt', 'r') as data:
    lines = data.readlines()

memory = dict()
for line in lines:
    line = line.strip().split()
    if 'mask' in line[0]:
        mask = string_to_list(line[2])
    else:
        address = line[0].split('[')[1].split(']')[0]
        value = string_to_list(str(bin(int(line[2]))).split('b')[1].zfill(36))
        for n, bitmask in enumerate(mask):
            if bitmask != 'X':
                value[n] = bitmask
        value = int(''.join(value), 2)
        memory[address] = value
summary = 0
for add in memory:
    summary += memory[add]
print(summary)