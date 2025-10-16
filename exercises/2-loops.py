# Ejercicio 1: Imprimir los números del 1 al 10
# Escribe un bucle que imprima los números del 1 al 10, cada uno en una nueva línea.

for i in range(1, 11):
  print(i)

# Ejercicio 2: Calcular la suma de una lista de números
# Escribe una función que tome una lista de números como entrada y devuelva la suma de todos los números en la lista.

def sumar_lista(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma

# Ejercicio 3: Encontrar el número más grande en una lista
# Escribe una función que tome una lista de números como entrada y devuelva el número más grande de la lista.

def encontrar_maximo(numeros):
  maximo = numeros[0]
  for numero in numeros:
    if numero > maximo:
      maximo = numero
  return maximo
