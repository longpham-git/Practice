"""
123
405
678
"""
CHECK_LIST = ["L", "#", "L\n", "#\n"]


def find_related_seat(row, col, arr):
    # 1
    one = two = three = four = five = six = seven = eight = ""
    subs = 1
    while (row - subs >= 0) and (col - subs >= 0):
        if arr[row - subs][col - subs] in CHECK_LIST:
            one = arr[row - subs][col - subs]
            break
        else:
            subs += 1
    # 2
    subs = 1
    while row - subs >= 0:
        if arr[row - subs][col] in CHECK_LIST:
            two = arr[row - subs][col]
            break
        else:
            subs += 1
    # 3
    subs = 1
    while (row - subs >= 0) and (col + subs < len(arr[row].strip())):
        if arr[row - subs][col + subs] in CHECK_LIST:
            three = arr[row - subs][col + subs]
            break
        else:
            subs += 1
    # 4
    subs = 1
    while col - subs >= 0:
        if arr[row][col - subs] in CHECK_LIST:
            four = arr[row][col - subs]
            break
        else:
            subs += 1
    # 5
    subs = 1
    while col + subs < len(arr[row].strip()):
        if arr[row][col + subs] in CHECK_LIST:
            five = arr[row][col + subs]
            break
        else:
            subs += 1
    # 6
    subs = 1
    while (row + subs < len(arr)) and (col - subs >= 0):
        if arr[row + subs][col - subs] in CHECK_LIST:
            six = arr[row + subs][col - subs]
            break
        else:
            subs += 1
    # 7
    subs = 1
    while row + subs < len(arr):
        if arr[row + subs][col] in CHECK_LIST:
            seven = arr[row + subs][col]
            break
        else:
            subs += 1
    # 8
    subs = 1
    while (row + subs < len(arr)) and (col + subs < len(arr[row].strip())):
        if arr[row + subs][col + subs] in CHECK_LIST:
            eight = arr[row + subs][col + subs]
            break
        else:
            subs += 1
    return one+two+three+four+five+six+seven+eight


with open('data.txt', 'r') as data:
    lines = data.readlines()
matrix = dict()
new_list = list(lines)
done = 0

while done == 0:
    for i in range(len(lines)):
        curr_row = lines[i].strip()
        for j in range(len(curr_row)):
            check = find_related_seat(i, j, lines)
            if (curr_row[j] == 'L') & ('#' not in check):
                temp = list(new_list[i])
                temp[j] = '#'
                new_list[i] = ''.join(temp)
            if (curr_row[j] == '#') & (check.count('#') >= 5):
                temp = list(new_list[i])
                temp[j] = 'L'
                new_list[i] = ''.join(temp)
            #print(f'upper {upper} this_ln {this_ln} lower {lower} Check {check}')
            #print(new_list)
    i = 0
    j = 0
    if lines == new_list:
        done = 1
    lines = list(new_list)
count = 0
for line in lines:
    count += line.count('#')

print(count)
