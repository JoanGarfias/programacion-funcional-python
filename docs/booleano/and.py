#
# EnunciadoEscribe un programa que simule la verificación de una temperatura.
# Declara una variable temperatura y asígnale el valor $22$.Declara dos variables booleanas:es_calido:
# Debe ser True si la temperatura es mayor o igual a $20$ Y menor o igual a $25$.es_extremo:
# Debe ser True si la temperatura es menor a $0$ O mayor a $40$.Utiliza los operadores de comparación (>=, <=, <, >)
# y el operador lógico and (para es_calido) y or (para es_extremo).Imprime el valor de ambas variables booleanas.

temperatura = -1

es_calido = temperatura >= 20 and temperatura <= 25
es_extremo = temperatura < 0 or temperatura > 40

if es_calido:
    print("Es calido")
elif es_extremo:
    print("Es extremo")
else:
    print("Es un dia normal xd")
