import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, _number_of_cells):
        self.cells = _number_of_cells
        self.g = nx.Graph()
        print('===Graph is created===')

        for i in range(1, self.cells + 1):
            for j in range(1, self.cells + 1):
                self.g.add_node(i * 10 + j)
        print(f'Number of nodes: {self.g.number_of_nodes()}')

    def is_connected(self):
        return nx.is_connected(self.g)

    def add_edge(self, _edge):
        self.g.add_edge(_edge[0], _edge[1])


f = open('input.txt', 'r')

print('Enter number of cells')
number_of_cells = f.readline()

G = Graph(int(number_of_cells))

print('Enter edges')
while True:
    edge = tuple(map(int, f.readline().split()))
    if edge == ():
        if G.is_connected():
            print('Graph is connected.')
            break
        else:
            print('Graph is not connected')
            continue
    G.add_edge(edge)


nx.draw(G.g, with_labels=True)
plt.savefig('graph.png')
