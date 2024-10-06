# Calificación con operador ternario

# Realiza un programa que asigne a una variable (llamada resultado) con base en una calificación (entre 0 y 100). Usa el operador ternario para asignar "Aprobado" si la calificación es mayor o igual a 60 y "Reprobado" en caso contrario.

Cal_1 = int(input('Ingresa la primera calificación '))
Cal_2 = int(input('Ingresa la segunda calificación '))
Cal_3 = int(input('Ingresa la tercera calificación '))

Prom = (Cal_1 + Cal_2 + Cal_3)// 3

mensaje = 'Aprobado' if Prom >= 6 else 'Reprobado'

print(mensaje)