from Core import create_maze, make_a_move, is_over

f = open('input.txt', 'r')
print('Enter number of nodes: ')
number_of_nodes = int(f.readline())

list_of_edges = []
line = f.readline()
print('Enter edges: ')
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

print('\nEnter start position: ')
curr_pos = tuple(int(x) for x in f.readline().split())
player_maze.add_node(curr_pos)
print(curr_pos)

print('\nEnter exit edge: ')
end = list(int(x) for x in f.readline().split())
maze.add_edge(tuple(end[0:2]), tuple(end[2:]))
print(tuple(end[0:2]), tuple(end[2:]))
print('Num of nodes: ', maze.number_of_nodes())
print('Num of edges: ', maze.number_of_edges())

print('Your position: ', curr_pos)
while not is_over(curr_pos, tuple(end[2:])):
    print('\nEnter new position: ')
    new_pos = tuple(int(x) for x in input().split())
    curr_pos = make_a_move(maze, player_maze, new_pos, curr_pos)
    print('New pos: ', curr_pos)
    print('Num of nodes: ', player_maze.number_of_nodes())
    print('Num of edges: ', player_maze.number_of_edges())

f.close()
