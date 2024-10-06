# Categoría de edad con operadores lógicos

# Escribe un programa que clasifique a una persona en una categoría según su edad. Usa un condicional ir tradicional con operadores lógicos (and, or o not) para las categorías, niños, adolescentes, adultos y adultos mayores.

persona = int(input('Ingresa tu edad '))

if 0 <= persona <= 12:
    print('Eres un niño')
elif 13 <= persona <= 19:
    print('Eres un adolescente')
elif 20 <= persona <= 64:
    print('Eres un adulto joven')
elif persona >= 65:
    print('Eres un adulto mayor')
