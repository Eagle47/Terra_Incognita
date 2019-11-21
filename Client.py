from Core import create_maze, make_a_move

f = open('input.txt', 'r')
print('Enter number of nodes: ')
number_of_nodes = int(f.readline())

list_of_edges = []
line = f.readline()
print('Enter edges: ')
while line != 'start\n':
    tmp = list(int(x) - 1 for x in line.split())
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

print('\nEnter start position: ')
curr_pos = tuple(int(x) for x in f.readline().split())
print(curr_pos)
player_maze.add_node(curr_pos)

while True:
    new_pos = tuple(int(x) for x in input().split())
    curr_pos = make_a_move(maze, player_maze, new_pos, curr_pos)
    print('New pos: ', curr_pos)
    print('Num of edges: ', player_maze.number_of_edges())
    print('Num of nodes: ', player_maze.number_of_nodes())

f.close()