import networkx as nx
from normalizeGraph import normalize

def dijkstra_algorithm_search(graphOG, start, end):
    start = start.lower()
    end = end.lower()
    graph=normalize(graphOG)
    
    if start not in graph or end not in graph:
        return "Start or end node does not exist."
    shortest_path = {start: (None, 0)}
    current_node = start
    visited = set()
    while current_node != end:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_path[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node]["weight"] + weight_to_current_node
            if next_node not in shortest_path:
                shortest_path[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_path[next_node][1]
                if current_shortest_weight > weight:
                    shortest_path[next_node] = (current_node, weight)

        next_destinations = {node: shortest_path[node] for node in shortest_path if node not in visited}
        if not next_destinations:
            return "Route not possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_path[current_node][0]
        current_node = next_node
    path.reverse()
    
    return path