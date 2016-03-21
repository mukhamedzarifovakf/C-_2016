import networkx as nx
import matplotlib.pyplot as plt


def dfs_tree(g, start, counted, tree_graph):
    counted.add(start)
    for neighbour in g[start]:
        if neighbour not in counted:
            dfs_tree(g, neighbour, counted, tree_graph)
            tree_graph.add_edge(start, neighbour, weight=0)
    return tree_graph


def get_graph(file):

    Graph = nx.Graph()
    for line in file:
        line = line.strip()
        vertex1, vertex2, weight = line.split()
        Graph.add_edge(vertex1, vertex2, weight=float(weight))
    return Graph


file = open('input.txt', 'r')
map = get_graph(file)
tree = nx.Graph()
counted = set()
tree = dfs_tree(map, 'Fejhoa', counted, tree)
pos_tree = nx.spring_layout(tree)
nx.draw_networkx_labels(tree, pos_tree,font_size=15,font_family='sans-serif')
nx.draw_networkx_nodes(tree, pos_tree, node_size=500)
nx.draw_networkx_edges(tree, pos_tree,width=6)
plt.savefig("Graph")
plt.show()