# Definir la clase coche
class Coche:
    ruedas = 4 # Atributo de clase

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        pass
# Crear instancias de la clase coche
coche_1 = Coche('Toyota', 'Corola')
coche_2 = Coche('KIA', 'Niro')

# Acceder al atributo de clase de las instancias
print(coche_1.ruedas)
print(coche_2.ruedas)