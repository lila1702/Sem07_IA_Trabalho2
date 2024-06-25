# Sem07_IA_Trabalho2
Segundo trabalho da matéria de Inteligência Artificial da Universidade Federal do Ceará, do campus de Russas

Feito por: _Lila Maria_

## Objetivo

O trabalho possui a finalidade de solucionar o Travelling Salesman Problem, onde um Vendedor deve passar por todas as cidades da região, e depois retornar a cidade de origem, na menor rota possível. Foi solicitado a utilização de três algoritmos para essa finalidade:
1. [Hill Climbing Algorithm](https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/) (Algoritmo Descida de Encosta)
2. [Genetic Algorithm](https://www.geeksforgeeks.org/genetic-algorithms/) (Algoritmo Genético)
3. [Simulated Annealing Algorithm](https://www.geeksforgeeks.org/simulated-annealing/) (Algoritmo de Têmpera Simulada)

## Execução do Código

Para executar o código, é necessário possuir [Python](https://www.python.org/downloads/) instalado, e possuir as seguintes dependências instaladas: _matplotlib, networkx, numpy_

Ao ter Python instalado, você pode instalar as dependências através do comando:
```
pip install matplotlib networkx numpy
```

E após isso, execute o arquivo ```main.py``` na raíz do projeto para poder interagir com a interface do programa
<img src="https://i.imgur.com/WDuomCk.png">

Caso queira adicionar uma cidade própria para testar, coloque o arquivo .txt em src/data/, certificando-se de que ele tenha o formato de matriz de adjacências
Uma base de dados para usar como referência pode ser encontrada [aqui](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html)

## Exemplos:

A cidade onde o Salesman inicia é sempre desenhado em azul, e a rota utilizada por ele é representado em vermelho

<img src="https://i.imgur.com/xwpfkkg.png">
<img src="https://i.imgur.com/8nOkvzu.png">
<img src="https://i.imgur.com/GL4ehvz.png">
<img src="https://i.imgur.com/0Lw77ay.png">
