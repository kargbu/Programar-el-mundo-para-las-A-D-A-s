# Método de clase

class Conejo:
    contidad_de_conejo = 0 # Atributo de clase

    def __init__(self,color, nombre):
        self.color = color
        self.nombre = nombre
        Conejo.cantidad_de_conejos += 1 # Aumenta la cantidad total de conejo
# Método de clase para obtener el total de conejos

    @classmethod
    def total_conejo(cls):
        return f'Total de conejos: {cls.cantidad_de_conejos}'
# Crear instancias de la clase Conejo
conejo_1 = Conejo('Blanco', 'Tambor')
conejo_2 = Conejo('Gris', 'Pochoclo')

# Llamar el método de clase
print(Conejo.total_conejo())