# Definición de la clase
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonidos(self):
        return 'Sonido animal' # Método genérico que puede ser sobre escrito

# Ahora, puedes crear subclase como perro y gato que se heredan de la clase Animal

class Perro(Animal):
    def hacer_sonidos(self):
        return 'what' # Sobre escribir el método para el sonido específico de un perro
    
class Gato(Animal):
    def hacer_sonidos(self):
        return 'mierda'
    
mi_perro = Perro('Cosquilla')
mi_gato = Gato('Nous')

print(f'Mi perro ladra {mi_perro.hacer_sonidos()}')
print(f'Mi gato mauia {mi_gato.hacer_sonidos()}')
