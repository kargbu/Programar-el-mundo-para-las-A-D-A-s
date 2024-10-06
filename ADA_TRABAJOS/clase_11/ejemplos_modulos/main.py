# Importamos el módulo completo

import operaciones

print(f'Suma (import completo): {operaciones}')

# Renombramos el módulo
import operaciones as op

print(f'Resta (modulo renombrado): {op.restar(5,2)}')

# Importar una función específica
from operaciones import multi

print(f'Multiplicación (función específica): {multi(3,10)}')

# Renombramos una función específica
from operaciones import sumar as sum

print(f'Suma (con una función renombrada): {sum(10,17)}')

# Importando todo el módulo con *
from operaciones import *
print(f'Resta (usando import): {restar(30,5)}')