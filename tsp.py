from sys import maxsize
from itertools import permutations
from pprint import pprint
from math import factorial
from helpers import crear_grafo_matricial, cronometrar, calcular_costo
from constantes import NODO_INICIAL, GRAFOS_FORMA_MATRICIAL, TAMAÑO_GRAFO_MAS_GRANDE, TAMAÑO_GRAFO

@cronometrar
def TSP(grafo, nodo_inicial=NODO_INICIAL):
 
  cantidad_nodos = len(grafo)
  nodos = (i for i in range(cantidad_nodos) if i != nodo_inicial) # todos los nodos menos el inicial
   
  menor_costo = maxsize
  mejor_camino = None

  permutaciones_posibles = permutations(nodos)
   
  for solucion in permutaciones_posibles:
      
    costo_camino_actual = calcular_costo(grafo, solucion, nodo_inicial)

    if costo_camino_actual < menor_costo:
      menor_costo = costo_camino_actual
      mejor_camino = solucion
      
  mejor_camino = (*mejor_camino, nodo_inicial) # Agregamos el nodo inicial a la tupla solución
  return mejor_camino, menor_costo



if __name__ == "__main__":
  """
   for tamaño_grafo in range(1, TAMAÑO_GRAFO_MAS_GRANDE+1):
      grafo_actual = GRAFOS_FORMA_MATRICIAL[tamaño_grafo]
      mejor_camino, costo_mejor_camino = TSP(grafo_actual)
      print(f'Tamaño grafo: {tamaño_grafo} - mejor camino: {mejor_camino} - costo: {costo_mejor_camino}')
  """

  grafo = GRAFOS_FORMA_MATRICIAL[TAMAÑO_GRAFO]
  mejor_camino, costo_mejor_camino = TSP(grafo)
  print(f'Tamaño grafo: {TAMAÑO_GRAFO} - mejor camino: {mejor_camino} - costo: {costo_mejor_camino}')
   
   