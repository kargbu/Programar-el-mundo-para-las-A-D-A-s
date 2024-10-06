# Definir una matriz 3 (filas) x 3 (columnas)

matriz_1 = [
    [1, 2, 3], # Fila 0
    [4, 5, 6], # Fila 1
    [7, 8, 9]  # Fila 2
]

# Acceder y mostrar algunos elementos específicos de la matriz_1

print(f'Algunos elementos de la matriz: {matriz_1}')
print(f'Elementos en la fila 0, columna 0 son los siguientes: {matriz_1[0][0]}')
print(f'Elemento de la fila 1, columna 2:  {matriz_1[1][2]}')

# Cambiar o modificar elementos específicos de la matriz
print('Algunos elementos de la matriz_1: ', matriz_1[0][1] == 2) # Cambiar el elemento en la fila
matriz_1[0][1] = 11
matriz_1[2][0] = 15
print('Matriz después de las modificaciones: ')
print(matriz_1)

#Acceder a una fila completa
print('\n Accediendo a una fila completa: ')
fila_completa = matriz_1[1] # Obtener toda la fila
print('Fila completa en la posición 1: ', fila_completa)

# Remplazar una fila completa
print('\nRemplazar una fila completa: ')
matriz_1[1] = [20, 21, 22]
print('Matriz después de reemplazar la fila 1: ')
print(matriz_1)

# Trabajar con una submatriz (parte de una matriz)

submatriz = [matriz_1[0][1:3], matriz_1[1][1:3]] # Extraer submatriz de las columnas 1 a 2
print('Submatriz: ', submatriz)
print(matriz_1[0])
print(matriz_1[1])
print(matriz_1[2])