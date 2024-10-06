# Verificación de elementos en una tupla
mi_tupla = 3, 6, 9, 12, 15
print(mi_tupla)
primero, segundo, tercero, cuarto, quinto = mi_tupla
elemento = 6
print(elemento)
mensaje ='Está en la tupla.' if elemento in mi_tupla else 'El número no está en la tupla'
print(mensaje)