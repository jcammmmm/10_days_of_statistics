import random
import sys
import math

SAMPLES = 1000000

# se ejecutan n instancias de la simulación con un beta que aumenta
# en 1 cada vez. Cada instancia consiste en generar 100 000 numeros 
# aleatorios entre el beta particular.
def main():
  for i in range(30):
    res = simulate_with_beta(i + 1)
    print(res[0], res[1], res[0] + res[1])

# La simulacion consiste en generar numeros aleatorios dentro del 
# rango particular. A partir del discriminante de la ecuacion 
# cuadratica (b*b - 4*a*c > 0) se identifica si la solucion es real
# o imaginaria. 
# Si la solucion es real se incrementa el contador de soluciones en 
# 1.  Al final se divide la cantidad de soluciones reales encontradas
# entre la cantidad total de pruebas. Este sera el porcentaje (proba-
# bilidad) reportada por la simulación
# La funcion retorna dos numeros. El primero, el valor calculado
# con esta simulacion. El segundo, mediante una ecuacion analitica.
def simulate_with_beta(beta):
  real_sol = 0
  for i in range(SAMPLES):
    a = 1
    b = random.random()*2*beta - beta
    c = random.random()*2*beta - beta
    if (discriminant(a, b, c)):
      real_sol = real_sol + 1
  return real_sol/SAMPLES, 2/(3*math.sqrt(beta))

# devuelve verdadero si la solución es real,
# falso de lo contrario
def discriminant(a, b, c):
  return b*b - 4*c > 0

if __name__ == '__main__':
  main()