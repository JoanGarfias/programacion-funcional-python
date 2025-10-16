PI = 3.141592653589793

try:
    radio = float(input("Ingrese el radio del círculo: "))

    area = PI * (radio ** 2)

    print(f"El área del círculo es: {area:.2f}")

except ValueError:
    print("El valor ingresado no es un número válido.")
