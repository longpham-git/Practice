LEFT = ['E', 'N', 'W', 'S', 'E', 'N', 'W']
RIGHT = ['E', 'S', 'W', 'N', 'E', 'S', 'W']

with open('data.txt', 'r') as data:
    lines = data.readlines()

current_facing = 'E'
location = {'E': 0, 'N': 0, 'W': 0, 'S': 0}
for line in lines:
    line = line.strip()
    command = line[0]
    parameter = int(line[1:])
    print(f'command{ command} parameter {parameter}')
    if command == 'F':
        location[current_facing] += parameter
    elif command == 'L':
        current_facing = LEFT[LEFT.index(current_facing) + int(parameter/90)]
    elif command == 'R':
        current_facing = RIGHT[RIGHT.index(current_facing) + int(parameter/90)]
    else:
        location[command] += parameter

print(location)
print(abs(location['E'] - location['W'])+abs((location['N'] - location['S'])))
