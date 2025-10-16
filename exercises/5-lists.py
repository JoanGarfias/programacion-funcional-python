# Ejercicio 1: Crear una lista de números y acceder a sus elementos
# Crea una lista de 5 números y accede al primer y último elemento.

numeros = [1, 2, 3, 4, 5]
print(numeros[0])
print(numeros[-1])

# Ejercicio 2: Modificar una lista
# Añade un nuevo número al final de la lista. Luego, elimina el segundo elemento de la lista.

numeros.append(6)
numeros.pop(1)

# Ejercicio 3: Ordenar una lista
# Ordena la lista de números en orden ascendente.

numeros.sort()
print(numeros)
