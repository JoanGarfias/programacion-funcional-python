nombreCompleto = "Pepe Sech" #str
edad = 20 #int
estatura = 1.75 #float
alumnos = ["Juan", "Maria", "Pedro"] #list
alumnos.append("Ana")
alumnos.remove("Juan")
alumnos.sort()
telefonos = ("iPhone 14", "iPhone 13", "iPhone 12") #tuple
telefonos = tuple(sorted(telefonos))
diccionario = {"nombre": "Pepe", "edad": 20, "estatura": 1.75} # diccionario

print("Nombre completo:", nombreCompleto)
print("Edad:", edad)
print("Estatura:", estatura)
print("Alumnos:", alumnos)
print("Telefonos:", telefonos)
print("Diccionario:", diccionario)

print("Tipo de dato de nombreCompleto:", type(nombreCompleto))
print("Tipo de dato de edad:", type(edad))
print("Tipo de dato de estatura:", type(estatura))
print("Tipo de dato de telefonos:", type(telefonos))
print("Tipo de dato de diccionario:", type(diccionario))
