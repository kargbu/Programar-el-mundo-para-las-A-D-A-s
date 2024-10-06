# Este programa es un juego de Trivia sobre programación en Python.
# Integrantes: Karina García, Catalina Vargas, Melani Chong

# Paso 4 Modulo random
import random

# Paso 8 Creación de funciones
def juego_trivia():

    def bienvenida ():
        print('\n¡Te doy la bienvenida al juego de L A   T R I V I A  D E   P Y T H O N!')
        
# Paso 3 Estructura básica del juego
    # 3.1 Nombre del usuario

    def datos ():
        nombre = input('\nIngresa tu nombre, por favor: ')

    # 3.2 Edad del usuario

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

# Paso 5 preguntas y respuestas

    # 5.1 Definir las preguntas y sus respuestas en un diccionario
    def preguntas_y_respuestas():
        preguntas = {
        '¿Un algoritmo es un conjunto de instrucciones secuenciales que permiten la resolución de un problema?': 'verdadero',
        'Son ejemplos de lenguajes interpretados: Ruby, JavaScript y Python': 'verdadero',
        'Un lenguaje de programación es un conjunto de reglas, sintaxis y semántica que permite a los programadores escribir instrucciones que una computadora puede entender y ejecutar': 'verdadero',               
        'JavaScript fue creado por Guido van Rossum a finales de los años 80': 'falso',
        'Los diccionarios son una variable que permite almacenar varios datos inmutables (no se pueden modificar una vez creados) de tipos diferentes': 'falso',
        'Las  listas permite modificar los datos una vez creados, es decir no son inmutables': 'verdadero',
        'Permite utilizar una clave para declarar y acceder a un valor, además permite modificar los valores: ¿hablamos de los diccionarios?': 'verdadero',
        'En el ámbito de la informática, la identación cumple una función similar a la de la sangría en la escritura formal del lenguaje humano.': 'verdadero',
        '¿La identación es obligatoria en Python?': 'verdadero',
        'Se encarga de ejecutar una misma acción “mientras que” una determinada condición se cumpla. ¿Lo anterior corresponde al bucle for?': 'falso',
        '¿El bucle for permite iterar sobre una variable compleja del tipo lista o tupla?': 'verdadero'} 

    # 5.2 Convertir en tuplas

        lista_preguntas = list(preguntas.items())

    # 5.3 Usar shuffle para mezclar las preguntas 

        random.shuffle(lista_preguntas)
        return lista_preguntas

# Paso 6 y 7 Mostrar la preguntar y evaluar la respuesta
    # Contador de puntuación
    def jugar(lista_preguntas):
        score = 0

    # Contador de intentos fallidos
        errores = 0

    # 1.6 Ciclo para mostar preguntas
        for preguntaX, respuesta_correcta in lista_preguntas:     #Ciclo for para que me muestre las preguntas de manera aleatoria
            respuesta_usuario = input(f'{preguntaX} (Responde verdadero o falso): ').lower()

# Validar respuestas
            if (respuesta_usuario == 'verdadero' and respuesta_correcta) or (respuesta_usuario == 'falso' and not respuesta_correcta):
                print('Es correcto')
                score += 1
            else:
                print('Es incorrecto')
                errores += 1
                print(f'Tu puntuación es de {score}')

    # 6.2 Contar y controlar los intentos fallidos
            if errores <= 3:
                print(f'Puntuación final: {score}/{len(lista_preguntas)}')

# Paso 7 Controlar errores consecutivos
        while errores == 3:
            print(f'Fallaste tres veces. Final del juego.')
        # Mostrar mensaje final
            print('\n¡Gracias por jugar esta trivia sobre Python, bonito día!')
            break

    bienvenida()
    datos()
    instrucciones()
    lista_preguntas = preguntas_y_respuestas()
    jugar(lista_preguntas)

juego_trivia()
