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
        print('WALL')
        return curr_pos

    player_maze.add_node(next_pos)
    player_maze.add_edge(curr_pos, next_pos)
    new_pos = next_pos

    return new_pos


def is_over(curr_pos, end):
    if curr_pos == end:
        print('You won!')
        return True
    return False
