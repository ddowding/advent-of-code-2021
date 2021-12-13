from funcs.utility_funcs import get_distance_and_direction

with open('data/day-2.txt') as f:

    position = 0
    depth = 0
    aim = 0

    lines = f.readlines()

    for index in range(len(lines)):
        direction, distance = get_distance_and_direction(lines, index)

        if direction == 'forward':
            position = position + distance
            aim_depth = distance * aim
            depth = depth + aim_depth
        if direction == 'up':
            aim = aim - distance
        if direction == 'down':
            aim = aim + distance

    print('END position', position)
    print('END Depth', depth)

    print('FINAL horizontal position', position*depth)


