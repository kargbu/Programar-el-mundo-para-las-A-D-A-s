# Crear una tupla

tupla_mixta = (1, 'Karina', 3.5)

# Mostrar completa la tupla
print('Tupla completa: ', tupla_mixta)

# Acceder a los elementos de una tupla por su índice (posición)
print('Primer elemento de la tupla: ', tupla_mixta[0])
print('Segundo elemento de la tupla: ', tupla_mixta[1])
print('Tercer elemento de la tupla: ', tupla_mixta[2])

# Explicación tuplas inmutables
print('\nLas tuplas no se pueden modificar. Intentemos hacerlo.')

# Mostremos qué alternativas tenemos
nueva_tupla = 1, 'Karina', 3.5
print(nueva_tupla)
nueva_tupla = 10, 'Karina', 3.5
print(nueva_tupla)