"""
 step 1: seat from 0-127 and 0-7 matched with binary value
 step 2: replace current data with binary
 optional: keep the dictionary of row and column for debugging
"""

with open('data.txt', 'r') as data:
    lines = data.readlines()

max_id = 0
seat_list = []
seat_dict = {}
for line in lines:
    line = line.strip()
    x = line.replace("F", "0")
    x = x.replace("B", "1")
    x = x.replace("R", "1")
    x = x.replace("L", "0")
    row = int(x[:7], 2)
    column = int(x[7:], 2)
    seat_id = row * 8 + column
    seat_dict[seat_id] = str(row) + '-' + str(column)
    seat_list.append(seat_id)
    if seat_id > max_id:
        max_id = seat_id
print(f'The highest seat ID is {max_id}')

for line in seat_list:
    if (line + 1 not in seat_list) and (line + 2 in seat_list):
        print(f'Your seat ID is {line + 1}')

