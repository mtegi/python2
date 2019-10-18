from sheep import Sheep
import numpy as np
import math


class Wolf:
    def __init__(self, wolf_move_dist):
        self.move_dist = wolf_move_dist
        self.x = 0
        self.y = 0
        self.eaten = []

    def search(self, sheep_arr):
        if len(sheep_arr) == 0:
            return #zjedzono wszystkie owce

        #znajdz owce ktora jest najblizej
        min_sheep = min(sheep_arr, key=lambda x: x.distance_from_wolf(self.x, self.y))

        #jesli nablizsza owca jest w zasiegu ataku to ja zjedz
        if min_sheep.distance_from_wolf(self.x, self.y) <= self.move_dist:
            self.eaten.append(min_sheep)
            del sheep_arr[sheep_arr.index(min_sheep)] # usun ja z zywych
        else: #zaawanowana matematyka ruchu wilka
            vec_sheep = np.array([min_sheep.x, min_sheep.y])
            vec_wolf = np.array([self.x, self.y])
            vec_ws = vec_sheep - vec_wolf
            a = math.sqrt((vec_ws[0]**2)+(vec_ws[1]**2))
            vec_ws_normalized = np.array([vec_ws[0] / a, vec_ws[1] / a])
            vec_res = vec_wolf + self.move_dist * vec_ws_normalized
            self.x = vec_res[0]
            self.y = vec_res[1]











