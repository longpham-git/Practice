"""
 step 1: Combine the string
 step 2: set that string
 step 3: count string length
"""


def get_list(in_list):
    out_list = []
    for raw_line in in_list:
        if len(raw_line) > 3:
            raw_line = raw_line.split()
            out_list.append(raw_line[2] + ' ' + raw_line[3])
    return out_list


def get_bag_value(in_list):
    sum_bag_val = 0
    for raw_line in in_list:
        if len(raw_line) > 3:
            raw_line = raw_line.split()
            bag_name = raw_line[2] + ' ' + raw_line[3]
            if bag_name in bag_content_dict:
                bag_val = bag_content_dict[bag_name]
                sum_bag_val = sum_bag_val + int(raw_line[1]) * (bag_val + 1)
            else:
                return 0
    return sum_bag_val


with open('test_data.txt', 'r') as data:
    lines = data.readlines()

find_list = ['shiny gold']
out_bag_list = set()
new_list = []
while len(find_list) > 0:
    new_list = []
    for bag in find_list:
        for line in lines:
            line = line.strip()
            out_bag = line.split(' bags contain')[0]
            in_bag = line.split(' bags contain')[1]
            if bag in in_bag:
                print(line)
                out_bag_list.add(out_bag)
                new_list.append(out_bag)
    find_list = new_list

print(len(out_bag_list))

find_list = ['shiny gold']
target_bags = ['shiny gold']
new_list = []
bag_content_dict = dict()
i = 0
while len(find_list) > 0:
    new_find_list = []
    for bag in find_list:
        A = []
        for line in lines:
            line = line.strip()
            out_bag = line.split(' bags contai')[0]
            in_bags = line.split(' bags contai')[1]
            if bag in out_bag:
                if 'no other' in in_bags:
                    bag_content_dict[bag] = 0
                else:
                    in_bags = in_bags.split('bag')
                    print(line)
                    target_bags = target_bags + get_list(in_bags)
                    A = A + get_list(in_bags)
                    new_find_list = new_find_list + A
                    print(new_find_list)
    find_list = new_find_list
print(f'{len(set(target_bags))} {set(target_bags)}')
#target_bags = ['posh black']
while len(bag_content_dict) != len(set(target_bags)):
    for bag in set(target_bags):
        for line in lines:
            line = line.strip()
            out_bag = line.split(' bags contai')[0]
            in_bags = line.split(' bags contai')[1]
            if bag in out_bag:
                if bag not in bag_content_dict:
                    in_bags = in_bags.split('bag')
                    if get_bag_value(in_bags) != 0:
                        bag_content_dict[bag] = get_bag_value(in_bags)
print(f'{len(bag_content_dict)} {bag_content_dict}')

for line in ['shiny gold bags contain 2 light chartreuse bags, 2 drab black bags, 1 bright orange bag, 1 shiny teal bag.']:
    out_bag = line.split(' bags contai')[0]
    in_bags = line.split(' bags contai')[1]
    bag = 'shiny gold'
    if bag in out_bag:
        in_bags = in_bags.split('bag')
        if get_bag_value(in_bags) != 0:
            bag_content_dict[bag] = get_bag_value(in_bags)