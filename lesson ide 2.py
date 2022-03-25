map1 =  [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24]
]
map2 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 24]
]
map3 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [24, 0, 0, 0]
]
map = map3

# define starting positions
start_position_x = 0
start_position_y = 0

# define function to make moves
def move(step, current_position_x, current_position_y):
    print("Current step is: ", step)
    print("current_position_x = ", current_position_x)
    print("current_position_y = ", current_position_y)

    can_move_right = current_position_x <= 2 and map[current_position_y][current_position_x+1] == 0
    can_move_bottom = current_position_y <= 2 and map[current_position_y+1][current_position_x] == 0
    can_move_left = current_position_x <= 2 and map[current_position_y][current_position_x-1] == 0
    can_move_up = current_position_y <= 2 and map[current_position_y-1][current_position_x] == 0

    right_is_finish = current_position_x <= 2 and map[current_position_y][current_position_x+1] == 24
    bottom_is_finish = current_position_y <= 2 and map[current_position_y+1][current_position_x] == 24
    left_is_finish = current_position_x <= 2 and map[current_position_x][current_position_x-1] == 24
    up_is_finish = current_position_y <= 2 and map[current_position_y-1][current_position_x] == 24

    if right_is_finish:
        print("Found finish on right")
        return False

    if bottom_is_finish:
        print("Found finish on bottom")
        return False

    if up_is_finish:
        print("Found finish on up")
        return False
    
    if left_is_finish:
        print("Found left on right")
        return False

    if can_move_right:
        print("Should move right")
        return[current_position_x + 1, current_position_y]

    if can_move_bottom:
        print("Should move down")
        return[current_position_x, current_position_y + 1]
    
    if can_move_left:
        print("Should move left")
        return[current_position_y][current_position_x-1]

    if can_move_up:
        print("Should move up")
        return[current_position_y-1][current_position_x]

current_move_number = 1
new_position = move(current_move_number, start_position_x, start_position_y)
while new_position:
    current_move_number = current_move_number + 1
    new_position = move(current_move_number, new_position[0], new_position[1])
