# Ejercicio 1: Crear una tupla y acceder a sus elementos
# Crea una tupla con 3 elementos y accede al segundo elemento.

mi_tupla = (1, "hola", 3.14)
print(mi_tupla[1])

# Ejercicio 2: Desempaquetar una tupla
# Crea una tupla con el nombre y la edad de una persona y desempaquétala en dos variables.

persona = ("Juan", 30)
nombre, edad = persona
print(nombre)
print(edad)

# Ejercicio 3: Intentar modificar una tupla
# Intenta modificar el primer elemento de la tupla y observa el error. Las tuplas son inmutables.

# mi_tupla[0] = 2 # Esto generará un TypeError
