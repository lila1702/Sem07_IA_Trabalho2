import random
import numpy as np
import time
import networkx as nx
import matplotlib.pyplot as plt

# Distancia total da rota
def calcular_tamanho_rota(rota, matriz_adj):
    distancia = 0    
    for i in range(len(rota)-1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i+1]
        distancia += matriz_adj[cidade_atual-1][proxima_cidade-1] # -1 para a cidade servir de índice para a matriz
    distancia += matriz_adj[rota[-1]-1][rota[0]-1] # Volta para a cidade inicial
    return distancia

# O fitness é o inverso da distância total da rota para que rotas mais curtas tenham maior fitness
def individual_fitness(rota, matriz_adj):
    return 1 / float(calcular_tamanho_rota(rota, matriz_adj))

# População inicial de rotas
def criar_populacao(cidades, tamanho_pop, cidade_inicial):
    populacao = []
    while (len(populacao) < tamanho_pop):
        individuo = random.sample(cidades, len(cidades))
        if (individuo[0] == cidade_inicial):
            populacao.append(individuo)  # Apenas rotas que iniciam na cidade inicial determinada
    return populacao

def selecionar_pais(populacao, fitness, num_pais):
    # Pesos "fitness" para selecionar pais com maior fitness
    pais = random.choices(populacao, weights=fitness, k=num_pais)
    return pais

# Crossover entre dois pais para criar dois filhos
def crossover(pai1, pai2):
    tamanho = len(pai1)
    ponto_corte = random.randint(1, tamanho - 1)
    
    # O filho 1 recebe a primeira parte do pai 1 e o resto das cidades do pai 2, na ordem em que aparecem
    filho1 = pai1[:ponto_corte] + [cidade for cidade in pai2 if cidade not in pai1[:ponto_corte]]
    # O filho 2 recebe a primeira parte do pai 2 e o resto das cidades do pai 1, na ordem em que aparecem
    filho2 = pai2[:ponto_corte] + [cidade for cidade in pai1 if cidade not in pai2[:ponto_corte]]
    
    return filho1, filho2

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        # Troca dois "genes" de lugar, aleatoriamente, segundo a probabilidade determinada
        if (random.random() < taxa_mutacao):
            j = random.randint(0, len(individuo) - 1)
            individuo[i], individuo[j] = individuo[j], individuo[i]

def genetic_algorithm(cidades, matriz_adj, tamanho_pop=100, taxa_mutacao=0.01):
    tempo_inicial = time.perf_counter()
    passos_solucao = 0

    # Escolhe uma cidade inicial aleatória
    cidade_inicial = random.choice(cidades)
    print(f"Cidade Inicial: {cidade_inicial}")
    
    populacao = criar_populacao(cidades, tamanho_pop, cidade_inicial)
    melhor_rota = None
    melhor_distancia = float('inf')
    geracoes_sem_melhoria = 0
    melhorou = True

    while (melhorou):
        # Calcula o fitness individual de cada rota na população de rotas
        fitness = [individual_fitness(individuo, matriz_adj) for individuo in populacao]
        nova_populacao = []

        # Gera uma nova população por crossover e mutação
        for _ in range(tamanho_pop // 2):
            pai1, pai2 = selecionar_pais(populacao, fitness, 2)
            filho1, filho2 = crossover(pai1, pai2)
            mutacao(filho1, taxa_mutacao)
            mutacao(filho2, taxa_mutacao)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao
        passos_solucao += 1
        melhorou = False

        # Verifica se a nova população possui uma solução melhor
        for individuo in populacao:
            distancia = calcular_tamanho_rota(individuo, matriz_adj)
            if (distancia < melhor_distancia):
                melhor_distancia = distancia
                melhor_rota = individuo
                melhorou = True

        if (not melhorou):
            geracoes_sem_melhoria += 1
        else:
            geracoes_sem_melhoria = 0

        # Termina após 2000 gerações sem melhoria
        if (geracoes_sem_melhoria >= 2000):
            break

    tempo_final = time.perf_counter()
    tempo_percorrido = tempo_final - tempo_inicial

    return melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao

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
    
    melhor_rota, melhor_distancia, tempo_percorrido, passos_solucao = genetic_algorithm(cidades, matriz_adj)
    print(f"Melhor Rota: {melhor_rota}")
    print(f"Melhor Distância: {melhor_distancia}")
    print(f"Tempo Percorrido: {tempo_percorrido}")
    print(f"Gerações: {passos_solucao}")
