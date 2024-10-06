# Contar ocurrencias de un diccionario anidado
# De la lista de películas

catalogo_peliculas = [
    {
        'Número': 1,
        'Título': 'Inception',
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
        'Título': 'The Matrix',
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
        'Título': 'Interstellar',
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
        'Título': 'The Godfather',
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
        'Título': 'Pulp Fiction',
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
        'Título': 'The Dark Knight',
        'Año': 2008,
        'Plataforma': 'HBO Max',
        'Artistas Principales': [
            {'Nombre': 'Christian Bale', 'En Catálogo': True},
            {'Nombre': 'Heath Ledger', 'En Catálogo': True},
            {'Nombre': 'Aaron Eckhart', 'En Catálogo': True}
        ]
    }
]

contador_HBO_max = 0

for peli in catalogo_peliculas:
    print(f'\nLos artistas de la película {peli["Título"]}\n')
    for artista in peli['Artistas Principales']:
        print(f'   - {artista["Nombre"]}')
    print(f'\n Se encuentra en {peli["Plataforma"]}')
    if peli["Plataforma"] == 'HBO Max':
        contador_HBO_max += 1
    print(f'Número de películas en HBO Max: {contador_HBO_max}')