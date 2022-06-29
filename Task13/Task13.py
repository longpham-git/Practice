with open('data.txt', 'r') as data:
    lines = data.readlines()

earliest_time = int(lines[0].strip())
buses = set(lines[1].strip().split(','))
print(f'earliest_time { earliest_time} buses {buses}')
closest_time = earliest_time*2
leave_time = 0
for bus in buses:
    if bus != 'x':
        bus = int(bus)
        leave_time = (int(earliest_time/bus)+1)*bus
        print(f'1212leave_time {leave_time} bus {bus} {closest_time}')
        if leave_time <= closest_time:
            closest_time = leave_time
            chosen_bus = bus
            print(f'leave_time {leave_time} bus {bus} {closest_time}')

print(f'closest_time { closest_time} chosen_bus {chosen_bus}')
print(f'wait for {closest_time - earliest_time} for bus {chosen_bus} = {(closest_time - earliest_time)*chosen_bus}')
