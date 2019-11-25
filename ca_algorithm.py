import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
# fig = plt.figure()
# data = np.array([[np.zeros(3) for item in range(y)] for itemm in range(x)])
# im = plt.imshow(data, animated=True)
neighbour_rule = 'vonNeumann'
space_width = 50
space_lengtth = 50
cell_empty = np.array([255, 255, 255], dtype=int)
cell_random = np.random.random(3)
array = [[cell_empty for y in range(space_width)] for x in range(space_lengtth)]
space = np.array(array)

fig = plt.figure()
l, = plt.imshow(space)


def add_random(number):
    for i in range(number):
        x = random.randint(0,space_lengtth-1)
        y = random.randint(0,space_width-1)
        space[x, y] = np.random.randint(0,255,3)
    plt.imshow(space)

def add():
    space[0, 1] = np.array([0,0,0])
    plt.imshow(space)

def one_step(space):
    space_new = np.array(array)
    for x in range(space_width):
        for y in range(space_lengtth):
            cell_current = space[x, y]
            if (cell_current<cell_empty).any():
                space_new[x, y] = cell_current
                continue
            else:
                neighbour = check_nieghbours(x, y)
                neighbour_dict = {}
                for neigh in neighbour:
                    cell_neigh = space[neigh[0], neigh[1]]
                    if (cell_neigh<cell_empty).any():
                        temp_val = neighbour_dict.setdefault(tuple(cell_neigh),0)
                        temp_val += 1
                        neighbour_dict[tuple(cell_neigh)] = temp_val
                    else:
                        continue
                if len(neighbour_dict):
                    max_key = [key for m in [max(neighbour_dict.values())] for key, val in neighbour_dict.items() if val == m]
                    if len(max_key) > 1:
                        out_val = np.asarray(random.choice(max_key))
                    else:
                        out_val = np.asarray(max_key[0])
                else:
                    out_val = cell_empty
            space_new[x, y] = out_val
    plt.imshow(space_new)
    return space_new


def check_nieghbours(x, y):
    if neighbour_rule == 'Moore':
        neighbour    = []
        neighbour.append(((x - 1)%space_width, (y - 1)%space_lengtth))
        neighbour.append(((x - 1)%space_width, (y    )%space_lengtth))
        neighbour.append(((x - 1)%space_width, (y + 1)%space_lengtth))
        neighbour.append(((x    )%space_width, (y - 1)%space_lengtth))
        neighbour.append(((x    )%space_width, (y + 1)%space_lengtth))
        neighbour.append(((x + 1)%space_width, (y - 1)%space_lengtth))
        neighbour.append(((x + 1)%space_width, (y    )%space_lengtth))
        neighbour.append(((x + 1)%space_width, (y + 1)%space_lengtth))
    elif neighbour_rule == 'vonNeumann':
        neighbour    = []
        neighbour.append(((x - 1)%space_width, (y    )%space_lengtth))
        neighbour.append(((x + 1)%space_width, (y    )%space_lengtth))
        neighbour.append(((x    )%space_width, (y + 1)%space_lengtth))
        neighbour.append(((x    )%space_width, (y - 1)%space_lengtth))
    return neighbour


# add_random(80)
# while cell_empty in space:
#     space = one_step(space)

def f(x, y):
    data = np.array([[[random.random(), random.random(), random.random()]
                      for item in range(y)] for itemm in range(x)])
    return data


def updatefig(*args):
    space = one_step(space)
    return


def run():
    anim = animation.FuncAnimation(fig, one_step, interval=5, blit=True)


