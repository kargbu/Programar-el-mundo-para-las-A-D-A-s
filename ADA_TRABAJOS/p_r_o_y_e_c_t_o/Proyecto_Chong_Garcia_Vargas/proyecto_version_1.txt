import random

def juego_trivia():

    def bienvenida():
        print('\n¡Te doy la bienvenida al juego de L A   T R I V I A  D E   P Y T H O N!')

    def datos():
        nombre = input('\nIngresa tu nombre, por favor: ')
        edad = int(input('\nIngresa tu edad, por favor: '))
        if edad >= 18:
            print(f'\n¡Hola, {nombre}!\nEres mayor de edad. Es hora de comenzar con la trivia.\n')
        else:
            print(f'\nLo siento {nombre}, no tienes la edad mínima para jugar. \n')
            exit()
        return nombre, edad

    def instrucciones():
        print('\nAntes de comenzar, las instrucciones del juego son las siguientes: debes contestar correctamente las preguntas. '
              'Por cada respuesta correcta ganarás 1 punto. Sin embargo, por cada respuesta incorrecta no sumarás puntos, '
              'pero si te equivocas más de tres veces, pierdes el juego.\n¡Ahora sí, a jugar!')

    def preguntas_y_respuestas():
        preguntas = {
            'Pregunta 1': 'verdadero',
            'Pregunta 2': 'verdadero',
            'Pregunta 3': 'verdadero'
        }
        lista_preguntas = list(preguntas.items())
        random.shuffle(lista_preguntas)
        return lista_preguntas

    def jugar(lista_preguntas):
        score = 0
        errores = 0

        for preguntaX, respuesta_correcta in lista_preguntas:
            respuesta_usuario = input(f'{preguntaX} (Responde verdadero o falso): ').lower()

            if (respuesta_usuario == 'verdadero' and respuesta_correcta == 'verdadero') or (respuesta_usuario == 'falso' and respuesta_correcta == 'falso'):
                print('Es correcto')
                score += 1
            else:
                print('Es incorrecto')
                errores += 1

            print(f'Tu puntuación es de {score}')
            if errores == 3:
                print('Fallaste tres veces. Final del juego.')
                break

        if errores < 3:
            print(f'Puntuación final: {score}/{len(lista_preguntas)}')

    bienvenida()
    datos()
    instrucciones()
    lista_preguntas = preguntas_y_respuestas()
    jugar(lista_preguntas)

juego_trivia()
