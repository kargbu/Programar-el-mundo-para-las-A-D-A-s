# Definición de una función con parámetros posicional y con nombre predeterminado
def presentacion_persona(nombre, edad, ciudad = 'Descnocida', profesion = 'Desconocida'):
    print(f'Nombre: {nombre}')
    print(f'Edad: {edad}') 
    print(f'Ciudad: {ciudad}')
    print(f'Profesión: {profesion}')

# Ejemplo de llamadas a la función

# Usando argumentos posicionales
print('Ejemplo con argumentos posicionales: ')
presentacion_persona('Karina', 44)

# Usando argumentos posicionales y con nombre
print('Ejemplo con argumentos posicionales y con nombre')
presentacion_persona('Marmol', 25, ciudad='México', profesion='Matemático')