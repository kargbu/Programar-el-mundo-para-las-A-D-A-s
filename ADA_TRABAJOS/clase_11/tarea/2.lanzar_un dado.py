# Generador de números aleatorios
# El objetivo es simular el lanzamiento de un dado y generar una lista de número aleatorios
import random

def lanzar_dado():
    results = []
    for _ in range(5):
        results.append(random.randint(1, 6))
    return results

while True:
    entrada = input('\nTeclea Enter para simular el lanzamiento de un dado, cinco veces.\n'
                    '\nDe lo contrario tipea salir:\n ')
    if entrada.lower() == 'salir':
        break
    results = lanzar_dado()
    print(f'El resultado de lanzar un dado es {results}')

    def select_num_results():
        random.shuffle(results)
        num = random.choice(results)
        print(f'El número seleccionado de la lista es: {num}')
    select_num_results()
