import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import os
from src.modules.hill_climbing import hill_climbing_algorithm

# Abrir arquivo com as distâncias entre as cidades
file_path = os.path.join("src", "data", "five_d.txt")
arquivo = open(file_path, "r")
content = arquivo.readlines()
# Converter para uma matriz de adjacências
for i, item in enumerate(content):
    item = item.strip("\n")
    item = item.split(" ")
    content[i] = item
    while ("" in content[i]):
        content[i].remove("")

content = [[float(item) for item in sublist] for sublist in content]
rotas_matriz = np.array(content)

# Criar nós do grafo (as cidades)
cidade = nx.Graph()
cidade.add_nodes_from([i for i in range(1, len(rotas_matriz)+1)])
# Desenhar os nós pelo networkx
pos = nx.spring_layout(cidade)
nx.draw_networkx_nodes(cidade, pos, node_size=350)
nx.draw_networkx_labels(cidade, pos, font_size=12, font_family="sans-serif")

# Criar lista de adjacência com base na matriz de adjacência, com os pesos de cada aresta
rotas = []
for i, rota in enumerate(rotas_matriz):
    for j, peso in enumerate(rota):
        if (peso == 0):
            continue
        #print(f"[{i}] - [{j}] - {peso}")
        rotas.append((i + 1, j + 1, peso))
        
print(rotas)

cidade.add_weighted_edges_from(rotas)
nx.draw_networkx_edges(cidade, pos, width=2)
# Desenhar as arestas pelo networkx
edge_labels = nx.get_edge_attributes(cidade, "weight")
nx.draw_networkx_edge_labels(cidade, pos, edge_labels=edge_labels)

# Mostrar
plt.axis("off")
plt.show()

