numeros = [1, 2, 3, 4, 5, 6, 7]
impares_cuadrados = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0,
numeros)))
print(impares_cuadrados)
# Salida: [1, 9, 25, 49]
