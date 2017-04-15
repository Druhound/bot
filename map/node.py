class Node():
    def __init__(self, id_node):
        self.id_node = id_node
        self.edges = []

    def __str__(self):
        return 'id_node:{0} - {1}'.format(self.id_node, self.edges)

    def append_edge(self, edge):
        temp = self.edges
        temp.append(edge)
        self.edges = temp

