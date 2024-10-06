# Lista inicial
mi_lista = [10, 20, 30, 40, 50]
print("Lista original: ", mi_lista)

# Actualizar un elemento en específico
mi_lista[2] = 35
print("Lista después de actualizar el tercer elemento: ", mi_lista)

# Actualizar un elemento usando índice negativo
mi_lista [-1] = 0
lisi = f'Lista después de actualizar el último elemento es {mi_lista}'
print(lisi)

# Actualizar varios elementos usando slicing
mi_lista[0:-1] = [10, 1000]
print('Lista después de actualizar un rango de elementos: ', mi_lista)

#Actualizar elementos basado en una condición
for i in range(len(mi_lista)):
    if mi_lista[i] < 10:
        mi_lista[i] += 1
print('Lista después de actualizar elementos menores que 10', mi_lista)