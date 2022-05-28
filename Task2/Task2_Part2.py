"""
Each policy actually describes two positions in the password, where 1 means the first character,
    2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
    Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant
    for the purposes of policy enforcement.
Given the same example list from above:
•	1-3 a: abcde is valid: position 1 contains a and position 3 does not.
•	1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
•	2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

with open('d2.txt', 'r') as data:
    lines = data.readlines()
valid_counter = 0
for line in lines:
    first_place = int(line.strip().split()[0].split('-')[0])
    second_place = int(line.strip().split()[0].split('-')[1])
    key = line.strip().split()[1].removesuffix(':')
    password = '0' + line.strip().split()[2]  # Password is letter and always start at 1
    if second_place <= len(password):
        if (password[first_place] == key) ^ (password[second_place] == key):
            valid_counter += 1

print(f'Total valid password: {valid_counter}')
