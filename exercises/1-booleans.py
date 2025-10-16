# Ejercicio 1: Comprobar si un número es par
# Escribe una función que tome un número como entrada y devuelva True si es par, y False si no lo es.

def es_par(numero):
  return numero % 2 == 0

# Ejercicio 2: Comprobar si una persona es mayor de edad
# Escribe una función que tome una edad como entrada y devuelva True si la persona es mayor o igual a 18 años, y False si no lo es.

def es_mayor_de_edad(edad):
  return edad >= 18

# Ejercicio 3: Comprobar si una cadena contiene una vocal
# Escribe una función que tome una cadena como entrada y devuelva True si contiene al menos una vocal (a, e, i, o, u), y False si no la tiene.

def contiene_vocal(cadena):
  for caracter in cadena:
    if caracter.lower() in "aeiou":
      return True
  return False
