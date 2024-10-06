# Lista de diccionarios

lista_datos = [
    {
        'Nombre' : 'Charo',
        'Edad'   : 45,
        'Calificaciones' : [5, 6, 7]

    },
    {
        'Nombre': 'Luis',
        'Edad': 30,
        'Calificaciones': [8, 9, 10]
    },
    {
        'Nombre': 'Ana',
        'Edad': 22,
        'Calificaciones': [7, 8, 9]
    },
    {
        'Nombre': 'Carlos',
        'Edad': 35,
        'Calificaciones': [6, 7, 8]
    },
    {
        'Nombre': 'María',
        'Edad': 28,
        'Calificaciones': [9, 9, 10]
    },
    {
        'Nombre': 'Jorge',
        'Edad': 40,
        'Calificaciones': [5, 6, 7]
    }
]

for persona in lista_datos:
    print(f'El nombre es {persona["Nombre"]}', f'y sus calificaciones son: {persona["Calificaciones"]}')
