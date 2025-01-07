#The following code will help the robot to escape the maze at Reborg's World challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()

turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()