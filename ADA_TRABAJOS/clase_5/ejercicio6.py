# Anidación compleja de diccionarios y listas
# Crea un diccionario que contenga información sobre una plataforma de películas
# Lista de diccionarios
productos = [
    {
        'Número': 1,
        'Nombre': 'Inception',
        'Año': 2010,
        'Plataforma': 'HBO Max',
        'Artistas Principales': [
            {'Nombre': 'Leonardo DiCaprio', 'En Catálogo': True},
            {'Nombre': 'Joseph Gordon-Levitt', 'En Catálogo': True},
            {'Nombre': 'Elliot Page', 'En Catálogo': True}
        ]
    },
    {
        'Número': 2,
        'Nombre': 'The Matrix',
        'Año': 1999,
        'Plataforma': 'Netflix',
        'Artistas Principales': [
            {'Nombre': 'Keanu Reeves', 'En Catálogo': True},
            {'Nombre': 'Laurence Fishburne', 'En Catálogo': True},
            {'Nombre': 'Carrie-Anne Moss', 'En Catálogo': True}
        ]
    },
    {
        'Número': 3,
        'Nombre': 'Interstellar',
        'Año': 2014,
        'Plataforma': 'Amazon Prime Video',
        'Artistas Principales': [
            {'Nombre': 'Matthew McConaughey', 'En Catálogo': True},
            {'Nombre': 'Anne Hathaway', 'En Catálogo': True},
            {'Nombre': 'Jessica Chastain', 'En Catálogo': True}
        ]
    },
    {
        'Número': 4,
        'Nombre': 'The Godfather',
        'Año': 1972,
        'Plataforma': 'Paramount+',
        'Artistas Principales': [
            {'Nombre': 'Marlon Brando', 'En Catálogo': True},
            {'Nombre': 'Al Pacino', 'En Catálogo': True},
            {'Nombre': 'James Caan', 'En Catálogo': True}
        ]
    },
    {
        'Número': 5,
        'Nombre': 'Pulp Fiction',
        'Año': 1994,
        'Plataforma': 'Hulu',
        'Artistas Principales': [
            {'Nombre': 'John Travolta', 'En Catálogo': True},
            {'Nombre': 'Uma Thurman', 'En Catálogo': True},
            {'Nombre': 'Samuel L. Jackson', 'En Catálogo': True}
        ]
    },
    {
        'Número': 6,
        'Nombre': 'The Dark Knight',
        'Año': 2008,
        'Plataforma': 'HBO Max',
        'Artistas Principales': [
            {'Nombre': 'Christian Bale', 'En Catálogo': True},
            {'Nombre': 'Heath Ledger', 'En Catálogo': True},
            {'Nombre': 'Aaron Eckhart', 'En Catálogo': True}
        ]
    }
]

# Imprimir el nombre y el año de estreno del segundo producto en la lista
# Imprimir los nombres de los artistas principales de la primera película

primera_pelicula = productos[0]

print(f'Artistas principales de {primera_pelicula["Nombre"]}:')

for artista in primera_pelicula['Artistas Principales']:
    print(artista['Nombre'])
