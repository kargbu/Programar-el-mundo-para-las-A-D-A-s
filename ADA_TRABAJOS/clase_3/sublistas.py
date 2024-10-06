# Definición de una lista
mi_lista = ['a', 'b', 'c', 'd', 'e']

# Obtener una sublista del índice 1 al 4 (exclusivo)
sublista1 = mi_lista[1:4]
print(sublista1)

# Obtener una sublista desde el inicio hasta el índice 3 (exclusivo, no lo incluye)
sublista2 = mi_lista[:3]
print(sublista2)

# Obtener una sublista desde el inicio 2 hasta el final
sublista3 = mi_lista[2:]
print(sublista3)

# Obtener una sublista con índices pares
sublista4 = mi_lista[::2]
print(sublista4)

# Si el índice de inicio es mayor que el índice final, se crea una lista vacía
sublista5 = mi_lista[4:2]
print(sublista5)