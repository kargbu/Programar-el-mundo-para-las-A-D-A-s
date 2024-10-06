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

# Usamos por para eliminar la clave edad y obtener su valor
valor_eliminado = persona.pop('edad: ')

# Imprimimos el valor eliminado y el diccionario resultante
print('Valo eliminado: ', valor_eliminado)
print('Diccionario después de eliminar edad: .', persona)

# Usar por con una clave que no existe y un valor por defecto
valor_inexistente = persona.pop('país', 'No especificado')
print('Valor cuando la clave no existe: ', valor_inexistente)

