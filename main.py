'''
Debe tener 1 menú de selección de algoritmos de búsqueda que permita elegir 1 sólo de manera individual y una opción que ejecuta todos a manera de comparación.
El código debe aceptar y funcionar sobre cualquier grafo utilizando la estructura que deseen los estudiantes
Se debe solicitar únicamente los requisitos de la búsqueda seleccionada según sea el caso
El código debe comprobar la entrada de los parámetros/nodos independientemente de su capitalización
Se debe tomar y comparar el tiempo de ejecución de cada algoritmo cuando se selecciona el "modo comparación" y presentar el algoritmo con el mejor tiempo y con la respuesta a la solución de la búsqueda de manera correcta
Todos los algoritmos deben entregar como salida el resultado de la búsqueda, ya sea el camino recorrido que resuleve el problema o el mensaje de error correspondiente
'''
import networkx as nx
from depthF import depth_first_search
from depthLimited import limited_depth_search
from iterativeDepth import iterative_depth
from breadthFirst import breadth_first_search
from dijkstra import dijkstra_algorithm_search
#import graph (variable G) from input_graph as graph
from input_graph import G as graph
def menu():
    print("1. Búsqueda a lo ancho")
    print("2. Búsqueda por profundidad")
    print("3. Búsqueda por profundidad con limite")
    print("4. Búsqueda por profundidad iterativa")
    print("5. Dikjstra")
    print("6. Comparación de algoritmos")
    print("7. Salir")
    return int(input("Seleccione una opción: "))

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            print("Búsqueda a lo ancho")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            print(breadth_first_search(graph, start, end))
        elif opcion == 2:
            print("Búsqueda por profundidad")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            print(depth_first_search(graph, start, end))
        elif opcion == 3:
            print("Búsqueda por profundidad con limite")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            limit = int(input("Ingrese el límite: "))
            print(limited_depth_search(graph, start, end, limit))
        elif opcion == 4:
            print("Búsqueda por profundidad iterativa")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            print(iterative_depth(graph, start, end))
        elif opcion == 5:
            print("Dikjstra")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            print(dijkstra_algorithm_search(graph, start, end))
        elif opcion == 6:
            print("Comparación de algoritmos")
            print("<==============================================>")
            start = input("Ingrese el nodo de inicio: ")
            end = input("Ingrese el nodo de destino: ")
            print("Búsqueda a lo ancho")
            print(breadth_first_search(graph, start, end))
            print("Búsqueda por profundidad")
            print(depth_first_search(graph, start, end))
            print("Búsqueda por profundidad con limite")
            limit = int(input("Ingrese el límite: "))
            print(limited_depth_search(graph, start, end, limit))
            print("Búsqueda por profundidad iterativa")
            print(iterative_depth(graph, start, end))
            print("Dikjstra")
            print(dijkstra_algorithm_search(graph, start, end))
        elif opcion == 7:
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()