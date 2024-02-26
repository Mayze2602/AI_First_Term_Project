from searchAlgorithms import breadth_first_search, depth_first_search, limited_depth_search, iterative_depth, dijkstra_algorithm_search
from input_graph import G as graph
from tools import printRoute, execute_time
import os


def menu():
    print("1. Búsqueda a lo ancho")
    print("2. Búsqueda por profundidad")
    print("3. Búsqueda por profundidad con limite")
    print("4. Búsqueda por profundidad iterativa")
    print("5. Dikjstra")
    print("6. Comparación de algoritmos")
    print("7. Salir")
    return int(input("Seleccione una opción: "))


def clear():
    if os.name == 'nt':
        os.system('pause')
        os.system('cls')
    else:
        print("Presione enter para continuar...")
        input()
        os.system('clear')


def main():
    while True:
        opcion = menu()

        if opcion == 1:
            print("Búsqueda a lo ancho")
            print("<==============================================>")
            print("Modo:")
            print("1. Directo")
            print("2. Explicación paso a paso")
            print("<==============================================>")
            modo = int(input("Seleccione una opción: "))
            if modo == 1:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                print("")
                route, execTime = execute_time(
                    breadth_first_search, graph, start, end)
                printRoute(route)
            elif modo == 2:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                printRoute(breadth_first_search(graph, start, end, True))
            print("<==============================================>")
            clear()

        elif opcion == 2:
            print("Búsqueda por profundidad")
            print("<==============================================>")
            print("Modo:")
            print("1. Directo")
            print("2. Explicación paso a paso")
            print("<==============================================>")
            modo = int(input("Seleccione una opción: "))
            if modo == 1:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                route, execTime = execute_time(
                    depth_first_search, graph, start, end)
                printRoute(route)
            elif modo == 2:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                printRoute(depth_first_search(graph, start, end, True))
            print("<==============================================>")
            clear()

        elif opcion == 3:
            print("Búsqueda por profundidad con limite")
            print("<==============================================>")
            print("Modo:")
            print("1. Directo")
            print("2. Explicación paso a paso")
            print("<==============================================>")
            modo = int(input("Seleccione una opción: "))
            if modo == 1:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                limit = int(input("Ingrese el límite: "))
                route, execTime = execute_time(
                    limited_depth_search, graph, start, end, limit)
                printRoute(route)
            elif modo == 2:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                limit = int(input("Ingrese el límite: "))
                printRoute(limited_depth_search(
                    graph, start, end, limit, True))
            print("<==============================================>")
            clear()

        elif opcion == 4:
            print("Búsqueda por profundidad iterativa")
            print("<==============================================>")
            print("Modo:")
            print("1. Directo")
            print("2. Explicación paso a paso")
            print("<==============================================>")
            modo = int(input("Seleccione una opción: "))
            if modo == 1:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                route, execTime = execute_time(
                    iterative_depth, graph, start, end)
                printRoute(route)
            elif modo == 2:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                printRoute(iterative_depth(graph, start, end, True))
            print("<==============================================>")
            clear()

        elif opcion == 5:
            print("Dikjstra")
            print("<==============================================>")
            print("Modo:")
            print("1. Directo")
            print("2. Explicación paso a paso")
            print("<==============================================>")
            modo = int(input("Seleccione una opción: "))
            if modo == 1:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                route, execTime = execute_time(
                    dijkstra_algorithm_search, graph, start, end)
                printRoute(route)
            elif modo == 2:
                start = input("Ingrese el nodo de inicio: ")
                end = input("Ingrese el nodo de destino: ")
                printRoute(dijkstra_algorithm_search(graph, start, end, True))
            print("<==============================================>")
            clear()

        elif opcion == 6:
            print("Comparación de algoritmos")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            times = {}
            print("Búsqueda a lo ancho")
            path, execTime = execute_time(
                breadth_first_search, graph, start, end)
            printRoute(path)
            if type(path) == list:
                times["Búsqueda a lo ancho"] = execTime
            print("<==============================================>")
            print("Búsqueda por profundidad")
            path, execTime = execute_time(
                depth_first_search, graph, start, end)
            printRoute(path)
            if type(path) == list:
                times["Búsqueda por profundidad"] = execTime
            print("<==============================================>")
            limit = int(input("Ingrese el límite: "))
            print("Búsqueda por profundidad con limite")
            path, execTime = execute_time(
                limited_depth_search, graph, start, end, limit)
            printRoute(path)
            if type(path) == list:
                times["Búsqueda por profundidad con limite"] = execTime
            print("<==============================================>")
            print("Búsqueda por profundidad iterativa")
            path, execTime = execute_time(iterative_depth, graph, start, end)
            printRoute(path)
            if type(path) == list:
                times["Búsqueda por profundidad iterativa"] = execTime
            print("<==============================================>")
            print("Dikjstra")
            path, execTime = execute_time(
                dijkstra_algorithm_search, graph, start, end)
            printRoute(path)
            if type(path) == list:
                times["Dikjstra"] = execTime
            print("<==============================================>")
            if times:
                print("Ranking de algoritmos:")
                # sort the dictionary by value from fastest to slowest
                num = 1
                for key, value in sorted(times.items(), key=lambda item: item[1]):
                    print(f"\t{num}.- {key}: {value} segundos.")
                    num += 1
            clear()
        elif opcion == 7:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
