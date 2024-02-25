from normalizeGraph import normalize

def depth_first_search(graph, start, goal,path=None):
    start = start.lower()
    goal = goal.lower()
    graph=normalize(graph)
    
    if start not in graph or goal not in graph:
        return "Start or end node does not exist."
    if path is None:
        path = []
    path.append(start)
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = depth_first_search(graph, neighbor, goal, path.copy())
            if new_path is not None:
                return new_path
    return None
