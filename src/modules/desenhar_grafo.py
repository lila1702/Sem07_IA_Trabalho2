import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo_rota(grafo, rota, melhor_distancia, tempo_percorrido, passos_solucao, cidade_inicial):
    pos = nx.spring_layout(grafo)
    # Desenha todos os nós em roxo
    nx.draw_networkx_nodes(grafo, pos, nodelist=[node for node in grafo.nodes() if node != cidade_inicial], node_size=650, node_color="purple")
    # Desenha o nó da cidade inicial em azul
    nx.draw_networkx_nodes(grafo, pos, nodelist=[cidade_inicial], node_size=650, node_color="blue")
    nx.draw_networkx_labels(grafo, pos, labels={node: node for node in grafo.nodes()}, font_size=14, font_color="white", font_family="Impact")
    
    # Desenha todas as arestas em cinza
    nx.draw_networkx_edges(grafo, pos, width=2, edge_color="gray")
    
    # Desenha as arestas da melhor rota em vermelho
    edge_list = [(rota[i], rota[i + 1]) for i in range(len(rota) - 1)] + [(rota[-1], rota[0])]
    nx.draw_networkx_edges(grafo, pos, edgelist=edge_list, width=2, edge_color="red")
    
    edge_labels = {(u, v): d['weight'] for u, v, d in grafo.edges(data=True)}
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)
    
    # Adiciona as legendas fora da área do gráfico
    plt.figtext(0.99, 0.01, f"Melhor Distância: {melhor_distancia}\nTempo de Execução: {tempo_percorrido:.5f} segundos\nPassos: {passos_solucao}", horizontalalignment='right', fontsize=12)
    
    plt.axis("off")
    plt.show()