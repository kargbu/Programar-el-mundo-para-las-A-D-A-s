# 1. Declaración de variables y constantes

edad = 25
nombre = "Ana"
esta_estudiando = True

# Declaración de constantes
PI = 3.14
PAIS = "Argentina"

# Leer valores de teclafo
edad =  int(input('Introduce tu edad: ')) # lee un número entero
nombre = input('Introduce tu nombre: ') # lee una cadena de texto
esta_estudiando = input('¿Estás estudiando (sí/no): ').lower() == 'sí' #lee y convierte a booleano

# 3. Tipos de datos
cantidad_de_libros = 10
título_libro = "El Principito"
es_interesante = True
temas = ["Aventura", "Fantasía", "Filosofía"]
autor = {"nombre": "Antoine de Saint-Exupéry", "nacionalidad": "Francesa"}

# Convertir tipos de datos
edad_str = str(edad)
cantidad_de_libros_float = float(cantidad_de_libros) #convertir un número entero a un número racional

# 4. Imprimir resultados en la consola
print('Nombre: ', nombre)
print('Edad: ', edad)
print('¿Estás estudiando: ', esta_estudiando)
print('Constante pi: ', PI)
print('Constante país: ', PAIS)
print('Cantidad de libros: ', cantidad_de_libros)
print('Título del libro: ', título_libro)
print('¿Es interesante?: ', es_interesante)
print('Temas del libro: ', temas)
print('Autor del libro: ', autor)
print('Edad (como cadena de texto: )', edad_str)
print('Cantidad de libros (como float): ', cantidad_de_libros_float)