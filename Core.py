import networkx as nx


def create_maze(nodes, edges):
    maze = nx.Graph()

    for i in range(nodes):
        for j in range(nodes):
            maze.add_node((i, j))

    for edge in edges:
        maze.add_edge(edge[0], edge[1])

    return maze
