def sumar_todos(container):
 """Funciona con cualquier contenedor iterable cuyos elementos sean
sumables."""
 total = 0
 for x in container:
 total += x
 return total
print(sumar_todos([1,2,3])) # 6
print(sumar_todos((10, 20))) # 30
print(sumar_todos(x for x in [4,5])) # 9
