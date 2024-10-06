# Ejemplo de una función que usa *args
def sum_num(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f'Suma de 1, 2, 3: {sum_num(1,2,3)}')

# Función que usa **kargs
def mostrar_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} : {valor}')
print('Ejemplo de la función: ')
mostrar_detalles(nombre='Ana', edad=30, ciudad='Madrid')

# Ejemplo combinado
def mostrar_info_completa(*args, **kwargs):
    print('Argumentos no nombrados: ')
    for arg in args:
        print(args)
    print('\nArgumentos nombrados: ')
    for clave, valor in kwargs.item():
        print(f'{clave} : {valor}')
    print('Ejemplo combinando argumentos de tuplas y diccionarios.')
    mostrar_info_completa(1, 2, 2, nombre='Karina', edad=30)

