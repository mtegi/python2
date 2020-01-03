from sheep import Sheep
from wolf import Wolf


class Chase:
    def __init__(self, init_pos_limit, sheep_move_dist, wolf_move_dist):
        self.alive_sheep = 0
        self.wolf_move_dist = wolf_move_dist
        self.sheep_move_dist = sheep_move_dist
        self.init_pos_limit = init_pos_limit
        self.num_of_sheep = 0
        self.sheep_arr = []
        self.wolf = Wolf(self.wolf_move_dist)
        self.current_turn = 0

    def reset(self):
        self.current_turn = 0
        self.wolf.reset()
        self.num_of_sheep = 0
        self.sheep_arr = []
        self.alive_sheep = 0

    def add_sheep(self, x, y):
        sheep = Sheep(self.init_pos_limit, self.sheep_move_dist, x, y)
        self.sheep_arr.append(sheep)
        self.alive_sheep += 1

    def step(self):
        self.alive_sheep = 0
        self.current_turn += 1
        for s in self.sheep_arr:
            if s not in self.wolf.eaten and s is not None:  # jesli nie zjedzona
                s.move()  # rusz owce
                self.alive_sheep += 1  # inkrementuj licznik zywych owiec
        if self.wolf.search(self.sheep_arr):
            self.alive_sheep -= 1
