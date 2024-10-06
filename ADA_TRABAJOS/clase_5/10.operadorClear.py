# Crear un diccionario
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

# Imprimimos el diccionario original
print('Diccionario original: ', persona)


# Usamos el método clear
persona.clear()
print('Diccionario después del método clear: ', persona)