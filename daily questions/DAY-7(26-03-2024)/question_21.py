'''A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
'''
from math import sqrt

x,y=0,0
while True:
    direction = input("Enter your direction:").split(' ')
    match direction[0]:
        case "UP":
            x += int(direction[1])
        case "DOWN":
            x -= int(direction[1])
        case "LEFT":
            y += int(direction[1])
        case "RIGHT":
            y -= int(direction[1])
        case _:
            break

print(round(sqrt(x**2 + y**2)))