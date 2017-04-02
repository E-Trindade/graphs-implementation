class Edge:

    def __init__(self, weight):
        self.weight = weight
    
    def __str__(self):
        return '<graph_am.Edge weight=%f>' %self.weight

def create_graph(nodes_range, edges=list()):
    graph = [[None] * nodes_range] * nodes_range
    for src, dest, weight in edges:
        insert_edge(graph, src, dest, weight)
    return graph


def insert_edge(graph, src, dest, weight=1):
    graph[src][dest] = Edge(weight)


def edge_exists(graph, src, dest):
    return graph[src][dest] is not None


def remove_edge(graph, src, dest):
    graph[src][key] = None


def is_node_empty(graph, node):
    for edge in graph[node]:
        if edge != None:
            return True
    return False


def get_next_edge(graph, node, last_edge=None):
    if len(graph[node]) == 0:
        return None

    if last_edge is None:
        return graph[0]

    for index, edge in enumerate(graph[node][:-1]):
        if edge == last_edge:
            return graph[node][index + 1]

    # raise ValueError('Edge Not Found')
    return None

'''
    void imprimeGrafo(TipoGrafo * grafo):
    Imprime os vertices e arestas do grafo no seguinte formato:
    v1:
        (adj11, peso11)
        (adj12, peso12)
        ...
    v2:
        (adj21, peso21)
        (adj22, peso22)
        ...
    Assuma que cada vértice é um inteiro de até 2 dígitos.
'''


def print_graph(graph):
    for i, edge_list in enumerate(graph):
        for j, edge in enumerate(edge_list):
            if edge:
                print('(edge %d-%d => %s)' % (i, j, edge.weight))


def free_graph(graph):
    pass


'''
    LeGrafo(nomearq, Grafo)
    Le o arquivo nomearq e armazena na estrutura Grafo
    Layout:
        A 1a linha deve conter o número de vertices e o numero de arestas do grafo,
        separados por espaço.
        A 2a linha em diante deve conter a informacao de cada aresta, que consiste
        no indice do vertice de origem, indice do vertice de destino e o peso da
        aresta, tambem separados por espacos.
        Observações:
            Os vertices devem ser indexados de 0 a | V | -1
            Os pesos das arestas sao numeros racionais nao negativos.

    Exemplo:
        O arquivo abaixo contem um grafo com 4 vertice(0, 1, 2, 3) e
    7 arestas.

    4 7
    0 3 6.3
    2 1 5.0
    2 0 9
    1 3 1.7
    0 1 9
    3 1 5.6
    0 2 7.2

    Codigo de saida:
        True:
            leitura bem sucedida
        False:
            erro na leitura do arquivo
'''


def read_graph(file):
    graph = None
    for index, line in enumerate(file.readlines()):
        if index == 0:
            node_number, edge_number = line.split(' ')
            graph = create_graph(int(node_number))
        else:
            src, dest, weight = line.split(' ')
            graph[int(src)][int(dest)] = Edge(float(weight))
    return graph


def is_final_edge(graph, node, edge):
    return get_next_edge(graph, node, edge) == None

'''
    recuperaAdj(v, p, u, peso, grafo):
        dado um vertice v e um
        ponteiro para uma aresta da lista de adjacencia de v,
        devolve nas variaveis "peso" e "u" respectivamente o peso
        da aresta e o numero do vertice adjacente
'''


def get_edge(graph, src, dest):
    return graph[src][dest]
