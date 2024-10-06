# Definir la clase persona.
class Persona:
    def __init__(self, nombre, edad, color_de_cabello):
        self.nombre = nombre
        self.edad = edad
        self.color_de_cabello = color_de_cabello

 # Crear un objeto de la clase persona
persona_1 = Persona('Ana', 33, 'rojo')

# Acceder a las propiedades del objeto
print(persona_1.nombre)
print(persona_1.edad)
print(persona_1.color_de_cabello)
