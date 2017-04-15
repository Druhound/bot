import time
import random
import math
from time import sleep
from unit.unit import bot
from map.map import *

if __name__ == '__main__':
    a = bot()
    map = generate(100, 300, (0, 25))

    map.add_random_attr_nodes(map.nodes())
    map.add_random_weight_edges(map.edges())

    # map.print_nodes_attr(map.nodes())
    map.print_edges_weight(map.edges())
    # print(map.nodes())
    # for edge in map.edges():
    #     print(edge)
    # print(map.weight_edges(0, map.node_neighbors[0]))
    # map.node_neighbors

    # range_list = len()
    # rand = random.choice(range(range_list))
    # print(range_list)
    # print(rand)

    while True:
        clock = time.time()
        print('###### Turn ######')
        neighbors = map.node_neighbors[a.node]
        a.move_bot(neighbors=neighbors, complexity=map.weight_edges(a.node, neighbors))
        sleep(1)