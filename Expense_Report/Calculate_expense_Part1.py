"""
Calculate expense report by 2 entries from a list
For example, suppose your expense report contained the following:
1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
the Output:
Your puzzle answer was 514579.
"""

TARGET_SUM = 2020

with open('data.txt', 'r') as data:
    lines = data.readlines()

for line in lines:
    first_number = int(line.strip())
    second_number = TARGET_SUM - first_number  # second number is subtraction of TARGET_SUM and current number
    if str(second_number)+'\n' in lines:  # If second number in the list then perform calculation
        expense_report = first_number * second_number
        break

print(f'Your puzzle answer was {expense_report}.')
