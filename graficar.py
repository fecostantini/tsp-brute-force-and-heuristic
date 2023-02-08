import matplotlib.pyplot as plt
import numpy as np
"""
algoritmos = ['Naive', 'Alg. Genético', 'Random']
valores = [0, 0.5, 0]
ypos = np.arange(len(algoritmos))
plt.xticks(ypos, algoritmos)
plt.bar(ypos, valores)

plt.show()


# Tiempos de ejecución Algoritmo Genético
tamaño_grafo = [i for i in range(4, 21)]

tiempo = [0.50, 0.56, 0.57, 0.60, 0.62, 0.74, 0.83, 0.74, 0.84, 1.08, 0.90, 0.99, 1.04, 1.01, 1.15, 1.11, 1.29]

ypos = np.arange(len(tamaño_grafo))
plt.xticks(ypos, tamaño_grafo)
plt.bar(ypos, tiempo)
plt.title('Tiempos de ejecución Algoritmo Genético')
plt.ylabel('Tiempo (segundos)')
plt.xlabel('Tamaño del grafo')

plt.show()
"""
# Comparación de costos

"""
tamaño_grafo = [i for i in range(4, 21)]


costos_AG = [193, 190, 151, 103, 199, 190, 147, 232, 238, 222, 191, 355, 375, 322, 303, 322, 299]
costos_naive = [193, 190, 151, 103, 199, 190, 119, 193, 209, 197, 155, 188, 298, 191, 194, 211, 198]
costos_random = [193, 343, 272, 321, 457, 532, 620, 794, 718, 628, 787, 810, 881, 987, 914, 1042, 1116]

xpos = np.arange(len(tamaño_grafo))
plt.xticks(xpos, tamaño_grafo)
offset=0.25
plt.bar(xpos-offset, costos_random, width=0.20, label='Alg. Random')
plt.bar(xpos, costos_AG, width=0.20, label='Alg. Genético')
plt.bar(xpos+offset, costos_naive, width=0.20, label='Alg. Ingenuo')
plt.legend()
plt.title('Comparación de costos')
plt.ylabel('Costo de la solución')
plt.xlabel('Tamaño del grafo')

plt.show()

"""
# Tiempos de ejecución Algoritmo Genético



tamaño_grafo = [i for i in range(4, 21)]

tiempo = [0, 0, 0, 0.001, 0.01, 0.04, 0.3, 4.2, 64, 771, 10025, 140357, 2105355, 33685691, 572656759, 10307821666, 195848611658]


ypos = np.arange(len(tamaño_grafo))
plt.xticks(ypos, tamaño_grafo)
plt.bar(ypos, tiempo)
plt.title('Tiempos de ejecución Algoritmo Ingenuo')
plt.ylabel('Tiempo (segundos)')
plt.xlabel('Tamaño del grafo')

plt.show()
