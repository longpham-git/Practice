"""
Calculate expense report by 3 entries from a list
For example, suppose your expense report contained the following:
1721
979
366
299
675
1456
The three entries that sum to 2020 are 979, 366, and 675.
Multiplying them together produces the answer, 241861950.
the Output:
Your puzzle answer was 241861950.
"""

TARGET_SUM = 2020

with open('data.txt', 'r') as data:
    lines = data.readlines()

modified_list = lines[:]
result = 'NOT DONE'
for line in lines:
    first_number = int(line.strip())
    reminder_sum = TARGET_SUM - first_number
    del modified_list[0]
    for in_line in modified_list:
        second_number = int(in_line.strip())
        third_number = reminder_sum - second_number
        if str(third_number)+'\n' in modified_list:
            expense_report = first_number * second_number * third_number
            result = ' DONE'
            print(f'Your puzzle answer was {expense_report}.')
            break
    if result == 'DONE':
        # print(f'First {first_number} Second{second_number} Third {third_number}')  # Debug code
        break
