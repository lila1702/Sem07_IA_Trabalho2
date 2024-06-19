import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

nodes = [0, 1, 2, 3]
graph.add_nodes_from(nodes)

edges = [
    (0, 1, 10),
    (0, 2, 15),
    (0, 3, 20),
    (1, 2, 35),
    (1, 3, 25),
    (2, 3, 30)
]

graph.add_weighted_edges_from(edges)

# Visualize the graph
pos = nx.spring_layout(graph)  # positions for all nodes

# Draw nodes
nx.draw_networkx_nodes(graph, pos, node_size=700)

# Draw edges
nx.draw_networkx_edges(graph, pos, width=6)

# Draw labels
nx.draw_networkx_labels(graph, pos, font_size=20, font_family='sans-serif')

# Draw edge labels (if there are weights)
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

# Show the plot
plt.axis('off')  # turn off the axis
plt.show()