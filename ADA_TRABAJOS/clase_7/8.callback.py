# Operación básica

def suma(a,b):
    return a + b

def restar(a,b):
    return a - b

# Función que recibe otra función como callback
def operacion(a,b,funcion_callback):
    resultado = funcion_callback(a,b)
    print(f'Resultado de la operación: {resultado}')

# Uso de la función 
print('Ejemplo de callback simple')
operacion(5, 3, suma)
operacion(5, 3, restar)