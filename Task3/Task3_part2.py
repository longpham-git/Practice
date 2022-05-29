"""
 step 1: Extend the tree if next location > current line length
 step 2: only from line 1 is taken to account -> remove line 0
 step 3: If a location is '#' increase counter
"""

with open('data.txt', 'r') as data:
    lines = data.readlines()
product = 1
slopes = ['1-1', '3-1', '5-1', '7-1', '1-2']
#slopes = ['3-1']
del lines[0]
iter_lines = iter(lines)
for slope in slopes:
    print(slope)
    right, down = int(slope.split('-')[0]), int(slope.split('-')[1])
    down_slope = down
    tree_counter, next_location = 0, 0
    iter_lines = iter(lines)
    for line in iter_lines:
        while down_slope > 1:
            down_slope -= 1
            next(iter_lines)
        down_slope = down
        line = line.strip()
        next_location += right
        extension_factor = int(next_location / len(line))+1
        if len(line) <= next_location:
            line = line * extension_factor
            print(line)
            print(f'location {next_location} is {line[next_location]}')
        if line[next_location] == '#':
            # print("hit a tree")
            tree_counter += 1
    print(tree_counter)
    product = product * tree_counter

print(f'Total tree encounter: {product}')

