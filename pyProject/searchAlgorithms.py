from tools import normalizeGraph

def iterative_depth(graph, start, goal):
    start = start.lower()
    goal = goal.lower()
    graph=normalizeGraph(graph)
    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    for depth in range(len(graph)):
        path = limited_depth_search(graph, start, goal, depth)
        if path:
            print("Goal in level: ", depth)
            return path
    return None

def dijkstra_algorithm_search(graphOG, start, end):
    start = start.lower()
    end = end.lower()
    graph=normalizeGraph(graphOG)
    
    if start not in graph or end not in graph:
        return "El nodo de inicio o final no existe."
    shortest_path = {start: (None, 0)}
    current_node = start
    visited = set()
    while current_node != end:
        print("Current node: ", current_node)
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
            return "Ruta no posible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_path[current_node][0]
        current_node = next_node
    path.reverse()
    
    return path

def limited_depth_search(graph, start, goal, limit, visited=None):
    start = start.lower()
    goal = goal.lower()
    graph=normalizeGraph(graph)
    if visited is None:
        visited = set()

    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    
    if start == goal:
        return [start]
    if limit == 0:
        return None
    visited.add(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            print("Current node: ", neighbor)
            path = limited_depth_search(graph, neighbor, goal, limit - 1, visited)
            if path:
                return [start] + path
    return None

def depth_first_search(graph, start, goal,path=None):
    start = start.lower()
    goal = goal.lower()
    graph=normalizeGraph(graph)
    
    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    if path is None:
        path = []
    path.append(start)
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        print("Current node: ", neighbor)
        if neighbor not in path:
            new_path = depth_first_search(graph, neighbor, goal, path.copy())
            if new_path is not None:
                return new_path
    return None

def breadth_first_search(graph, start, goal):
    start = start.lower()
    goal = goal.lower()
    graph=normalizeGraph(graph)
    
    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    queue = [[start]]
    while queue:
        print("Current node: ", queue[0][-1])
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.neighbors(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None