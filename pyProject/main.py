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
    os.system('pause')
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            print("Búsqueda a lo ancho")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            printRoute(execute_time(breadth_first_search, graph, start, end))
            print("<==============================================>")
            clear()
        elif opcion == 2:
            print("Búsqueda por profundidad")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            printRoute(execute_time(depth_first_search, graph, start, end))
            print("<==============================================>")
            clear()
        elif opcion == 3:
            print("Búsqueda por profundidad con limite")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            limit = int(input("Ingrese el límite: "))
            printRoute(execute_time(limited_depth_search, graph, start, end, limit))
            print("<==============================================>")
            clear()
        elif opcion == 4:
            print("Búsqueda por profundidad iterativa")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            printRoute(execute_time(iterative_depth, graph, start, end))
            clear()
        elif opcion == 5:
            print("Dikjstra")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            printRoute(execute_time(dijkstra_algorithm_search, graph, start, end))
            print("<==============================================>")
            clear()
        elif opcion == 6:
            print("Comparación de algoritmos")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            print("Búsqueda a lo ancho")
            printRoute(execute_time(breadth_first_search, graph, start, end))
            print("<==============================================>")
            print("Búsqueda por profundidad")
            printRoute(execute_time(depth_first_search, graph, start, end))
            print("<==============================================>")
            limit = int(input("Ingrese el límite: "))
            print("Búsqueda por profundidad con limite")
            printRoute(execute_time(limited_depth_search, graph, start, end, limit))
            print("<==============================================>")
            print("Búsqueda por profundidad iterativa")
            printRoute(execute_time(iterative_depth, graph, start, end))
            print("<==============================================>")
            print("Dikjstra")
            printRoute(execute_time(dijkstra_algorithm_search, graph, start, end))
            print("<==============================================>")
            clear()
        elif opcion == 7:
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()