import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import os
from src.modules.hill_climbing import hill_climbing_algorithm
from src.modules.desenhar_grafo import desenhar_grafo_rota

def set_up(filename, solver):
    # Abrir arquivo com as distâncias entre as cidades
    file_path = os.path.join("src", "data", filename)
    arquivo = open(file_path, "r")
    content = arquivo.readlines()
    # Converter para uma matriz de adjacências
    for i, item in enumerate(content):
        item = item.strip("\n").split(" ")
        content[i] = [float(k) for k in item if k != ""]

    rotas_matriz = np.array(content)

    # Criar nós do grafo (as cidades)
    cidade = nx.Graph()
    nos_cidades = [i for i in range(1, len(rotas_matriz)+1)]
    
    cidade.add_nodes_from(nos_cidades)

    # Desenhar os nós pelo networkx
    # pos = nx.spring_layout(cidade)
    # nx.draw_networkx_nodes(cidade, pos, node_size=500, node_color="purple")
    # nx.draw_networkx_labels(cidade, pos, font_size=12, font_family="Impact", font_color="white")

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
    # nx.draw_networkx_edges(cidade, pos, width=2, edge_color="gray")
    # # Desenhar as arestas pelo networkx
    # edge_labels = nx.get_edge_attributes(cidade, "weight")
    # nx.draw_networkx_edge_labels(cidade, pos, edge_labels=edge_labels)

    # Mostrar
    # plt.axis("off")
    # plt.show()
    
    # Hill Climbing Algorithm
    if (solver == 1):
        melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao = hill_climbing_algorithm(nos_cidades, rotas_matriz)
        desenhar_grafo_rota(cidade, melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao, melhor_rota[0])
    # Genetic Algorithm
    if (solver == 2):
        pass
    # Têmpera Simulada
    if (solver == 3):
        pass


if (__name__ == "__main__"):
    print("[1] - Escolher arquivo para importar como cidade (o arquivo deve estar em src/data)")
    print("[2] - Hill Climbing Algorithm")
    print("[3] - Genetic Algorithm")
    print("[4] - Têmpera Simulada")
    print("[0] - Sair")
    user_choice = -1
    filename = "five_d.txt"
    
    while (user_choice != 0):
        user_choice = int(input("Digite a opção desejada: "))
        if (user_choice == 0):
            break
        if (user_choice == 1):
            filename = input("Digite o nome do arquivo: ")
            if (filename.endswith(".txt") == False):
                filename += ".txt"
        if (user_choice == 2):
            set_up(filename, solver=1)
        
        user_choice = -1