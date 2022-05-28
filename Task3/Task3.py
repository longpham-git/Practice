"""
 step 1: Extend the tree if next location > current line length
 step 2: only from line 1 is taken to account -> remove line 0
 step 3: If a location is '#' increase counter
"""

with open('data.txt', 'r') as data:
    lines = data.readlines()
tree_counter = 0
next_location = 0
del lines[0]
for line in lines:
    line = line.strip()
    next_location += 3
    extension_factor = int(next_location / len(line))+1
    if len(line) < next_location:
        line = line * extension_factor
    # print(line)
    # print(f'location {next_location} is {line[next_location]}')
    if line[next_location] == '#':
        # print("hit a tree")
        tree_counter += 1

print(f'Total tree encounter: {tree_counter}')
