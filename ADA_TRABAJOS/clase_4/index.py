# tupla.index(valor) solo devuelve la primera aparición
mi_tupla = 1, 2, 1, 1, 1, 6
print(mi_tupla)

i = mi_tupla.index(6)
print(f'El número 6 se encuentra en la posición {i} de la tupla')

# Verificar si un valor está en la tupla antes de buscar su índice
valor_buscado = 2
if valor_buscado in mi_tupla:
    indice_valor = mi_tupla.index(valor_buscado)
    print(f'El número {valor_buscado} se encuentra en la posición {indice_valor} de la tupla.')
else:
    print(f'El número {valor_buscado} no está en la tupla.')