"""
Minesweeper but the mines follow the rules of Conways game of life
a turn moves ahead every time you hit a part of the board
V 1.3.1
last update: 11/1/2021

last change: buttons are fully working, just need to get everything else working

other tasks: need to refactor as soon as first prototype is functional

current task: make it so the numbers can function

current known bugs:
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
    live_or_dead = []
    for x in range(10):
        for y in range(10):
            live_cells_nearby = check_cell(x, y)
            dead_or_alive = cell_dead_or_alive(live_cells_nearby, x, y)
            mine_swap[x][y] = dead_or_alive

def turn():
    turn_check()
    nearby_mines()
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
# design/architecture
def is_mine(x, y):
    x, y = int(x), int(y)

    if mine_location[y][x] == 1:
        print('is mine')
        return True
    else:
        return False

#board class
class board:
    import turtle

    #objects
    Button = turtle.Turtle

    #clicked = Button.onclick(self, button_press_action)


#game functionality
def generate_board(x = 10, y = 10):  #it's button_array[y][x] instead of [x][y] because of how the arrays are generated
    button_array = []
    hitboxes = []

    for y_cor in range(y):
        button_array.append([])
        hitboxes.append([])

        for x_cor in range(x):
            button_array[y_cor].append(board.Button())
            button_array[y_cor][x_cor].shape("square")
            button_array[y_cor][x_cor].color("black")
            button_array[y_cor][x_cor].penup()
            button_array[y_cor][x_cor].speed(0)
            button_array[y_cor][x_cor].setpos(x_cor * 25, y_cor * -25)

            #I don't think hitboxes are needed, but im keeping them here just incase, will delete later if unused
            hitbox_size = 12
            hitboxes[y_cor].append([button_array[y_cor][x_cor].xcor() + hitbox_size, button_array[y_cor][x_cor].xcor() - hitbox_size,
                                    button_array[y_cor][x_cor].ycor() + hitbox_size, button_array[y_cor][x_cor].ycor() - hitbox_size])

    return hitboxes, button_array

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
    if live_cells_nearby == 0:
        return 'white'

    elif live_cells_nearby == 1:
        return 'blue'
    elif live_cells_nearby == 2:
        return 'green'
    elif live_cells_nearby == 3:
        return 'red'
    elif live_cells_nearby == 4:
        return 'purple'
    elif live_cells_nearby == 5:
        return 'brown'
    elif live_cells_nearby == 6:
        return 'light blue'
    elif live_cells_nearby == 7:
        return 'black'
    elif live_cells_nearby == 8:
        return 'grey'

def nearby_mines():
    nearby_mines_array = []
    for x in range(10):
        for y in range(10):
            live_cells_nearby = check_cell(x, y)
            color = numbers(live_cells_nearby)
            mine_swap[y][x] = color

            if buttons_covered[y][x] == 0:
                button_array[y][x].color(mine_swap[y][x])


def button_press_action(button_clicked_x, button_clicked_y):
    pressed_mine = is_mine(button_clicked_x, button_clicked_y)
    turn()

#open screen
window = turtle.Screen()
window.bgcolor("white")
window.title("Minesweeper Conways Game of Life")

#generate board
last_mouse_x, last_mouse_y = 0, 0
hitboxes, button_array = generate_board()

while True:
    turtle.onscreenclick(get_mouse_click_coor)

    if check_mouse_click(MOUSE_X, MOUSE_Y, last_mouse_x, last_mouse_y) == True:
        button_clicked_x = round(MOUSE_X / 24)
        button_clicked_y = round(abs(MOUSE_Y / 24))

        if buttons_covered[button_clicked_y][button_clicked_x] == 1:
            buttons_covered[button_clicked_y][button_clicked_x] = 0

            button_press_action(button_clicked_x, button_clicked_y)

            button_array[button_clicked_y][button_clicked_x].color('green')

    last_mouse_x, last_mouse_y = MOUSE_X, MOUSE_Y
    window.update()
