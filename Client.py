import networkx as nx


def create_maze(nodes, edges):
    maze = nx.Graph()

    if nodes > 1:
        for i in range(1, nodes + 1):
            for j in range(1, nodes + 1):
                maze.add_node((i, j))

    for edge in edges:
        maze.add_edge(edge[0], edge[1])

    return maze


def make_a_move(true_maze, player_maze, next_pos, curr_pos):
    if true_maze.has_node(next_pos):
        player_maze.add_node(next_pos)

    if not true_maze.has_edge(curr_pos, next_pos):
        return curr_pos

    player_maze.add_node(next_pos)
    player_maze.add_edge(curr_pos, next_pos)
    new_pos = next_pos

    return new_pos


f = open('input8.txt', 'r')
number_of_nodes = int(f.readline())

list_of_edges = []
line = f.readline()
while line != 'start\n':
    tmp = list(int(x) for x in line.split())
    list_of_edges.append([tuple(tmp[0:2]), tuple(tmp[2:])])
    line = f.readline()

maze = create_maze(number_of_nodes, list_of_edges)
print('True maze created')
print('Num of nodes: ', maze.number_of_nodes())
print('Num of edges: ', maze.number_of_edges())

l_player = []
player_maze = create_maze(1, l_player)
print('\nMaze for player created')
print('Num of nodes: ', player_maze.number_of_nodes())
print('Num of edges: ', player_maze.number_of_edges())

print('\nStart position: ')
start = tuple(int(x) for x in f.readline().split())
player_maze.add_node(start)
print(start)

print('\nExit edge: ')
end = list(int(x) for x in f.readline().split())
maze.add_edge(tuple(end[0:2]), tuple(end[2:]))
print(tuple(end[0:2]), tuple(end[2:]))
print('Num of nodes: ', maze.number_of_nodes())
print('Num of edges: ', maze.number_of_edges())

print('\nTreasure position:')
treasure = tuple(int(x) for x in f.readline().split())
print(treasure)

f.close()
