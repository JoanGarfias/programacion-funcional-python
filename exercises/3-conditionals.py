# Ejercicio 1: Comprobar si un número es positivo, negativo o cero
# Escribe una función que tome un número como entrada e imprima si es positivo, negativo o cero.

def comprobar_numero(numero):
  if numero > 0:
    print("El número es positivo")
  elif numero < 0:
    print("El número es negativo")
  else:
    print("El número es cero")

# Ejercicio 2: Asignar una calificación en función de una puntuación
# Escribe una función que tome una puntuación como entrada y devuelva una calificación en letra (A, B, C, D o F) según la siguiente escala:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

def asignar_calificacion(puntuacion):
  if puntuacion >= 90:
    return "A"
  elif puntuacion >= 80:
    return "B"
  elif puntuacion >= 70:
    return "C"
  elif puntuacion >= 60:
    return "D"
  else:
    return "F"

# Ejercicio 3: Determinar si un año es bisiesto
# Escribe una función que tome un año como entrada y devuelva True si es un año bisiesto, y False si no lo es.
# Un año es bisiesto si es divisible por 4, excepto los años que son divisibles por 100 pero no por 400.

def es_bisiesto(año):
  if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    return True
  else:
    return False
