# El polimorfismo es un concepto en POO que permite
# que objetos de diferentes clases sean tratados como
# de una misma clase común. Esto se llama "duck typing"
# El comportamiento de un objeto se determina por sus métodos y propiedades

import numpy as np
import scipy.stats as stats

# Clase padre
class Distribucion:
    def calcular_probabilidad(self, x):
        raise
        NotImplementedError('Este método debe ser implementado por las subclases')

# Clase derivada por la distribución normal
class Distibucion_Normal(Distribucion):
    def __init__(self, media, desviacion_standar):
        self.media = media
        self.desviacion_standar = desviacion_standar
    
    def calcular_probabilidad(self, x):
        return stats.norm.pdf(s, self.media, self.desviacion_standar)

# Clase derivada para distribución binomial

class Distribución_Binomial(Distribucion):
    def __init__(self, n, p):
        self.n = n
        self.p = p
    
    def calcular_probabilidad(self, x):
        stats.binom.pmf(x, self.n, self.p)


# Función que usa polimorfismo
def imprimir_probabilidad(distribucion, x):
    probabilidad = distribucion.calcular_probabilidad(x)
    print(f"La probabilidad de {x} es {probabilidad}")

# Crear instancias de las distribuciones
normal = DistribucionNormal(media=0, desviacion_estandar=1)
binomial = DistribucionBinomial(n=10, p=0.5)

# Usar polimorfismo para calcular probabilidades
imprimir_probabilidad(normal, 0)  # Probabilidad en una distribución normal
imprimir_probabilidad(binomial, 5)  # Probabilidad en una distribución binomial