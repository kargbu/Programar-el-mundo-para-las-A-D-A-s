# Definir clase en python, es un lugar en donde vivien objetos, cuyos objetos tienen atributos y realizan actividades
class Coche:
    # El método _init_ es el que llama al constructor. Nos permite crear objetos en una clase.
    def _init_ (self, marca, modelo):
                # Self es la referencia al objeto que estamos creando.
                self.marca = marca # Es el atributo de instancia
                self.modelo = modelo