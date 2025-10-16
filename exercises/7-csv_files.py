import csv

# Ejercicio 1: Leer un archivo CSV y imprimir su contenido
# Escribe una función que tome el nombre de un archivo CSV como entrada y lea su contenido, imprimiendo cada fila.

def leer_csv(nombre_archivo):
  with open(nombre_archivo, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
      print(fila)

# Ejercicio 2: Leer un archivo CSV y procesar los datos
# Escribe una función que lea el archivo 'people.csv' y calcule la edad promedio de las personas en el archivo.

def calcular_edad_promedio(nombre_archivo):
  edades = []
  with open(nombre_archivo, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Omitir la fila de encabezado
    for fila in lector_csv:
      edades.append(int(fila[1]))
  return sum(edades) / len(edades)

# Ejercicio 3: Escribir en un archivo CSV
# Escribe una función que tome una lista de listas como entrada y la escriba en un nuevo archivo CSV.

def escribir_csv(nombre_archivo, datos):
  with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)

# Ejemplo de uso
leer_csv('/home/joangarfias/DISCO/REPOSITORIOS/programacion-funcional-python/exercises/people.csv')
print(f"La edad promedio es: {calcular_edad_promedio('/home/joangarfias/DISCO/REPOSITORIOS/programacion-funcional-python/exercises/people.csv')}")
nuevos_datos = [['Nombre', 'Edad', 'Ciudad'], ['Ana', '25', 'Valencia'], ['Luis', '40', 'Bilbao']]
escribir_csv('/home/joangarfias/DISCO/REPOSITORIOS/programacion-funcional-python/exercises/nuevas_personas.csv', nuevos_datos)
