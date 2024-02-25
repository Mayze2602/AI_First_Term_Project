from normalizeGraph import normalize

def breadth_first_search(graph, start, goal):
    start = start.lower()
    goal = goal.lower()
    graph=normalize(graph)
    
    if start not in graph or goal not in graph:
        return "Start or end node does not exist."
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.neighbors(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return None