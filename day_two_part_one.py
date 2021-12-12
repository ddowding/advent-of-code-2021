from funcs.utility_funcs import depth_measurement

with open('data/day-2.txt') as f:

    position = 0
    depth = 0

    lines = f.readlines()

    for index in range(len(lines)):
        row_values = lines[index].split(' ')
        direction = row_values[0]
        distance = int(row_values[1])

        if direction == 'forward':
            position = position + distance
        if direction == 'up':
            depth = depth - distance
        if direction == 'down':
            depth = depth + distance

    print('END position', position)
    print('END Depth', depth)

    print('FINAL horizontal position', position*depth)


        
 