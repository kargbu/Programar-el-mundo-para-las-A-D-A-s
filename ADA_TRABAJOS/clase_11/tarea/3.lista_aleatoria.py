# Generar una lista de 10 números aleatorios entre 1 y 100
import random

def list_of_random_number():
    list_num = [random.randint(1, 100)
                for _ in range(5)]
# Nos indica que no necesitamos el valor del iterador sino que
# solo que se repita 5 veces

    print(f'La lista de números aleatorios es {list_num}')

    list_num.sort()

    print(f'La lista ordenada es: {list_num}')
# LLamar a la función
list_of_random_number()