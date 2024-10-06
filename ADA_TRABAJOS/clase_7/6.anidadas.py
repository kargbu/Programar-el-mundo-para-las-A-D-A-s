# Ejemplo de composición de funciones
def funcion_externa(x):
    def funcion_interna(y):
        return y + 10
    return funcion_interna(x) # llama a la función interna con el valor x
# llamamos a la función externa
resultado = funcion_externa(5)
print(f'Resultado de la función externa: {resultado}')