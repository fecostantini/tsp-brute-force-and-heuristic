from random import randint
from functools import wraps
from time import time

def calcular_costo(grafo, solucion, nodo_inicial):
    costo = 0
    k = nodo_inicial

    for j in solucion:
        costo += grafo[k][j]
        k = j
    
    costo += grafo[k][nodo_inicial]
      
    return costo


"""
  Los grafos que se utilizan en el programa fueron creados por esta función y se encuentran guardados
  en la constante GRAFOS_FORMA_MATRICIAL en el archivo constantes.py
"""
def crear_grafo_matricial(cantidad_nodos):
   forma_matricial_grafo = [[0 for i in range(cantidad_nodos)] for i in range(cantidad_nodos)]

   for i in range(cantidad_nodos):
      for j in range(cantidad_nodos):
         if j < i: continue
         costo = randint(1,100) if i!=j else 0
         forma_matricial_grafo[i][j] = costo
         forma_matricial_grafo[j][i] = costo
   
   return forma_matricial_grafo


def cronometrar(f):
    @wraps(f)
    def wrap(*args, **kw):
        t_inicio = time()
        resultado = f(*args, **kw)
        t_final = time()
        tiempo = t_final - t_inicio
        print(f'{f.__name__} tomó {tiempo:2.4f} segundos')
        return resultado
    return wrap


def t(n): # Calcular el tiempo de ejecución del algoritmo ingenuo
    from math import factorial
    return factorial(n-1) / 1000000 * 1.61
