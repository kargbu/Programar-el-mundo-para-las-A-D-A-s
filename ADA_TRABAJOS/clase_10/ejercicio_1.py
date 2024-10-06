# Crea una clase Estudiante con atributos como nombre, edad, y
# notas. Implementa métodos para calcular el promedio de notas
# y determinar si el estudiante ha aprobado o no. Agrega una
# clase Curso que contenga una lista de estudiantes y un método
# para mostrar todos los estudiantes aprobados.

class Estudiante:
    def __init__(self,nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
        pass
lista_estudiantes = [
Estudiante('Francisco', 16, [1,10,2,9]),
Estudiante('Ana', 17, [2,9,3,8]),
Estudiante('Karina', 18, [3,8,4,7]),
Estudiante('Camilo', 17, [4,6,5,10]),
]

# Método para sumar las notas
def calcular_suma(notas):
    return sum(notas)
def calcula_prom(notas):
    suma = calcular_suma(notas)
    return suma / len(notas)
class Curso:
    def __init__(self):
        self.aprobados = []
        pass
    def agregar_aprobado(self, nombre, promedio):
            
        if promedio >= 6:
                self.aprobados.append(estudiante.nombre)

    def mostrar_lista(self):
            print(f'Los estudiantes que aprobaron son: {", ".join(self.aprobados)}')

curso = Curso()

for estudiante in lista_estudiantes:
#   suma_notas = calcular_suma(estudiante.notas) Calcula la suma de las notas. NO sirve para el cálculo del promedio.
    promedios = calcula_prom(estudiante.notas)

    print(f'El promedio de {estudiante.nombre} es de {promedios}')

curso.agregar_aprobado(estudiante.nombre, promedios)
curso.mostrar_lista()