# Ejercicio 3. Rango, enumeración y break y continua

lista_cadena = ['yo', 'te', 'quiero', 'para', 'beso', 'casa', 'mandarina', 'compras', '', 'Uruguay', 'viaje', 'trabajo']

# Crear el objeto en enumerate
mostrara_in_val = enumerate(lista_cadena, 0)

# Imprimir los elementos enumerados
for indice, valor in mostrara_in_val:
   
    if valor == '':
        print(f'{indice}: encontró al vacío')

        continue

    print(f'{indice}: {valor}')

# Ejemplo de uso de break
    if indice == 5:
        print('Se ha alcanzado el índice 5, se interrumpe el bucle.')
        break

# El bloque else se ejecuta si el bucle for no se interrumpe con un break
else:
    print('El bucle for ha terminado sin interrupciones.')
