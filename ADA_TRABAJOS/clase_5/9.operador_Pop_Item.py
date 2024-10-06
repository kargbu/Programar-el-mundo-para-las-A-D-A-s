# Crear un diccionari
persona = {
    'nombre: ': 'Francisco',
    'edad: ': 62,
    'casado: ': False,
    'hijos: ': False,
    'dirección: ': { # la clave es un string y el valor es un diccionario
        'calle: ': 'Calle Manuel Márquez Sterling',
        'número: ': 34,
        'interior: ': 807,
        'ciudad: ': 'Ciudad de México'
    }
}

# Imprimir el diccionario original
print('Diccionario original: ', persona)

# Usamos popItem para eliminar y obtener el último par clave-valor
ultimo_elemento = persona.popitem()

# Imprimimos el par clave-valor
print('Último par clave-valor eliminado: ', ultimo_elemento)

# Imprimimos después de usar popItem
print('Diccionario después de usar popItem: ', persona)