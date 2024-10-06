# Definición de una lista
mi_lista = ['a', 'b', 'c', 'd', 'e', 'f']

# Acceso usando índices positivos
primer_elemento = mi_lista[4]
segundo_elemento = mi_lista[5]
print('El quinto elemento de la lista es', primer_elemento)
print('El sexto elemento de la lista es', segundo_elemento)

# Acceso usando índices negativos
ultimo_elemento = mi_lista[-1]
penultimo_elemento = mi_lista[-2]
print('El último elemento de la lista es', ultimo_elemento)
print('El penúltimo elemento de la lista es', penultimo_elemento)

# Acesso a sublista (slicing)
print('Sublista de los índices 1 a 3:', mi_lista[1:4])
print('Sublista desde el inicio hasta el índice 3: ', mi_lista[:3+1])
print(f'Sublista desde el índice 2 hasta el final: {mi_lista[2:]}')

# Acceso con paso a slicing, los pasos son subsucesiones de índices
lis_1 = f'La sublista de índices pares es {mi_lista[::2]}'
print(lis_1)
lis_2 = f'La sublista con índices pares en el rango de 1 a 4 {mi_lista[1:5:2]}'
print(lis_2)

# Iteración a través de la lista
for i in mi_lista:
    print(i)
