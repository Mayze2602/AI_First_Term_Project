import networkx as nx
def normalize(graph_og):
    graph = nx.DiGraph()
    for node in graph_og.nodes():
        graph.add_node(node.lower())
    for edge in graph_og.edges(data=True):
        graph.add_edge(edge[0].lower(), edge[1].lower(), weight=edge[2]['weight'])
    return graph