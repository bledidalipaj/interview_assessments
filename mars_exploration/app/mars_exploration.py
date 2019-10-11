def change_direction(direction, move):
    if move == 'L':
        if direction == 'N':
                direction = 'E'
        elif direction == 'W':
            direction = 'N'
        elif direction == 'S':
            direction = 'W'
        elif direction == 'E':
            direction = 'S'
    elif move == 'R':
        if direction == 'N':
                direction = 'W'
        elif direction == 'W':
            direction = 'S'
        elif direction == 'S':
            direction = 'E'
        elif direction == 'E':
            direction = 'N'

    return direction


def find_rover_position(initial_position, facing_direction, moves, grid):
    x, y = initial_position 

    # available_directions = ['N', 'W', 'S', 'E']
    
    for index, move in enumerate(moves):
        if move != 'M':
            facing_direction = change_direction(facing_direction, move)
        else:
            # we are moving - move == 'M'
            if facing_direction == 'N':
                # check if we can make the move
                if y < grid[1]:
                    y += 1
            elif facing_direction == 'W':
                # check if we can make the move
                if x < grid[0]:
                    x += 1 
            elif facing_direction == 'S':
                # check if we can make the move
                if y > 0:
                    y -= 1
            elif facing_direction == 'E':
                # check if we can make the move
                if x > 0:
                    x -= 1
    # given rover's position check and the direction of the move
    # check if the rover is allowed to make the move

    return [x, y, facing_direction]


# Example
# Test input:
# 5 5
# 1 2 N
# LMLMLMLMM
# 3 3 E
# MMRMMRMRRM
# Test output:
# 1 3 N
# 5 1 E

# find_rover_position(initial_position, facing_direction, moves, grid)
print(find_rover_position([1, 2], 'N', 'LMLMLMLMM', [5, 5]))
print(find_rover_position([3, 3], 'E', 'MMRMMRMRRM', [5, 5]))
print(find_rover_position([0, 0], 'N', 'MMMMMMLMM', [5, 5]))
