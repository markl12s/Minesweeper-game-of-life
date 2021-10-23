"""
Minesweeper but the mines follow the rules of Conways game of life
a turn moves ahead every time you hit a part of the board
V 1.2.0
last update: 10/17/2021

last change: can succesfully function for spot 0, 0

other tasks:

current task: redesign minesweeper

current known bugs:
"""

import turtle, random

mine_location = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
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

buttons_covered = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

# functions/architecture
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

def turn():
    turn_check()
    mine_location = mine_swap

    return mine_location


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


# corners
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


"""Minesweeper"""
mouse_location = turtle.Turtle()
mouse_location.penup()
mouse_location.hideturtle()
mouse_location.speed(0)

window = turtle.Screen()
window.bgcolor("white")
window.title("Minesweeper Conways Game of Life")


# design/architecture
def is_mine(x, y):
    x, y = int(x), int(y)

    if mine_location[y][x] == 1:
        return True
    else:
        return False

def generate_board(x = 10, y = 10):  #it's button_array[y][x] instead of [x][y] because of how arrays are generated
    button_array = []

    for y_cor in range(y):
        button_array.append([])

        for x_cor in range(x):
            button_array[y_cor].append(turtle.Turtle())
            button_array[y_cor][x_cor].shape("square")
            button_array[y_cor][x_cor].color("black")
            button_array[y_cor][x_cor].penup()
            button_array[y_cor][x_cor].speed(0)
            button_array[y_cor][x_cor].setpos(x_cor * 25, y_cor * -25)
            #move the buttons around

            #button_covered[y_cor][x_cor] = True
            #button_mine[y_cor][x_cor] = is_mine(x, y)

    return button_array

#generate board
generate_board()

while True:
    window.update()
