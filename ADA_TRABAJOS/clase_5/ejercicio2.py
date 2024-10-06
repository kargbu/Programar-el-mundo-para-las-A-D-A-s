# Modificar y eliminar elementos de un diccionario
# Ejercicio 1. Crear y acceder a un diccionario básico
# Referencia de Data Género

libro_1 = {
                
        'Título': 'Feminismos de Datos',
        'Autor' : 'D\'Ignazio C. y Klein L.',
        'Año'   : 2023,
        'Género': 'Ciencia, Filosofía'
}

# Modificar el valor de una clave
libro_1['Año'] = 2024

# Verificar el cambio
print(libro_1)


# Eliminar la clave 'Género' usando del
del libro_1['Género']

print(libro_1)