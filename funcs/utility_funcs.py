
def depth_measurement(previous_measurement, depth, increased, decreased):
    if previous_measurement and depth > previous_measurement:
        increased = increased + 1
        print(depth, 'increased')
    elif previous_measurement:
        decreased = decreased + 1
        print(depth, 'decreased')

    if previous_measurement == False:
        print(depth, 'N/A - no previous measurement')
        pass

    previous_measurement = depth
    return (previous_measurement, increased, decreased) 