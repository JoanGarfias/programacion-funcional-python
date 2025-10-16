# Ejercicio 1: Crear un diccionario de información de una persona
# Crea un diccionario que almacene el nombre, la edad y la ciudad de una persona.

persona = {
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Madrid"
}

# Ejercicio 2: Acceder y modificar valores de un diccionario
# Accede al valor de la clave "edad" e imprímelo. Luego, modifica el valor de la clave "ciudad" a "Barcelona".

print(persona["edad"])
persona["ciudad"] = "Barcelona"

# Ejercicio 3: Iterar sobre un diccionario
# Itera sobre las claves y valores del diccionario e imprímelos.

for clave, valor in persona.items():
  print(f"{clave}: {valor}")
