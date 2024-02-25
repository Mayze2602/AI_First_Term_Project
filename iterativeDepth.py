from normalizeGraph import normalize

def limited_depth_search(graph, start, goal, limit):
    start = start.lower()
    end = end.lower()
    graph=normalize(graph)

    if start == goal:
        return [start]
    if limit == 0:
        return None
    for neighbor in graph.neighbors(start):
        path = limited_depth_search(graph, neighbor, goal, limit - 1)
        if path:
            return [start] + path
    return None

def iterative_depth(graph, start, goal):
    if start not in graph or goal not in graph:
        return "Start or end node does not exist."
    for depth in range(len(graph)):
        path = limited_depth_search(graph, start, goal, depth)
        if path:
            print("Goal in level: ", depth)
            return path
    return None
