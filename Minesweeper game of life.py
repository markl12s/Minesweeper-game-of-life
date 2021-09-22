"""
Minesweeper but the mines follow the rules of Conways game of life
a turn moves ahead every time you hit a part of the board

V 1.0.2
last update: 9/20/2021
last change: fixed the not working on click, some small refactoring

current task: design how the full board will function
"""

from random import *
from turtle import Turtle, Screen

global MINE_LOCATION
MINE_LOCATION = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                 [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

global MINE_SWAP
MINE_SWAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        live_cells_nearby = sum_cell_collection( # top left corner
            [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)])
    elif target_cell_x == -1 and target_cell_y == 0:
        live_cells_nearby = sum_cell_collection( # bottom left corner
            [(-2,-1), (-2,0), (-2,1), (-1,-1), (-1,1), (0,-1), (0,0), (0,1)])
    elif target_cell_x == 0 and target_cell_y == -1:
        live_cells_nearby = sum_cell_collection( # top right corner
            [(-1,0), (0,0), (1,0), (1,-1), (-1,-1), (-1,-2), (0,-2), (1,-2)])
    elif target_cell_x == -1 and target_cell_y == -1:
        live_cells_nearby = sum_cell_collection( # bottom right corner
            [(-1,0), (0,0), (1,0), (-1,-1), (1,-1), (-1,-2), (0,-2), (1,-2)])

    # middle cells
    elif target_cell_x != 0 and target_cell_x != -1:
        if target_cell_y != 0 and target_cell_y != -1:
            live_cells_nearby = add_row(target_cell_x - 1, target_cell_y)
            live_cells_nearby += add_sides(target_cell_x, target_cell_y)
            live_cells_nearby += add_row(target_cell_x + 1, target_cell_y)

    # check if cell is alive
    if MINE_LOCATION[target_cell_x][target_cell_y] == 0:
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
    return sum(
        [MINE_LOCATION[middle_x % 10][(middle_y + i) % 10] for i in [-1, 0, 1]])


def add_sides(middle_x, middle_y):
    return sum(
        MINE_LOCATION[middle_x][middle_y - 1],
        MINE_LOCATION[middle_x][(middle_y + 1) % 10]
    )

def sum_cell_collection(locations):
    return sum([MINE_LOCATION[x][y] for x, y in locations])


def turn():
    turn_check()
    MINE_LOCATION = MINE_SWAP

"""Minesweeper"""
def is_mine(x, y):
    if MINE_LOCATION[x][y] == 1:
        return True
    else:
        return False

#design/architecture

#press uncovered space
#on mousepress
def click_on_space(x, y):
    global space_0_covered, space_0_mine

    if space_0_covered == True:
        if space_0_mine == False:
            space_0_covered = False
            turn()
            #calculate number of nearby mines to spaces
            #show numbers
            print(MINE_LOCATION)
        elif space_0_mine == True:
            print('Game Over')
    else:
        pass

#execution

if __name__ == "__main__":
    window = Screen()
    window.bgcolor("white")
    window.title("Minesweeper Conways Game of Life")

    space_0 = Turtle()
    space_0.shape("square")
    space_0.color("black")
    space_0.setpos(0, 0)
    space_0_covered = True
    space_0_mine = is_mine(0, 0)
    print(MINE_LOCATION)

    while True:
        space_0_mine = is_mine(0, 0)
        space_0.onclick(click_on_space)
        window.update()
