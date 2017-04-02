# class Edge:
#     __init__(self, weight):
#         self.weight = weight


# def create_graph(nodes=list(), edges=list()):
#     obj = dict()
#     for node in nodes:
#         obj[node] = dict()
#     for src, dest, weight in edges:
#         insert_edge(graph, src, dest, weight)
#     return obj

# def insert_node(graph, node):
#     graph[node] = dict()


# def insert_edge(graph, src, dest, weight=1)
#     graph[src][dest] = Edge(weight)


# def edge_exists(graph, src, dest):
#     return graph[src].get(dest, None) is not None


# def remove_edge(graph, src, dest):
#     graph[src].pop(key, None)


# def is_node_empty(graph, node):
#     return len(graph[node].values()) == 0


# def get_next_edge(graph, node, last_edge=None):
#     pass

# '''
#     void imprimeGrafo(TipoGrafo * grafo):
#     Imprime os vertices e arestas do grafo no seguinte formato:
#     v1:
#         (adj11, peso11)
#         (adj12, peso12)
#         ...
#     v2:
#         (adj21, peso21)
#         (adj22, peso22)
#         ...
#     Assuma que cada vértice é um inteiro de até 2 dígitos.
# '''


# def print_graph(graph):
#     pass


# def free_graph(graph):
#     pass


# '''
#     LeGrafo(nomearq, Grafo)
#     Le o arquivo nomearq e armazena na estrutura Grafo
#     Lay - out:
#         A 1a linha deve conter o número de vertices e o numero de arestas do grafo,
#         separados por espaço.
#         A 2a linha em diante deve conter a informacao de cada aresta, que consiste
#         no indice do vertice de origem, indice do vertice de destino e o peso da
#         aresta, tambem separados por espacos.
#         Observações:
#             Os vertices devem ser indexados de 0 a | V | -1
#             Os pesos das arestas sao numeros racionais nao negativos.

#     Exemplo:
#         O arquivo abaixo contem um grafo com 4 verticennnns(0, 1, 2, 3) e
#     7 arestas.

#     4 7
#     0 3 6.3
#     2 1 5.0
#     2 0 9
#     1 3 1.7
#     0 1 9
#     3 1 5.6
#     0 2 7.2

#     Codigo de saida:
#         1:
#             leitura bem sucedida
#         0:
#             erro na leitura do arquivo
# '''


# def read_graph(file):
#     pass


# def is_final_edge(graph, node, edge):
#     return get_next_edge(graph, node, edge) == None

# '''
#     recuperaAdj(v, p, u, peso, grafo):
#         dado um vertice v e um
#         ponteiro para uma aresta da lista de adjacencia de v,
#         devolve nas variaveis "peso" e "u" respectivamente o peso
#         da aresta e o numero do vertice adjacente
# '''


# def get_edge(graph, node, edge):
#     pass

