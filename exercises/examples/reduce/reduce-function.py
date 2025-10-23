from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Sumamos todos los números
suma_total = reduce(lambda x, y: x + y, numeros)

print(suma_total)
