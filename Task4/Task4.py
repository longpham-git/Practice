"""
 step 1: every new line is a new passport
 step 2: valid is 8 (7 + optional cid)
 step 3: If valid '#' increase counter
 optional: smallest eyr is taken into account as "this" year
"""

with open('data.txt', 'r') as data:
    lines = data.readlines()
valid_cnt = 0
field_cnt = 0
min_eyr = 9999
mandatory_field = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
for line in lines:
    if line == '\n':
        field_cnt = 0
    else:
        line = line.strip()
        for field in mandatory_field:
            if field in line:
                field_cnt += 1
                if field == 'eyr:':
                    expire = int(line.split('eyr:')[1].split()[0])
                    min_eyr = expire if expire < min_eyr else min_eyr
        if field_cnt == 7:
            valid_cnt += 1
            field_cnt = 0

print(f'If this year is {min_eyr}, # of valid passport is: {valid_cnt}')
