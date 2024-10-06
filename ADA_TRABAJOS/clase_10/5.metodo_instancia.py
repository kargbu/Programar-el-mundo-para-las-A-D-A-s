# Método instancia

class Perro:
    def __init__(self, raza, nombre):
        self.raza = raza
        self.nombre = nombre
        pass
# Método para mostrar información del perro
    def mostrar_info(self):
        return f'Perro: {self.raza} {self.nombre}'
# Crear un objeto de la clase perro
mi_perro = Perro('Labrador','Cosquilla')
tu_perro = Perro('Chihuahua', 'Loquita')
# Usar el método del objeto
print(mi_perro.mostrar_info())
print(tu_perro.mostrar_info())

# En la clase Perro, el método mostrar info es un método de instancia que proporciona una representación de la información.
