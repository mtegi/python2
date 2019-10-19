from sheep import Sheep
from wolf import Wolf
import json
import csv


class Chase:
    def __init__(self, turns, num_of_sheep, init_pos_limit, sheep_move_dist, wolf_move_dist):
        self.alive_sheep = 0
        self.wolf_move_dist = wolf_move_dist
        self.sheep_move_dist = sheep_move_dist
        self.init_pos_limit = init_pos_limit
        self.num_of_sheep = num_of_sheep
        self.turns = turns
        self.sheep_arr = [Sheep(self.init_pos_limit, self.sheep_move_dist) for i in range(0, self.num_of_sheep)]
        self.wolf = Wolf(self.wolf_move_dist)
        self.alive_sheep = None
        self.current_turn = None

    def start(self):
        with open('alive.csv', 'w', newline='') as alive_file, open('pos.json', 'w') as json_file:
            json_data = []
            for t in range(0, self.turns):
                self.alive_sheep = 0
                self.current_turn = t + 1
                for s in self.sheep_arr:
                    if s not in self.wolf.eaten and s is not None: #jesli nie zjedzona
                        s.move() #rusz owce
                        self.alive_sheep += 1 #inkrementuj licznik zywych owiec
                self.wolf.search(self.sheep_arr) #ruch wilka
                self.print()# na konsole
                self.alive_to_csv(alive_file)# do csv
                self.json_append(json_data)# do jsona
            json.dump(json_data, json_file, indent=4)

    def print(self):
        print("Turn: " + str(self.current_turn))
        print(" wolf pos: " + str(self.wolf.x) + " , " + str(self.wolf.y))
        print(" alive sheep = " + str(self.alive_sheep))
        if self.wolf.eaten_sheep_index is not None:
            print("Sheep no." + str(self.wolf.eaten_sheep_index + 1) + " was eaten.")

    def alive_to_csv(self, alive_file):
        writer = csv.writer(alive_file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([self.current_turn, self.alive_sheep])

    def json_append(self, json_data):
        json_data.append({
            'round_no': self.current_turn,
            'wolf_pos': [self.wolf.x, self.wolf.y],
            'sheep_pos': [[s.x, s.y] if s is not None else None for s in self.sheep_arr]
        })


chase = Chase(50, 15, 10.0, 0.5, 1.0)
chase.start()

