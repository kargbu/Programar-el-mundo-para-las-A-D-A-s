# Ejercicio 1. Crea un programa que reciba una lista de números y realice las
# siguientes operaciones


lis_num = [1,2,3,4,4,4,4,1,2,5,6,6,7,7,8,9]
# 1. Crea una lista para eliminar duplicados
set_num = set(lis_num)
print(set_num)

#2. Iterar sobre el conjunto set e imprime cada número
contador = 0
set_new = set()
for elemento in set_num:
    print(elemento)
    # Contar cuántos números son mayores que un valor dado y almacenar en un nuevo set
    if elemento < 5:
        contador += 1
        set_new.add(elemento)

print(f'Los números menores que 5 son: {set_new}')
print(f'La cantidad de números es {contador}')