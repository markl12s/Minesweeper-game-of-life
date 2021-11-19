"""
Minesweeper but the mines follow the rules of Conways game of life
a turn moves ahead every time you hit a part of the board
V 1.3.2
last update: 11/11/2021

last change: some minor refactoring, hoping that if I refactor it the bug will just "jump out"
so I can find it

other tasks: need to refactor as soon as first prototype is functional

current task: make it so the numbers can function, can't find the cause of the bug

current known bugs: doesn't replace the numbers with the correct numbers
"""

import turtle
import random

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

buttons_covered = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

number_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

final_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

    return live_cells_nearby

    # check if cell is alive
def cell_dead_or_alive(live_cells_nearby, target_cell_x, target_cell_y):
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
    for x in range(10):
        for y in range(10):
            live_cells_nearby = check_cell(x, y)
            dead_or_alive = cell_dead_or_alive(live_cells_nearby, x, y)
            mine_swap[x][y] = dead_or_alive

    return mine_swap

def turn():
    final_board = []
    mine_swap = turn_check()
    nearby_mines()
    mine_location = mine_swap
    final_board = change_color()

    for x in range(10):
        final_board.append([])
        for y in range(10):
            if buttons_covered[y][x] == 0:
                final_board.append(str(number_array[y][x]))

    return mine_location, final_board


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

    nearby_cells.append(int(mine_location[-1][-1]))
    nearby_cells.append(int(mine_location[-1][0]))
    nearby_cells.append(int(mine_location[-1][1]))

    nearby_cells.append(int(mine_location[0][-1]))
    nearby_cells.append(int(mine_location[0][1]))

    nearby_cells.append(int(mine_location[1][-1]))
    nearby_cells.append(int(mine_location[1][0]))
    nearby_cells.append(int(mine_location[1][1]))

    return sum(nearby_cells)


def bot_left_corner():
    nearby_cells = []

    nearby_cells.append(int(mine_location[-2][-1]))
    nearby_cells.append(int(mine_location[-2][0]))
    nearby_cells.append(int(mine_location[-2][1]))

    nearby_cells.append(int(mine_location[-1][-1]))
    nearby_cells.append(int(mine_location[-1][1]))

    nearby_cells.append(int(mine_location[0][-1]))
    nearby_cells.append(int(mine_location[0][0]))
    nearby_cells.append(int(mine_location[0][1]))

    return sum(nearby_cells)


def top_right_corner():
    nearby_cells = []

    nearby_cells.append(int(mine_location[-1][0]))
    nearby_cells.append(int(mine_location[0][0]))
    nearby_cells.append(int(mine_location[1][0]))

    nearby_cells.append(int(mine_location[1][-1]))
    nearby_cells.append(int(mine_location[-1][-1]))

    nearby_cells.append(int(mine_location[-1][-2]))
    nearby_cells.append(int(mine_location[0][-2]))
    nearby_cells.append(int(mine_location[1][-2]))

    return sum(nearby_cells)


def bot_right_corner():
    nearby_cells = []

    nearby_cells.append(int(mine_location[-1][0]))
    nearby_cells.append(int(mine_location[0][0]))
    nearby_cells.append(int(mine_location[1][0]))

    nearby_cells.append(int(mine_location[-1][-1]))
    nearby_cells.append(int(mine_location[1][-1]))

    nearby_cells.append(int(mine_location[-1][-2]))
    nearby_cells.append(int(mine_location[0][-2]))
    nearby_cells.append(int(mine_location[1][-2]))

    return sum(nearby_cells)


"""Minesweeper"""
# design/architecture
def is_mine(x, y):
    x, y = int(x), int(y)

    if mine_location[y][x] == 1:
        print('is mine')
        return True
    else:
        return False

#game functionality
def generate_board(x = 10, y = 10):  #it's button_array[y][x] instead of [x][y] because of how the arrays are generated
    button_array = []
    hitboxes = []

    for y_cor in range(y):
        button_array.append([])
        hitboxes.append([])

        for x_cor in range(x):
            button_array[y_cor].append(turtle.Turtle())
            button_array[y_cor][x_cor].shape("square")
            button_array[y_cor][x_cor].color("black")
            button_array[y_cor][x_cor].penup()
            button_array[y_cor][x_cor].speed(0)
            button_array[y_cor][x_cor].setpos(x_cor * 25, y_cor * -25)

    return button_array

MOUSE_X, MOUSE_Y = 0, 0
def get_mouse_click_coor(x, y):
    global MOUSE_X, MOUSE_Y

    turtle.onscreenclick(None)
    MOUSE_X, MOUSE_Y = x, y
    return x, y

def check_mouse_click(MOUSE_X, MOUSE_Y, last_mouse_x, last_mouse_y):
    if MOUSE_X == last_mouse_x:
        if MOUSE_Y == last_mouse_y:
            return False

        return True
    return True

def numbers(live_cells_nearby):
    set_number = {
        0: 'white',

        1: 'blue',
        2: 'green',
        3: 'red',
        4: 'purple',
        5: 'brown',
        6: 'light blue',
        7: 'black',
        8: 'grey',
    }

    return set_number.get(live_cells_nearby)

def nearby_mines():
    for x in range(10):
        for y in range(10):
            live_cells_nearby = check_cell(x, y)
            color = numbers(live_cells_nearby)
            final_board[y][x] = color

            if buttons_covered[y][x] == 0:
                button_array[y][x].color(final_board[y][x])

    return button_array


def button_press_action(button_clicked_x, button_clicked_y):
    pressed_mine = is_mine(button_clicked_x, button_clicked_y)
    turn()

    return pressed_mine

def change_color():
    global final_board

    for y in range(10):
        for x in range(10):
            if buttons_covered[y][x] == 0:
                live_cells_nearby = check_cell(x, y)
                number = numbers(live_cells_nearby)

                final_board[y][x] = number
            else:
                final_board[y][x] = 0

    return final_board

#open screen
window = turtle.Screen()
window.bgcolor("white")
window.title("Minesweeper Conways Game of Life")

#generate board
last_mouse_x, last_mouse_y = 0, 0
button_array = generate_board()

while True:
    turtle.onscreenclick(get_mouse_click_coor)

    if check_mouse_click(MOUSE_X, MOUSE_Y, last_mouse_x, last_mouse_y) == True:
        button_clicked_x = round(MOUSE_X / 24)
        button_clicked_y = round(abs(MOUSE_Y / 24))

        if buttons_covered[button_clicked_y][button_clicked_x] == 1:
            buttons_covered[button_clicked_y][button_clicked_x] = 0

            button_array[button_clicked_y][button_clicked_x].color('green')
            button_press_action(button_clicked_x, button_clicked_y)

            mine_location, final_board = turn()

            for x in range(10):
                for y in range(10):
                    if button_array[y][x] == 0:
                        button_array[y][x].color(final_board[y][x])
                    else:
                        pass

    last_mouse_x, last_mouse_y = MOUSE_X, MOUSE_Y
    window.update()
