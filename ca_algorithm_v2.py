import numpy as np
import random
import time
import copy
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


class CellularAutomata:
    def __init__(self, number, space_width, space_length,  border_rule='snakelike', string='MOORE'):
        self.MOORE = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        self.VONNEUMANN = ((-1, 0), (0, -1), (0, 1), (1, 0))
        self.border_rule = border_rule
        self.number = number
        self.space_width = space_width
        self.space_length = space_length
        self.space = np.zeros((self.space_width, self.space_width), dtype=np.uint8)
        # self.space_prev = np.zeros((self.space_width, self.space_width), dtype=np.uint8)
        self.cell_empty = 0
        self.neighbours = self.choose_neighbours(string)
        self.color_id = {}
        self.coordinates = []
        self.image = plt.figure()

    def evaluate_id(self, nei_list):
        counter = 0
        num = nei_list[0]
        for i in nei_list:
            if i > 0:
                curr_frequency = nei_list.count(i)
                if curr_frequency > counter:
                    counter = curr_frequency
                    num = i
        return num

    def choose_neighbours(self, string):
        if string == 'MOORE':
            neighbours = self.MOORE
        else:
            neighbours = self.VONNEUMANN
        return neighbours

    def add_random(self):
        self.color_id.setdefault(0, np.array([255, 255, 255], dtype=np.uint8))
        for i in range(self.number):
            self.color_id.setdefault(i+1, np.random.randint(0, 255, 3, dtype=np.uint8))
            random_x = random.randint(0, self.space_width-1)
            random_y = random.randint(0, self.space_width-1)
            self.space[random_x, random_y] = i+1
            self.coordinates.append((random_x, random_y))
        return self.color_id

    def one_step(self):
        space_prev = copy.deepcopy(self.space)
        t1 = time.time()
        for x in range(self.space_width):
            for y in range(self.space_width):
                if space_prev[x, y] == self.cell_empty:
                    nei_list = []
                    for neigh in self.neighbours:
                        xn, yn = neigh
                        if self.border_rule == 'absorbing':
                            if (x + xn) < 0 or (y + yn) < 0 or (x + xn) >= self.space_width or (y + yn) >= self.space_width:
                                nei_list.append(0)
                            else:
                                nei_list.append(space_prev[x+xn, y+yn])
                        else:
                            nei_list.append(space_prev[(x + xn) % self.space_width, (y + yn) % self.space_width])
                    if sum(nei_list) > 0:
                        self.space[x, y] = self.evaluate_id(nei_list)
                    else:
                        self.space[x, y] = 0
        print(f"{time.time() - t1}")
        return

def get_cmap(n, name='RdGy'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


cmap = LinearSegmentedColormap.from_list('mycmap', ['white', 'blue', 'cyan', 'green', 'yellow','red'])
ca = CellularAutomata(100, 200, 200)
ca.add_random()
ca.one_step()
plt.imshow(ca.space, cmap=cmap)