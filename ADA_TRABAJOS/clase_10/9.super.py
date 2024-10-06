# Definición de clase
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__ (self, raza):
        self.raza = raza

mi_perro = Perro('Perro', 'callejero')

print(f'Mi perro se llama {mi_perro.nombre}\n')
print(f'\nPerro es de raza {mi_perro.raza}')