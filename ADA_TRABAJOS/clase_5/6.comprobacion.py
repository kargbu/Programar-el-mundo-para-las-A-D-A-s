# Crear un diccionario
persona = {
    'nombre' : 'Emilia',
    'edad' : 33,
    'ciudad' : 'Caba'
}

# Comprobar si una clave existe en el diccionario antes de acceder a su valor
clave = 'edad'

if clave in persona:
    valor = persona[clave]
    print(f'El valor de {clave} es: {valor}')
else:
    print(f'La clave {clave} no existe en el diccionario. ')

# Intentar acceder a una clave que no existe
clave_inexistente = 'país'
if clave_inexistente in persona:
    valor = persona[clave_inexistente]
    print(f'El valor de {clave_inexistente} no existe en el diccionari. ')
else:
    print(f'La clave {clave_inexistente} no existe en el diccionario.')

# Otra manera de comprobar
persona_2 = {
    'nombre: ' : 'Karina',
    'edad: ' : 33,
    'ciudad: ' : 'CABA'
}
print('nombre' in persona_2)