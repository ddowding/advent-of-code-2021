
with open('data/day-1.txt') as f:

    increased = 0
    decreased = 0
    previous_measurement = False

    for line in f:
        depth = int(line)        

        if previous_measurement and depth > previous_measurement:
            increased = increased + 1
            print(depth, 'increased')
        elif previous_measurement:
            decreased = decreased + 1
            print(depth, 'decreased')

        if previous_measurement == False:
            print(depth, 'N/A - no previous measurement', )
            pass

        previous_measurement = depth

        
    print('TOTAL Increased', increased)
    print('TOTAL Decreased', decreased)