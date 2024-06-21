import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def hill_climbing_algorithm(cidade):
    pass


if (__name__ == "__main__"):
    grafo = nx.Graph()
    nodes = [0, 1, 2, 3, 4, 5]
    edges = [
        (0, 1, 12),
        (0, 2, 15),
        (0, 3, 26),
        (0, 4, 11),
        (1, 2, 11),
        (1, 4, 23),
        (2, 4, 9),
        (3, 2, 4),
        (5, 3, 90)
    ]
    
    grafo.add_nodes_from(nodes)
    grafo.add_weighted_edges_from(edges)
    
    pos = nx.spring_layout(grafo)
    nx.draw_networkx_nodes(grafo, pos, node_size=650, node_color="purple")
    nx.draw_networkx_labels(grafo, pos, font_size=14, font_color="white", font_family="Impact")
    nx.draw_networkx_edges(grafo, pos, width=2)
    edge_labels = nx.get_edge_attributes(grafo, "weight")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    
    plt.axis("off")
    plt.show()