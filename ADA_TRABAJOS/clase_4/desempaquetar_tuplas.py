# Ejemplo, desempaquetado básico
# Crear una tupla con varios tipos de datos

mi_tupla = 1, 'Python', 3.1416
# Desempaquetar la tupla
numero, lenguaje, pi = mi_tupla
# Mostrar el valor de cada variable después del desempaquetado
print('Número: ', numero)
print('Lenguaje: ', lenguaje)
print('Pi: ', pi)

# Ejemplo 2: Número de variables que no son iguales a la original
# Crea una tupla con tres elementos

mi_tupla_2 = 1, 'Python', 3.1416, 'te amo'
numero,lenguaje, Pi, estado = mi_tupla_2
print('Estado emocional: ', estado)

# Ejemplo 3, desempaquetado con el operador *
# Crear una tupla con varios elementos

mi_tupla_3 = 1, 'Python', 3.1416, 'te amo'
# Desempaquetar la tupla con el operador *
primer_elemento, *resto = mi_tupla
print('\nPrimer elemento: ', primer_elemento)
print('Resto de los elemento: ', mi_tupla)