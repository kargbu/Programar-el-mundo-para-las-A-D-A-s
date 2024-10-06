# Creación del menú de opciones

def menu_opciones():
    print('Selecciona el número de la opción')

    print('1. Agregar película')
    print('2. Lista de películas')
    print('3. Eliminar catálogo')
    print('4. Salir')

# 1. Función agregar película
def agregar_peli():
    print('Seleccionaste la opción de agregar película')
    with open('catalogo_pelis_1.txt', 'a') as catalogo:
        catalogo.write(input('Escribe el título de la película.\n '))

# 2. Lista de películas
def lista_pelis():
    print('Seleccionaste la opción de lista de películas')

# 3. Eliminar catálogo
def eliminar_catalogo():
    print('Seleccionaste la opción de eliminar catálogo')

# 4. Salir
def salir():
    print('Seleccionaste la opción de salir')

while True:
    menu_opciones()
    opciones = int(input('Introduce una opción: '))

    if opciones == 1:
        agregar_peli()
    elif opciones == 2:
        lista_pelis()
    elif opciones == 3:
        eliminar_catalogo()
    elif opciones == 4:
        print('Saliste del menú')
        break
    else:
        print('Opción no válida. Intenta otra vez.')

