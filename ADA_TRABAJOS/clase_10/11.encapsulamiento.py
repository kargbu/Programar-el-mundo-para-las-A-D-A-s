# En Python no hay un encapsulamiento como tal
# Se simula con dobles guines bajos __, al inicio
# del nombre de un atributo o método para iniciar 
# que son privados

class Ejemplo:
    def __init__(self, valor):
        self.__atributo_privado = valor
        # Este es un atributo privados
       
    def __metodo_privado(self):
         print(f'Este es el método privado')
    # Este es un método privado

    def metodo_publico(self):
        print(f'Este es un método público')

        self.__metodo_privado()
    # Llamando al método privado desde dentro de la clase
obj = Ejemplo('Puto')
    # print(obj.__atributo_privado)
    # Esto arrojará un Error

obj.metodo_publico()
    # Esto llamará al método privado internamente