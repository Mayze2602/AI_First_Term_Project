from tools import normalizeGraph


def iterative_depth(graph, start, goal, step_by_step=False):
    start = start.lower()
    goal = goal.lower()
    graph = normalizeGraph(graph)

    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    if step_by_step:
        print(f"{start.title()} y {goal.title()} están en el grafo.")

    for depth in range(len(graph)):
        if step_by_step:
            print(f"Profundidad actual: {depth}")

        path = limited_depth_search(
            graph, start, goal, depth, step_by_step=step_by_step)
        if path:
            if step_by_step:
                print(f"Objetivo encontrado en nivel: {depth}")
            return path

    if step_by_step:
        print("No se encontró un camino dentro de los límites de profundidad dados.")
    return None


def dijkstra_algorithm_search(graph, start, goal, step_by_step=False):
    start = start.lower()
    goal = goal.lower()
    graph = normalizeGraph(graph)

    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    if step_by_step:
        print(f"{start.title()} y {goal.title()} están en el grafo.")

    shortest_path = {start: (None, 0)}
    current_node = start
    visited = set()
    while current_node != goal:
        if step_by_step:
            print("Nodo actual: ", current_node)
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_path[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node]["weight"] + \
                weight_to_current_node
            if next_node not in shortest_path:
                shortest_path[next_node] = (current_node, weight)
                if step_by_step:
                    print(
                        f"Agregando o actualizando nodo: {next_node.title()} con peso: {weight}")
            else:
                current_shortest_weight = shortest_path[next_node][1]
                if current_shortest_weight > weight:
                    shortest_path[next_node] = (current_node, weight)
                    if step_by_step:
                        print(
                            f"Actualizando el camino más corto para: {next_node.title()} con nuevo peso: {weight}")

        next_destinations = {node: shortest_path[node]
                             for node in shortest_path if node not in visited}
        if not next_destinations:
            return "Ruta no posible"

        current_node = min(next_destinations,
                           key=lambda k: next_destinations[k][1])
        if step_by_step:
            print("Siguiente nodo a visitar:", current_node.title())

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_path[current_node][0]
        current_node = next_node

    path.reverse()

    return path


def limited_depth_search(graph, start, goal, limit, step_by_step=False, visited=None):
    start = start.lower()
    goal = goal.lower()
    graph = normalizeGraph(graph)

    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    if step_by_step:
        print(f"{start.title()} y {goal.title()} están en el grafo con un límite de profundidad de {limit}.")

    if visited is None:
        visited = set()
        if step_by_step:
            print("Nodos visitados inicialmente: Ninguno")

    if start == goal:
        if step_by_step:
            print("Se encontró el camino:", start.title())
        return [start]

    if limit <= 0:
        if step_by_step:
            print("Límite de profundidad alcanzado sin encontrar el objetivo.")
        return None

    visited.add(start)
    if step_by_step:
        print("Visitando:", start.title(), "con límite restante:", limit)

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            if step_by_step:
                print("Explorando vecino:", neighbor.title())
            path = limited_depth_search(
                graph, neighbor, goal, limit-1, step_by_step, visited)
            if path:
                return [start] + path

    if step_by_step and start == list(visited)[0]:
        print("No se encontró un camino desde el nodo inicial con el límite de profundidad proporcionado.")
    else:
        if step_by_step:
            print("Retrocediendo desde:", start.title())
    return None


def depth_first_search(graph, start, goal, step_by_step=False, path=None):
    start = start.lower()
    goal = goal.lower()
    graph = normalizeGraph(graph)

    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    if step_by_step and path is None:
        print(f"{start.title()} y {goal.title()} están en el grafo.")

    if path is None:
        path = [start]
        if step_by_step:
            print("Camino inicial:", path)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            if step_by_step:
                print("Explorando desde:", start.title(),
                      "a vecino:", neighbor.title())
            new_path = depth_first_search(
                graph, neighbor, goal, step_by_step, path + [neighbor])
            if new_path:
                return new_path

    if step_by_step and start == path[0]:
        print("No se encontró un camino desde el nodo inicial.")
    else:
        if step_by_step:
            print("Retrocediendo desde:", start.title())
    return None


def breadth_first_search(graph, start, goal, step_by_step=False):
    start = start.lower()
    goal = goal.lower()
    graph = normalizeGraph(graph)

    if start not in graph or goal not in graph:
        return "El nodo de inicio o final no existe."
    if step_by_step:
        print(f"{start.title()} y {goal.title()} están en el grafo.")

    queue = [[start]]
    if step_by_step:
        print("Cola inicial:", queue)

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if step_by_step:
            print("Nodo actual:", node.title())

        if node == goal:
            return path

        for neighbor in graph.neighbors(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            if step_by_step:
                print("Se explora vecino y se actualiza la cola:", neighbor.title())

    if step_by_step:
        print("No se encontró un camino.")
    return None
