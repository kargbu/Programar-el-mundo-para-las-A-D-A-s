# Solicitar al usuario que ingrese un número
# Para calcular lo que se escribe
import math

number_requested = int(input(f'\nIngresa un número natural para calcular su entero mayor que,\n'
                                '\n su entero menor que, su raíz cuadrada, el factorial\n'
                                '\n y elevar el número tipiado a la quinta potencia\n'))
mayor_entero = math.ceil(number_requested)
print(f'El mayor entero de {number_requested} es {mayor_entero}')

menor_entero = math.floor(number_requested)
print(f'El menor entero de {number_requested} es {menor_entero}')

raiz_cuadrada = math.sqrt(number_requested)
print(f'La raíz cuadara de {number_requested} es {raiz_cuadrada}')

el_factorial = math.factorial(number_requested)
print(f'El factorial de {number_requested} es {el_factorial}')

quinta_potencia = math.pow(number_requested, 5)
print(f'La quinta potencia de {number_requested} es {quinta_potencia}')

