# Definimos la clase de 
class Gato:
    def __init__(self, color, nombre):
        self.color = color   # Atributo color
        self.nombre = nombre # Atributo nombre
        pass
gato_1 = Gato('negro', 'Felix')
gato_2 = Gato('gris', 'Ares')

# Acceder a los atributos de instancias
print(gato_1.color)
print(gato_2.color)