"""
Suppose you have the following list:
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given letter must appear for the password
    to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
    but needs at least 1. The first and third passwords are valid: they contain one a or nine c,
    both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

with open('d2.txt', 'r') as data:
    lines = data.readlines()
valid_counter = 0
for line in lines:
    min_val = line.strip().split()[0].split('-')[0]
    max_val = line.strip().split()[0].split('-')[1]
    key = line.strip().split()[1].removesuffix(':')
    password = line.strip().split()[2]
    if (password.count(key) >= int(min_val)) and (password.count(key) <= int(max_val)):
        # print(f'min = {min_val} max = {max_val} key = {key} cnt = {password.count(key)} password = {password}')
        valid_counter = valid_counter + 1

print(f'Total valid password: {valid_counter}')
