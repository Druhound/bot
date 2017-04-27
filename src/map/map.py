# from pygraph.algorithms.generators import generate
from pygraph.classes.digraph import digraph
import random
from random import randint, shuffle


def generate(num_nodes, num_edges, weight_range=(1, 1)):
    random_graph = Directed_graph()

    nodes = range(num_nodes)
    random_graph.add_nodes(nodes)

    edges = []
    edges_append = edges.append
    for x in nodes:
        for y in nodes:
            if ((x != y) or (x > y)):
                edges_append((x, y))

    shuffle(edges)

    min_wt = min(weight_range)
    max_wt = max(weight_range)
    for i in range(num_edges):
        each = edges[i]
        random_graph.add_edge((each[0], each[1]), wt=randint(min_wt, max_wt))

    return random_graph


class Directed_graph(digraph):
    def add_random_weight_edges(self, edges):
        for edge in edges:
            self.set_edge_weight(edge, random.randint(0, 25))

    def print_edges_weight(self, edges):
        for edge in edges:
            print("edge: {0}: {1}".format(edge, self.edge_weight(edge)))

    def add_random_attr_nodes(self, nodes):
        for node in nodes:
            self.add_node_attribute(node, random.randint(0, 25) * -1)

    def print_nodes_attr(self, nodes):
        for node in nodes:
            print("node: {0} - {1}".format(node, self.node_attributes(node)))

    def weight_edges(self, node, edges):
        array = []
        # print(node, edges)
        for edge in edges:
            list = (node, edge)
            array.append(self.edge_weight(list))
            # array.append(dict(zip(node, edge)))
            # print(array)
        # print(array)
        return array