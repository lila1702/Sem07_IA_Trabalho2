import random
import math
import numpy as np
import networkx as nx
import time

def calcular_tamanho_rota(rota, matriz_adj):
    # Calcula a distância total da rota.
    distancia = 0    
    for i in range(len(rota)-1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i+1]
        distancia += matriz_adj[cidade_atual-1][proxima_cidade-1] # -1 para a cidade servir de índice para a matriz
    distancia += matriz_adj[rota[-1]-1][rota[0]-1] # Volta para a cidade inicial
    return distancia

# Perturba a rota atual trocando a ordem de duas cidades aleatórias.
def perturbar(rota):
    # Cópia da rota atual
    nova_rota = rota[:]
    # Escolhe aleatoriamente dois índices diferentes para trocar as cidades
    i, j = random.sample(range(1, len(rota)), 2)  # Começa de 1 para não mudar a cidade inicial
    nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]
    return nova_rota

def criar_populacao_inicial(cidades, cidade_inicial, tamanho_pop):
    # Cria a população inicial de rotas onde todas iniciam com a cidade inicial.
    populacao = []
    while (len(populacao) < tamanho_pop):
        rota = random.sample(cidades, len(cidades))
        if (rota[0] == cidade_inicial):
            populacao.append(rota)
    return populacao

def tempera_simulada(cidades, matriz_adj, T_inicial=10000, T_min=1, alpha=0.995, max_iter=100000):
    # Aplica o algoritmo da têmpera simulada para solucionar o problema do Caixeiro Viajante.
    tempo_inicial = time.perf_counter()
    
    cidade_inicial = random.randint(1, len(cidades))  # Escolhe a cidade inicial
    
    # Cria a população inicial onde todas as rotas iniciam com a cidade inicial
    populacao = criar_populacao_inicial(cidades, cidade_inicial, tamanho_pop=100)
    rota = random.choice(populacao) # Escolhe uma rota aleatória da população inicial
    
    melhor_solucao = rota[:]
    melhor_custo = calcular_tamanho_rota(rota, matriz_adj)
    passos_solucao = 0  # Inicializa a contagem de passos com 0
    
    T = T_inicial # Inicialização da temperatura atual a partir da temperatura inicial
    
    while (T > T_min) and (max_iter > 0):
        rota_nova = perturbar(rota)
        # Calcula os custos da rota atual e da nova
        custo_atual = calcular_tamanho_rota(rota, matriz_adj)
        custo_novo = calcular_tamanho_rota(rota_nova, matriz_adj)
        # Calcula a variação de energia (o custo)
        delta_E = custo_novo - custo_atual
        # Aceita a nova rota se for melhor OU com uma probabilidade decrescente
        if (delta_E < 0) or (random.random() < math.exp(-delta_E / T)):
            rota = rota_nova
            if (custo_novo < melhor_custo):
                melhor_solucao = rota_nova[:]
                melhor_custo = custo_novo
                passos_solucao += 1  # Incrementa o contador de passos apenas quando há melhora
        
        # Reduz a temperatura multiplicando pelo fator de redução
        T *= alpha 
        # Decrementa o número máximo de iterações
        max_iter -= 1
    
    tempo_final = time.perf_counter()
    tempo_percorrido = tempo_final - tempo_inicial
    
    return melhor_solucao, melhor_custo, tempo_percorrido, passos_solucao

if __name__ == "__main__":
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
    
    matriz_adj = nx.to_numpy_array(grafo, weight='weight')
    
    melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao = tempera_simulada(cidades, matriz_adj)
    
    print(f"Melhor Rota: {melhor_rota}")
    print(f"Melhor Distância: {melhor_distancia}")
    print(f"Tempo percorrido: {tempo_percorrido:.6f} segundos")
    print(f"Passos: {passos_solucao}")
