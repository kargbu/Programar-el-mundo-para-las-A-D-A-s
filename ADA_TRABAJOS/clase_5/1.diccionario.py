# Ejemplo de diccionario
diccionario_vacio = {}
print('Ejemplo de un diccionario vacio: ', diccionario_vacio)

# Ejemplo básico de un diccionario
persona = {
    'nombre: ': 'Francisco',
    'edad: ': 62,
    'casado: ': False,
    'hijos: ': False,
    'dirección: ': { # la clave es un string y el valor es un diccionario
        'calle: ': 'Calle Manuel Márquez Sterling',
        'número: ': 34,
        'interior: ': 807,
        'ciudad: ': 'CDMX'
    }
}
print('Ejemplo de un diccionario básico: ', persona)

# Ejemplo de diccionario con valores de distintos tipos
diccionario_mixto = {
    'nombre: ' : 'Karina',
    1 : [2, 3, 4, 5], # La clave es un entero y el valor es un string
}
print('Ejemplo de un diccionario mixto. ', diccionario_mixto)

