from funcs.utility_funcs import depth_measurement


with open('data/day-1.txt') as f:

    increased = 0
    decreased = 0
    previous_measurement = False

    for line in f:
        depth = int(line)        

        (previous_measurement, increased, decreased) = depth_measurement(previous_measurement, depth, increased, decreased)
        
    print('TOTAL Increased', increased)
    print('TOTAL Decreased', decreased)