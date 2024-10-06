# Usa la función lambda para definir la suma de dos números
Suma = lambda x, y : x+y
print(f'La suma de 5 + 3 = {Suma(5,3)}')

# Usa la función lambda para hacer cuadrados de una lista dada
list_num = [1, 2, 3, 4, 5, 6, 7]
cuadrados = map(lambda x: x** 2, list_num)
print(f'Los cuadrados de la lista son: {list_num} : {list(cuadrados)}')
