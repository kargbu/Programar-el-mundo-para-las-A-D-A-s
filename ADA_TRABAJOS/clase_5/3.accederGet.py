# Crear un diccionario
persona = {
    'nombre' : 'Veronica',
    'edad' : 25,
    'ciudad' : 'Buenos Aires'
}

# Usar el método .get para acceder a los elementos
nombre = persona.get('nombre')
edad = persona.get('edad')
ciudad = persona.get('ciudad')

# Imprimir
print('Nombre: ', nombre)
print('Edad: ', edad)
print('Ciudad: ', ciudad)

# Intentar acceder a una clave que no existe usando el método .get
pais = persona.get('país')
print('País: ', pais)

# Usar .get con un valor determinado si la clave no existe
pais_con_valor_predeterminado = persona.get('país', 'No especificado')
print('País: ', pais_con_valor_predeterminado)