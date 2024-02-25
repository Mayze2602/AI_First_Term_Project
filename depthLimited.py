from normalizeGraph import normalize

def limited_depth_search(graph, start, goal, limit=10):
    start = start.lower()
    goal = goal.lower()
    graph=normalize(graph)

    if start not in graph or goal not in graph:
        return "Start or end node does not exist."
    
    if start == goal:
        return [start]
    if limit == 0:
        return None
    for neighbor in graph.neighbors(start):
        path = limited_depth_search(graph, neighbor, goal, limit - 1)
        if path:
            return [start] + path
    return None