import networkx as nx
import matplotlib.pyplot as plt

input = open('input.txt', 'r')
Graph = nx.Graph()
for line in input:
    line = line.strip()
    if not line:
        continue
    print(line)
    vertex1, vertex2, weight = line.split()
    Graph.add_edge(vertex1, vertex2, weight=float(weight))
pos = nx.spring_layout(Graph)
nx.draw_networkx_nodes(Graph, pos, node_size=700)
elarge = [(u,v) for (u,v,d) in Graph.edges(data=True) if d['weight']>100]
esmall = [(u,v) for (u,v,d) in Graph.edges(data=True) if d['weight'] <=100]
nx.draw_networkx_edges(Graph, pos, edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(Graph, pos, edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

nx.draw_networkx_labels(Graph, pos,font_size=20,font_family='sans-serif')
plt.axis('off')
plt.savefig("Graph")
plt.show()