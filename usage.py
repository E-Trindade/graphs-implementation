import graph_am

with open('data/test_graph.txt') as file:
    graph = graph_am.read_graph(file)
    graph_am.print_graph(graph)
    print(graph_am.get_edge(graph, 3, 2))
