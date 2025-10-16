a = 8
b = 0

try:
    division = a / b
    print(f"La división de {a} y {b} es: {division}")
except ZeroDivisionError:
    print("No se puede dividir por cero")
