from functools import reduce

numeros = [10, 25, 3, 89, 42]

mayor = reduce(lambda x, y: x if x > y else y, numeros)

print(mayor)
