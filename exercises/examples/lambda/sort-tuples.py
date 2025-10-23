# Lista de tuplas (nombre, edad)
personas = [('Ana', 25), ('Luis', 30), ('María', 20)]

# Ordenamos por edad (segundo elemento)
ordenadas = sorted(personas, key=lambda persona: persona[1])

print(ordenadas)
