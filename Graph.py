import networkx as nx


class Graph(nx.Graph):
    def __init__(self, _number_of_cells):
        self.cells = _number_of_cells
        self.g = nx.Graph()
        print('===Graph is created===')

        for i in range(1, self.cells + 1):
            for j in range(1, self.cells + 1):
                self.g.add_node(i * 10 + j)
        print(f'Number of nodes: {self.g.number_of_nodes()}')


g = nx.Graph()
number_of_cells = input('Enter number of cells: ')


def main():
    f = open('input.txt', 'r')

    print('Enter number of cells')
    number_of_cells = f.readline()

    g = Graph(int(number_of_cells))

    print('Enter edges')
    while True:
        edge1, edge2 = map(int, f.readline().split())
        if edge1 and edge2:
            if g.is_connected():
                print('Graph is connected.')
                break
            else:
                print('Graph is not connected')
                continue
        g.add_edge((edge1, edge2))

    return g


if __name__ == '__main__':
    main()
