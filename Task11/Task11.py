
with open('data.txt', 'r') as data:
    lines = data.readlines()
matrix = dict()
print(len(lines))
new_list = list(lines)
done = 0
while done == 0:
    for i in range(len(lines)):
        curr_row = lines[i].strip()
        for j in range(len(curr_row)):
            if i == 0:
                if j == 0:
                    upper = ''
                    this_ln = curr_row[j+1]
                    lower = lines[i+1].strip()[j:j+2]
                elif j < len(curr_row):
                    upper = ''
                    this_ln = curr_row[j-1:j+2].replace(curr_row[j], '', 1)
                    lower = lines[i+1].strip()[j-1:j+2]
                else:
                    upper = ''
                    this_ln = curr_row[j-1]
                    lower = lines[i+1].strip()[j-1:j+1]
            elif i < len(lines)-1:
                if j == 0:
                    upper = lines[i-1].strip()[j:j+2]
                    this_ln = curr_row[j+1]
                    lower = lines[i+1].strip()[j:j+2]
                elif j < len(curr_row):
                    upper = lines[i-1].strip()[j-1:j+2]
                    this_ln = curr_row[j-1:j+2].replace(curr_row[j], '', 1)
                    lower = lines[i+1].strip()[j-1:j+2]
                else:
                    upper = lines[i-1].strip()[j-1:j+1]
                    this_ln = curr_row[j-1]
                    lower = lines[i+1].strip()[j-1:j+1]
            else:
                if j == 0:
                    upper = lines[i-1].strip()[j:j+2]
                    this_ln = curr_row[j+1]
                    lower = ''
                elif j < len(curr_row):
                    upper = lines[i-1].strip()[j-1:j+2]
                    this_ln = curr_row[j-1:j+2].replace(curr_row[j], '', 1)
                    lower = ''
                else:
                    upper = lines[i-1].strip()[j-1:j+1]
                    this_ln = curr_row[j-1]
                    lower = ''
            check = upper + this_ln + lower
            if (curr_row[j] == 'L') & ('#' not in check):
                temp = list(new_list[i])
                temp[j] = '#'
                new_list[i] = ''.join(temp)
            if (curr_row[j] == '#') & (check.count('#') >= 4):
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
