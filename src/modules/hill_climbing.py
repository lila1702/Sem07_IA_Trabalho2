import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import time
from copy import deepcopy
#from desenhar_grafo import desenhar_grafo_rota

# Distancia total da rota
def calcular_tamanho_rota(rota, matriz_adj):
    distancia = 0    
    #print(f"Rota: {rota}")
    for i in range(len(rota)-1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i+1]
        distancia = distancia + matriz_adj[cidade_atual-1][proxima_cidade-1] # -1 para a cidade servir de índice para a matriz
    distancia = distancia + matriz_adj[rota[-1]-1][rota[0]-1] # Volta para a cidade inicial
    return distancia

def hill_climbing_algorithm(cidades, matriz_adj):
    tempo_inicial = time.perf_counter()
    passos_solucao = 0
    
    cidade_inicial = random.randint(1, len(cidades))
    num_cidades = len(cidades)
    # Definindo a rota inicial aleatória
    cidade_index = cidades.index(cidade_inicial)
    cidades.remove(cidade_inicial)
    melhor_rota = random.sample(cidades, num_cidades-1)
    melhor_rota = [x for x in melhor_rota[::-1]]
    melhor_rota.append(cidade_inicial)
    melhor_rota = [x for x in melhor_rota[::-1]]
    cidades.insert(cidade_index, cidade_inicial) # Colocar o estado inicial da cidade de volta no lugar
    
    melhor_distancia = calcular_tamanho_rota(melhor_rota, matriz_adj)
    
    no_improvement = False
    while (no_improvement != True):
        passos_solucao += 1
        
        # Gerar vizinhos
        vizinhos = []
        for i in range(num_cidades - 1):
            for j in range(i + 1, num_cidades):
                vizinho = deepcopy(melhor_rota)
                vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
                #print(f"vizinho[i]: {vizinho[i]}, vizinho: {vizinho}")
                if (vizinho[0] == cidade_inicial): # Apenas rotas que iniciam com a cidade determinada anteriormente
                    vizinhos.append(vizinho)
        
        # Avaliar vizinhos e encontrar o melhor
        melhor_vizinho = vizinhos[0]
        melhor_vizinho_distancia = calcular_tamanho_rota(melhor_vizinho, matriz_adj)
        
        for vizinho in vizinhos[1:]:
            distancia_vizinho = calcular_tamanho_rota(vizinho, matriz_adj)
            if (distancia_vizinho < melhor_vizinho_distancia):
                melhor_vizinho = vizinho
                melhor_vizinho_distancia = distancia_vizinho
        
        # Critério de parada: se não houver melhoria
        if (melhor_vizinho_distancia < melhor_distancia):
            melhor_rota = melhor_vizinho
            melhor_distancia = melhor_vizinho_distancia
        else:
            no_improvement = True
            
    tempo_final = time.perf_counter()
    tempo_percorrido = tempo_final - tempo_inicial
    print(f"Cidade Inicial: {cidade_inicial}")
    return melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao

# For testing purposes
if (__name__ == "__main__"):
    grafo = nx.Graph()
    cidades = list(range(1, 6))
    
    arestas = [
        (1, 2, 12),
        (1, 3, 15),
        (1, 4, 26),
        (1, 5, 11),
        (2, 3, 11),
        (2, 5, 23),
        (3, 5, 9),
        (4, 3, 4),
        (4, 2, 6),
        (5, 4, 90)
    ]
    
    grafo.add_nodes_from(cidades)
    grafo.add_weighted_edges_from(arestas)
    
    # pos = nx.spring_layout(grafo)
    # nx.draw_networkx_nodes(grafo, pos, node_size=650, node_color="purple")
    # nx.draw_networkx_labels(grafo, pos, labels={node: node for node in grafo.nodes()}, font_size=14, font_color="white", font_family="Impact")
    # nx.draw_networkx_edges(grafo, pos, width=2)
    # edge_labels = {(u, v): d['weight'] for u, v, d in grafo.edges(data=True)}
    # nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    
    # plt.axis("off")
    # plt.show()
    
    matriz_adj = nx.to_numpy_array(grafo, weight='weight')
    
    melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao = hill_climbing_algorithm(cidades, matriz_adj)
    #print(f"Melhor Rota: {melhor_rota}\nMelhor Distância: {melhor_distancia}\nTempo: {tempo_percorrido:.5f}\nPassos: {passos_solucao}")
    
    #desenhar_grafo_rota(grafo, melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao, cidades[0])