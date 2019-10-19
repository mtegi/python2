from sheep import Sheep
import numpy as np
import math


class Wolf:
    def __init__(self, wolf_move_dist):
        self.move_dist = wolf_move_dist
        self.x = 0
        self.y = 0
        self.eaten = []
        self.eaten_sheep_index = None

    def search(self, sheep_arr):
        if sheep_arr == [None] * len(sheep_arr): #czy cala tablica to None'y ?
            return #zjedzono wszystkie owce

        #znajdz owce ktora jest najblizej
        tmp_arr = [s for s in sheep_arr if s is not None] #kopiowanie tablicy ale nwm czy da sie inaczej
        min_sheep = min(tmp_arr, key=lambda x: x.distance_from_wolf(self.x, self.y))

        #jesli nablizsza owca jest w zasiegu ataku to ja zjedz
        if min_sheep.distance_from_wolf(self.x, self.y) <= self.move_dist:
            self.eaten.append(min_sheep)
            self.eaten_sheep_index = sheep_arr.index(min_sheep) #indeks zjedzonej owcy (do wypisywania)
            sheep_arr[sheep_arr.index(min_sheep)] = None
        else: #zaawanowana matematyka ruchu wilka
            vec_sheep = np.array([min_sheep.x, min_sheep.y]) #wektor owcy
            vec_wolf = np.array([self.x, self.y]) # wektor wilka
            vec_ws = vec_sheep - vec_wolf #wektor wypadkowy
            a = math.sqrt((vec_ws[0]**2)+(vec_ws[1]**2))
            vec_ws_normalized = np.array([vec_ws[0] / a, vec_ws[1] / a]) #znormalizowany wektor wypadkowy
            vec_res = vec_wolf + self.move_dist * vec_ws_normalized #wektor koncowy
            self.x = vec_res[0] #ustaw nowe wspolrzedne
            self.y = vec_res[1]
            self.eaten_sheep_index = None # bo nie zjadl zadnej











