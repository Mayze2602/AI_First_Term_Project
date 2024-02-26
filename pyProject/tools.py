import networkx as nx
import time

def execute_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print("Execution time: ", round(end_time - start_time, 6), " seconds")
    return result

def normalizeGraph(graph_og):
    graph = nx.DiGraph()
    for node in graph_og.nodes():
        graph.add_node(node.lower())
    for edge in graph_og.edges(data=True):
        graph.add_edge(edge[0].lower(), edge[1].lower(), weight=edge[2]['weight'])
    return graph

def printRoute(route):
    if type(route) == str:
        print(route)
    elif route == None:
        print("Route not possible.")
    else:
        print("Route: ", end="")
        for i in range(len(route)):
            route[i] = route[i].title()
            print(route[i], end="")
            if i < len(route) - 1:
                print(" -> ", end="")
        print()