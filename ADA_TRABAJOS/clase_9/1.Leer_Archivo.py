# Paso 1 definimos nombre archivo

nombre_archivo = 'archivo.txt'

# Paso 2. Leemos todo el contenido de una sola vez

with open(nombre_archivo, 'r') as archivo:
    print('Leyendo el archivo de una vez con read (): ')
    contenido_completo = archivo.red()
    print(contenido_completo)
    print('-' * 40)