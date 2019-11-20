from Core import create_maze

f = open('input.txt', 'r')
number_of_nodes = int(f.readline())

list_of_edges = []
line = f.readline()
while line != '':
    tmp = list(int(x) - 1 for x in line.split())
    list_of_edges.append([tuple(tmp[0:2]), tuple(tmp[2:])])
    line = f.readline()

maze = create_maze(number_of_nodes, list_of_edges)
print('Num of nodes: ', maze.number_of_nodes())
print('Num of edges: ', maze.number_of_edges())
