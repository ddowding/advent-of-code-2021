from funcs.utility_funcs import depth_measurement

with open('data/day-1.txt') as f:

    increased = 0
    decreased = 0
    previous_measurement = False

    lines = f.readlines()

    for index in range(len(lines)):
        if index < len(lines) - 2:
            depth = int(lines[index]) + int(lines[index + 1]) + int(lines[index + 2])
        
            (previous_measurement, increased, decreased) = depth_measurement(previous_measurement, depth, increased, decreased)
 
    print('TOTAL Increased', increased)
    print('TOTAL Decreased', decreased)