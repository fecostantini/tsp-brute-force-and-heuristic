from math import sqrt
import random
import numpy as np
from helpers import cronometrar, calcular_costo
from constantes import NODO_INICIAL, GRAFOS_FORMA_MATRICIAL, TAMAÑO_GRAFO_MAS_GRANDE, TAMAÑO_GRAFO


class TSP_GA:
  def __init__(
        self, 
        grafo, 
        nodo_inicial=NODO_INICIAL, 
        cantidad_poblacion=100, 
        porcenaje_mutacion=0.05, 
        porcentaje_mutacion_gen=0.3, 
        generaciones=500):
   
      self.grafo = grafo
      self.nodo_inicial = nodo_inicial
      self.cantidad_poblacion = cantidad_poblacion
      self.porcentaje_mutacion = porcenaje_mutacion
      self.porcentaje_mutacion_gen = porcentaje_mutacion_gen
      self.nro_generaciones = generaciones

      
      self.cantidad_nodos = len(grafo)
      self.tamaño_individuo = self.cantidad_nodos - 1
      self.poblacion =  np.zeros((self.cantidad_poblacion, self.tamaño_individuo), dtype=int)
      self.cantidad_mas_aptos = int(sqrt(cantidad_poblacion))



  def crear_individuo(self):
    individuo = [i for i in range(self.cantidad_nodos) if i != self.nodo_inicial]
    random.shuffle(individuo)
    
    return individuo
  

  # La aptitud de un individuo está dada por su costo (mientras menor sea, más apto)
  def aptitud(self, individuo):
    return calcular_costo(self.grafo, individuo, self.nodo_inicial)


  def get_mas_aptos_con_indices(self):
    aptitudes_poblacion = np.array([self.aptitud(individuo) for individuo in self.poblacion])
    dtype=[('indice', int), ('aptitud', float)]

    aptitudes_poblacion_con_indices = np.array([(i, aptitud) for i, aptitud in zip(list(range(self.cantidad_poblacion)), aptitudes_poblacion)], dtype=dtype)
    aptitudes_poblacion_con_indices_ordenado = np.sort(aptitudes_poblacion_con_indices, order='aptitud').tolist() # aptitudes con indices, ordenados x aptitud en orden descendiente
    mas_aptos_con_indice = aptitudes_poblacion_con_indices_ordenado[0:self.cantidad_mas_aptos]
      
    return mas_aptos_con_indice

  def individuo_valido(self, individuo):
    return len(set(individuo)) == self.tamaño_individuo



  def cruza(self, a, b):

    hijo1, hijo2 = None, None
    hijo_elegido = None
    hijos_validos = False

    puntos_de_corte = list(range(1, self.cantidad_nodos)) # No se corta de ninguna de las dos puntas
    random.shuffle(puntos_de_corte)

    for punto in puntos_de_corte:
      porcion_a = a[0:punto]
      porcion_b = b[punto:]
      
      hijo1 = list(porcion_a) + list(porcion_b)
      hijo2 = list(porcion_b) + list(porcion_a)
      
      if self.individuo_valido(hijo1): 
         hijos_validos = True
         break
      
    if hijos_validos: hijo_elegido = hijo1 if random.random() > 0.5 else hijo2
    else:             hijo_elegido = a     if random.random() > 0.5 else b

    hijo_elegido = self.mutar(hijo_elegido) if random.random() < self.porcentaje_mutacion else hijo_elegido
    
    return hijo_elegido 
      

  def mutar(self, individuo):
    for i in range(self.tamaño_individuo):
      if random.random() < self.porcentaje_mutacion_gen:
        i1 = random.randint(0, self.tamaño_individuo-1)
        i2 = random.randint(0, self.tamaño_individuo-1)
            
        while i1 == i2: 
          if self.tamaño_individuo == 1: break # Nunca va a darse que i1 != i2
          i2 = random.randint(0, self.tamaño_individuo-1) # Nos aseguramos que sean dos elementos diferentes

        individuo[i1], individuo[i2] = individuo[i2], individuo[i1]

    return individuo

  @cronometrar
  def iniciar(self):
    mas_apto, fitness_mas_apto = None, None

    for i in range(self.cantidad_poblacion):
      self.poblacion[i] = self.crear_individuo()

    for gen in range(1, self.nro_generaciones+1):
      # Selección
      mas_aptos_con_indice = self.get_mas_aptos_con_indices()
      mas_aptos = np.array([self.poblacion[i] for i, _ in mas_aptos_con_indice])

      
      # Mejor individuo de toda la población
      mas_apto = mas_aptos[0]
      fitness_mas_apto = mas_aptos_con_indice[0][1]
      #print(f'Generación {gen} - {mas_apto} es el individuo más apto con un fitness de {fitness_mas_apto}') 
      # print(f'Generación {gen} - el más apto posee un fitness de {fitness_mas_apto}') 
  
      # Crossover
      nueva_poblacion = [mas_apto] # Mantenemos al más apto
      while len(nueva_poblacion) != self.cantidad_poblacion:
        padre = random.choice(mas_aptos)
        madre = random.choice(mas_aptos)
        nueva_poblacion.append(self.cruza(padre, madre))
  
      self.poblacion = nueva_poblacion

    mas_apto = (*mas_apto, self.nodo_inicial) # Agregamos el nodo inicial a la tupla más apta
    return mas_apto, fitness_mas_apto



if __name__ == "__main__":
 
  
  grafo = GRAFOS_FORMA_MATRICIAL[TAMAÑO_GRAFO]
  tsp = TSP_GA(grafo, cantidad_poblacion=100,generaciones=500, porcentaje_mutacion_gen=0.1)
    
  mejor_camino, costo_mejor_camino = tsp.iniciar()
  print(f'Tamaño grafo: {TAMAÑO_GRAFO} - mejor camino: {mejor_camino} - costo: {costo_mejor_camino}')
