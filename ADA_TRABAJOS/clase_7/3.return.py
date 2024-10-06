# Definimos una función
def cal_cuadrado(numero):
    return numero * numero
resultado = cal_cuadrado(4)

print('Ejemplo básico de return: ')
print(f'El cuadrado de 4 es {resultado}')

# Ejemplo que retorne múltiples valores
def obtener_datos():
    nombre = 'Ana'
    edad = 30
    return nombre, edad # regresa los valores como tupla

# Asignamos los valores a una variable
nombre, edad = obtener_datos()
print(f'Ejemplo de múltiples valores. Nombre: {nombre}, edad: {edad}')

# La función no regresa, es decir, no retorna.
def clasifican_numero(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else: 
        return 'Cero'
resultado_1 = clasifican_numero(10)
resultado_2 = clasifican_numero(-3)

print('El ejemplo donde el return es del if')
print(f'El número 10 es {resultado_1}')
print(f'El número -3 es: {resultado_2}')

# Ejemplo sin return
def mostrar_mensaje(nombre):
    return print(mostrar_mensaje(Luis))