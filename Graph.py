import networkx as nx
import matplotlib.pyplot as plt

number_of_cells = 2

G = nx.Graph()
for i in range(1, number_of_cells + 1):
    for j in range(1, number_of_cells + 1):
        G.add_node(i * 10 + j)
print('===Graph is created===')
print(f'Number of nodes: {G.number_of_nodes()}')

while True:
    edge = tuple(map(int, input().split()))
    if edge == ():
        if nx.is_connected(G):
            print(f'Graph is connected: {nx.is_connected(G)}')
            break
        else:
            print(f'Graph is connected: {nx.is_connected(G)}')
            print('!!! Add more edges !!!')
            continue
    G.add_edge(edge[0], edge[1])
    print(f'Got the edge: {edge}')
print('==Edges are added===')

nx.draw(G, with_labels=True)
plt.savefig('graph.png')
