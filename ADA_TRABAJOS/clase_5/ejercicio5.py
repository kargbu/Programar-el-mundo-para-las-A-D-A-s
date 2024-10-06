# Diccionarios dentro de una lista
# Crea una lista de diccionarios
productos = [
    {
        'Nombre': 'Inception',
        'Precio': 12.99,
        'Cantidad en stock': 10
    },
    {
        'Nombre': 'The Matrix',
        'Precio': 9.99,
        'Cantidad en stock': 5
    },
    {
        'Nombre': 'Interstellar',
        'Precio': 14.99,
        'Cantidad en stock': 7
    },
    {
        'Nombre': 'The Godfather',
        'Precio': 19.99,
        'Cantidad en stock': 3
    },
    {
        'Nombre': 'Pulp Fiction',
        'Precio': 11.99,
        'Cantidad en stock': 8
    },
    {
        'Nombre': 'The Dark Knight',
        'Precio': 13.99,
        'Cantidad en stock': 6
    }
]

# Imprimir el nombre y el precio del segundo producto en la lista
segundo_producto = productos[1]
print(f'Nombre: {segundo_producto["Nombre"]}, Precio: {segundo_producto["Precio"]}')
