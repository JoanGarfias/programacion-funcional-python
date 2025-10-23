cadena = "Pepe"
num = 6
longitud = len(cadena)

if longitud > num:
    print(f"La cadena tiene {longitud} carácteres que {num}")
elif longitud < num:
    print(f"La cadena tiene {longitud}, es menor a {num}")
else:
    print(f"La cadena tiene exactamente {num} carácteres")
