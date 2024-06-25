import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
from src.modules.hill_climbing import hill_climbing_algorithm
from src.modules.desenhar_grafo import desenhar_grafo_rota
from src.modules.genetic_algorithm import genetic_algorithm
from src.modules.tempera_simulada import tempera_simulada

def set_up(filename, solver):
    # Abrir arquivo com as distâncias entre as cidades
    file_path = os.path.join("src", "data", filename)
    try:
        arquivo = open(file_path, "r")
    except:
        print("Erro ao abrir o arquivo. Verifique que o nome do arquivo foi digitado corretamente e que ele se encontra na pasta src/data")
        return
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
    
    # Hill Climbing Algorithm
    if (solver == 1):
        melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao = hill_climbing_algorithm(nos_cidades, rotas_matriz)
        desenhar_grafo_rota(cidade, melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao, melhor_rota[0])
    # Genetic Algorithm
    if (solver == 2):
        melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao = genetic_algorithm(nos_cidades, rotas_matriz)
        desenhar_grafo_rota(cidade, melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao, melhor_rota[0])
    # Têmpera Simulada
    if (solver == 3):
        melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao = tempera_simulada(nos_cidades, rotas_matriz)
        desenhar_grafo_rota(cidade, melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao, melhor_rota[0])


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
        if (user_choice == 3):
            set_up(filename, solver=2)
        if (user_choice == 4):
            set_up(filename, solver=3)
        
        user_choice = -1