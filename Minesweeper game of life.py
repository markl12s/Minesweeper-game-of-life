"""
Minesweeper but the mines follow the rules of Conways game of life
a turn moves ahead every time you hit a part of the board

V 1.0.0
last update: 9/11/2021

current task: set up gui
"""

import turtle, random

mine_location = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                 [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

mine_swap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

"""game of life"""

#functions/architecture
def check_cell(target_cell_x, target_cell_y):
    live_cells_nearby = 0

    # corners
    if target_cell_x == 0 and target_cell_y == 0:
        live_cells_nearby = top_left_corner()
    elif target_cell_x == -1 and target_cell_y == 0:
        live_cells_nearby = bot_left_corner()
    elif target_cell_x == 0 and target_cell_y == -1:
        top_right_corner()
    elif target_cell_x == -1 and target_cell_y == -1:
        bot_right_corner()

    # middle cells
    elif target_cell_x != 0 and target_cell_x != -1:
        if target_cell_y != 0 and target_cell_y != -1:
            live_cells_nearby = add_row(target_cell_x - 1, target_cell_y)
            live_cells_nearby += add_sides(target_cell_x, target_cell_y)
            live_cells_nearby += add_row(target_cell_x + 1, target_cell_y)

    # check if cell is alive
    if mine_location[target_cell_x][target_cell_y] == 0:
        if live_cells_nearby == 3:
            return 1
        else:
            return 0
    else:
        if live_cells_nearby == 2:
            return 1
        elif live_cells_nearby == 3:
            return 1
        else:
            return 0


def turn_check():
    live_or_dead = []
    for x in range(10):
        for y in range(10):
            dead_or_alive = check_cell(x, y)
            mine_swap[x][y] = dead_or_alive


# checking cells nearby
def add_row(middle_x, middle_y):
    row = []

    row.append(mine_location[(middle_x) % 10][(middle_y - 1) % 10])
    row.append(mine_location[(middle_x) % 10][middle_y])
    row.append(mine_location[(middle_x) % 10][(middle_y + 1) % 10])

    return sum(row)


def add_sides(middle_x, middle_y):
    row = []

    row.append(mine_location[middle_x][middle_y - 1])
    row.append(mine_location[middle_x][(middle_y + 1) % 10])

    return sum(row)


#corners
def top_left_corner():
    nearby_cells = []

    nearby_cells.append(mine_location[-1][-1])
    nearby_cells.append(mine_location[-1][0])
    nearby_cells.append(mine_location[-1][1])

    nearby_cells.append(mine_location[0][-1])
    nearby_cells.append(mine_location[0][1])

    nearby_cells.append(mine_location[1][-1])
    nearby_cells.append(mine_location[1][0])
    nearby_cells.append(mine_location[1][1])

    return sum(nearby_cells)


def bot_left_corner():
    nearby_cells = []

    nearby_cells.append(mine_location[-2][-1])
    nearby_cells.append(mine_location[-2][0])
    nearby_cells.append(mine_location[-2][1])

    nearby_cells.append(mine_location[-1][-1])
    nearby_cells.append(mine_location[-1][1])

    nearby_cells.append(mine_location[0][-1])
    nearby_cells.append(mine_location[0][0])
    nearby_cells.append(mine_location[0][1])

    return sum(nearby_cells)


def top_right_corner():
    nearby_cells = []

    nearby_cells.append(mine_location[-1][0])
    nearby_cells.append(mine_location[0][0])
    nearby_cells.append(mine_location[1][0])

    nearby_cells.append(mine_location[1][-1])
    nearby_cells.append(mine_location[-1][-1])

    nearby_cells.append(mine_location[-1][-2])
    nearby_cells.append(mine_location[0][-2])
    nearby_cells.append(mine_location[1][-2])

    return sum(nearby_cells)


def bot_right_corner():
    nearby_cells = []

    nearby_cells.append(mine_location[-1][0])
    nearby_cells.append(mine_location[0][0])
    nearby_cells.append(mine_location[1][0])

    nearby_cells.append(mine_location[-1][-1])
    nearby_cells.append(mine_location[1][-1])

    nearby_cells.append(mine_location[-1][-2])
    nearby_cells.append(mine_location[0][-2])
    nearby_cells.append(mine_location[1][-2])

    return sum(nearby_cells)

def turn():
    turn_check()
    mine_location = mine_swap

    return mine_location

"""Minesweeper"""
window = turtle.Screen()
window.bgcolor("black")
window.title("Minesweeper Conways Game of life")

uncovered_space = turtle.Turtle()
uncovered_space.shape("square")
uncovered_space.color("white")
uncovered_space.setpos(0, 0)
uncovered_space_covered = False

#design/architecture

#press uncovered space
#on mousepress
def mouse_pressed():
    if uncovered_space_covered == False:
        #if not a mine
            #uncover space
            #move game of life up one turn
            #calculate number of nearby mines to spaces
            #show numbers
        #if there is a mine
            #end game
    else:
        pass

#execution
print(mine_location)

while True:
    uncovered_space.onclick(mouse_pressed())
    window.update()
