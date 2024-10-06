# Manejo de matrículas en la tupla
matricula = 101, 102, 103, 104, 105

cuantas_veces = matricula.count(102)
print('La matrícula 102 aparece', cuantas_veces, 'vez en la tupla')

posicion_matricula = matricula.index(104)
print(f'La matrícula 104 está en la posición {posicion_matricula} de la tupla.')