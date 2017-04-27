import time
from time import sleep
from src import settings
import data.main

from src.map.map import *
from src.unit.unit import bot
from PSQL import main

if __name__ == '__main__':
    # a = bot()
    # map = generate(100, 300, (0, 25))

    # map.add_random_attr_nodes(map.nodes())
    # map.add_random_weight_edges(map.edges())

    # map.print_nodes_attr(map.nodes())
    # map.print_edges_weight(map.edges())
    # print(map.nodes())
    # for edge in map.edges():
    #     print(edge)
    # print(map.weight_edges(0, map.node_neighbors[0]))
    # print(map.node_neighbors)

    # range_list = len()
    # rand = random.choice(range(range_list))
    # print(range_list)
    # print(rand)
    # print(map.weight_edges(0, map.node_neighbors[0]))
    """
        DATA
    """
    data = data.main.parsing('map.csv')
    values = data[0]
    header = data[1]
    """
        !DATA
    """

    """
        INIT
    """
    database = main.connect_database(settings.DATABASE, settings.USER, settings.HOST, settings.PASSWORD)
    cursor = main.cursor(database)

    seq = main.create_seq(cursor, 'nodes', 'node')
    main.insert_table_CSV(cursor, 'node', header, seq)
    main.commit_changes(database)
    main.cursor_close(cursor)

    """
        !INIT
    """
    # while True:
    #     clock = time.time()
    #     print('###### Turn ######')
    #     neighbors = map.node_neighbors[a.node]
    #     a.move_bot(neighbors=neighbors, complexity=map.weight_edges(a.node, neighbors))
    #     sleep(1)
