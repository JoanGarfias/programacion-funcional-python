from functools import reduce
numeros = [-3, -1, 0, 2, 4, 6]
dobles_positivos = list(map(lambda x: x * 2, filter(lambda x: x > 0,
numeros)))
suma = reduce(lambda x, y: x + y, dobles_positivos)
print(suma)
# Salida: 24 (porque 2*2 + 4*2 + 6*2 = 24)
