# Crea un sistema simple para determinar si un usuario es elegible para una promoción especial.
# Declara dos variables de entrada:edad con el valor $18$.tiene_membresia con el valor False.
# La promoción tiene dos condiciones de elegibilidad:
# Condición A: El usuario debe ser mayor de $16$ AÑOS Y debe tener una MEMBRESÍA.
# Condición B: El usuario no debe tener la Condición A (es decir, no es elegible por la regla A), PERO tiene $25$ años o más.
#

edad = 18
tiene_membresia = True

tiene_promocion = (edad > 16 and tiene_membresia) or (edad >= 25)
membresia_texto = ""
if tiene_membresia:
    membresia_texto = "con membresia"
else:
    membresia_texto = "sin membresia"

if tiene_promocion:
    print(f"La persona con edad {edad} {membresia_texto} es candidato a promoción")
else:
    print(f"La persona con edad {edad} NO es candidato a promoción")
