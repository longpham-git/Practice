"""
 step 1: Combine the string
 step 2: set that string
 step 3: count string length
"""

with open('data.txt', 'r') as data:
    lines = data.readlines()

group = ''
total = 0
print(len(lines))
for n, line in enumerate(lines):
    if line == '\n':
        print(f'all answer {group} sum of {set(group)} is {len(set(group))}')
        group_answer = len(set(group))
        group = ''
        total = total + group_answer
    else:
        line = line.strip()
        group = group + line
    if n == len(lines)-1:
        print(f'all answer {group} sum of {set(group)} is {len(set(group))}')
        group_answer = len(set(group))
        group = ''
        total = total + group_answer

print(total)
group_mem_cnt = 0
group = ''

total = 0
for n, line in enumerate(lines):
    if line == '\n':
        group_answer = 0
        for char in set(group):
            if group.count(char) == group_mem_cnt:
                group_answer += 1
        group = ''
        print(group_answer)
        group_mem_cnt = 0
        total = total + group_answer
    else:
        line = line.strip()
        group_mem_cnt += 1
        group = group + line
    if n == len(lines)-1:
        group_answer = 0
        for char in set(group):
            if group.count(char) == group_mem_cnt:
                group_answer += 1
        print(group_answer)
        group = ''
        group_mem_cnt = 0
        total = total + group_answer

print(total)