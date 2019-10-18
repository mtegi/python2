from sheep import Sheep
from wolf import Wolf

turns = 50
num_of_sheep = 15
init_pos_limit = 10.0
sheep_move_dist = 0.5
wolf_move_dist = 1.0

sheep_arr = [Sheep(init_pos_limit, sheep_move_dist) for i in range(0, num_of_sheep)]
wolf = Wolf(wolf_move_dist)
for t in range(0, turns):
    alive_sheep = 0
    for s in sheep_arr:
        if s not in wolf.eaten and s is not None:
            s.move()
            alive_sheep += 1

    wolf.search(sheep_arr)
    print("Turn: " + str(t + 1))
    print(" wolf pos: " + str(wolf.x) + " , " + str(wolf.y))
    print(" alive sheep = " + str(alive_sheep))




