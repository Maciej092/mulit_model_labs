import numpy as np
import matplotlib.pyplot as plt
import random
import time
from typing import *
import matplotlib.animation as animation

grain_id = [0, 0.5, 1]
neighbour_rule = 'Moore'
space_x = 10
space_y = 10
color_white = [255, 255, 255]
color_black = [0, 0, 0]
a = [[[random.random(), random.random(), random.random()] for y in range(space_y)] for x in range(space_x)]
Z = np.array(a)

fig, ax = plt.subplots(1, 1)
ax.imshow(Z)
ax.set_title('default: no edges')
fig.tight_layout()
plt.show()
current_x = 0
current_y = 0


def add(x):
    Z[x] = [random.randint(0, 255) for x in range(space_x)]
    ax.imshow(Z)
counter = []


def one_step():
    counter.append(1)
    Z[current_x+len(counter)][current_y+len(counter)] = 1
    ax.imshow(Z)


def get_grain_id(x: int, y: int) -> float:
    matrix_higth = space_x
    metrix_width = space_y
    if Z[x][y]:     # Need to check if cell is out of the range. If yes, choose the neigh based on border rules
        pass
    val = Z[x][y]
    return val


def check_neighbourhood(pos):
    pos_x  = pos[0]
    pos_y  = pos[1]
    out_id = 0
    neighbours = list()
    neighbours_id_one = list()
    neighbours_id_two  = list()
    if neighbour_rule == 'Moore':
        neighbours[0] = get_grain_id(pos_x-1, pos_y-1)
        neighbours[1] = get_grain_id(pos_x-1, pos_y)
        neighbours[2] = get_grain_id(pos_x-1, pos_y+1)
        neighbours[3] = get_grain_id(pos_x, pos_y-1)
        neighbours[4] = get_grain_id(pos_x, pos_y+1)
        neighbours[5] = get_grain_id(pos_x+1, pos_y-1)
        neighbours[6] = get_grain_id(pos_x+1, pos_y)
        neighbours[7] = get_grain_id(pos_x+1, pos_y+1)
        if sum(neighbours) > 0:
            for neigh in neighbours:
                if neigh == grain_id[1]:
                    neighbours_id_one.append(neigh)
                if neigh == grain_id[2]:
                    neighbours_id_two.append(neigh)
        else:
            'There was no active grain within the nieghbourhood'
            out_id = grain_id[0]
            return out_id

    if neighbour_rule == 'vonNeumann':
        neighbours[1] = get_grain_id(pos_x-1, pos_y)
        neighbours[3] = get_grain_id(pos_x, pos_y-1)
        neighbours[4] = get_grain_id(pos_x, pos_y+1)
        neighbours[6] = get_grain_id(pos_x+1, pos_y)
        if sum(neighbours) > 0:
            for neigh in neighbours:
                if neigh == grain_id[1]:
                    neighbours_id_one.append(neigh)
                if neigh == grain_id[2]:
                    neighbours_id_two.append(neigh)
        else:
            'There was no active grain within the nieghbourhood'
            out_id = grain_id[0]
            return out_id

    if len(neighbours_id_one) > len(neighbours_id_two):
        out_id = grain_id[1]
    if len(neighbours_id_two) > len(neighbours_id_one):
        out_id = grain_id[2]
    if len(neighbours_id_two) == len(neighbours_id_one):
        out_id = grain_id[random.choice([1, 2])]
    return out_id


# def start():
#     current_val = 0
#     current_x   = 0
#     current_y   = 0
#     # First step
#     current_pos = [current_x, current_y]
#     current_val = get_grain_id(current_x, current_y)
#     # Check the neighbours
#     if current_val == 1:
#         pass
#     else:
#         check_neighbourhood(current_pos)
#
#     current_x = 0
#     current_y = 1
#
#     ax.imshow(Z)


def animate(i):
    x = random.randint(0,9)
    y = random.randint(0,9)
    while x < space_y:
        Z[x][y] = 1
        ax.imshow(Z)


def start():
    ani = animation.FuncAnimation(fig, animate, interval=1000)

# for num in range(1000):
#     add(num)
#     time.sleep(0.01)