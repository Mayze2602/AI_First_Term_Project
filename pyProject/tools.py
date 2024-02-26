import networkx as nx
import time
from timeit import Timer


import time

def execute_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print("Tiempo de ejecución: ", round(execution_time, 6), "segundos.")
    return result, execution_time


def normalizeGraph(graph_og):
    graph = nx.DiGraph()
    for node in graph_og.nodes():
        graph.add_node(node.lower())
    for edge in graph_og.edges(data=True):
        graph.add_edge(edge[0].lower(), edge[1].lower(),
                       weight=edge[2]['weight'])
    return graph


def printRoute(route):
    if type(route) == str:
        print(route)
    elif route == None:
        print("Ruta no posible.")
    else:
        print("Ruta: ", end="")
        for i in range(len(route)):
            route[i] = route[i].title()
            print(route[i], end="")
            if i < len(route) - 1:
                print(" -> ", end="")
        print()
