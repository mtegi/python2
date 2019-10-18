import random
import math


def calc_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


class Sheep:
    def __init__(self, init_pos_limit, sheep_move_dist):
        self.move_dist = sheep_move_dist
        self.x = random.uniform(-init_pos_limit, init_pos_limit)
        self.y = random.uniform(-init_pos_limit, init_pos_limit)

    def move(self): #ruch o kierunek
        direction = random.randint(1, 4)
        if direction == 1: #polnoc
            self.y += self.move_dist
        elif direction == 2: #poludnie
            self.y -= self.move_dist
        elif direction == 3: #wschod
            self.x -= self.move_dist
        elif direction == 4: #zachod
            self.x += self.move_dist

    def distance_from_wolf(self, wolf_x, wolf_y):
        return calc_distance(wolf_x, wolf_y, self.x, self.y)
