# Ejercicio 2. Desarrolla un programa que haga lo siguiente

num = []
# Inicia una lista para guardar los número

while True:
    ingresa_num = int(input(f'\nIngresa un número entero '))

    if ingresa_num == 0:
        print('El 0 no suma')
        break
    else:
       num.append(ingresa_num)


# Calcula la suma de los números ingresados
resultado = 0
for e in num:
    resultado += e

# resultado = sum(num)
print(f'La suma de los números ingresados es {resultado}')
       