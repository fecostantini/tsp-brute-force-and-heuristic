from random import shuffle
from helpers import cronometrar, calcular_costo
from constantes import NODO_INICIAL, GRAFOS_FORMA_MATRICIAL, TAMAÑO_GRAFO_MAS_GRANDE, TAMAÑO_GRAFO

@cronometrar
def solucion_aleatoria(grafo, nodo_inicial=NODO_INICIAL):
    cantidad_nodos = len(grafo)
    solucion = [i for i in range(cantidad_nodos) if i != nodo_inicial]
    shuffle(solucion)


    costo = calcular_costo(grafo, solucion, nodo_inicial)
    return solucion, costo

if __name__ == "__main__":

    
    grafo = GRAFOS_FORMA_MATRICIAL[TAMAÑO_GRAFO]
    camino, costo = solucion_aleatoria(grafo)
    print(f'Tamaño grafo: {TAMAÑO_GRAFO} - camino: {camino} - costo: {costo}')

   