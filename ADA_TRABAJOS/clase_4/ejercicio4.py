# Manipulación de tuplas y comprobbación de índices

frutas = 'manzana', 'banana', 'cereza'
posición_cereza = frutas.index('cereza')
print('La posición de la cereza  en la tupla es', posición_cereza)

fruta = input('Escribe una fruta en minúsculas ')
mensaje = f'La fruta {fruta} está en la tupla' if fruta in frutas else f'La fruta {fruta} no está en la tupla'
print(mensaje)

