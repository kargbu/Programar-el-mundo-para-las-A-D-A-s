# Anidación básica de diccionario
# Crea un diccionario que represente una persona con las siguientes claves

persona_1 = {
    'Nombre'    : 'El innombrable',
    'Edad'      : '40',
    'Dirección' : {
        'Calle'         : 'José Rocabruna 79',
        'Departamento'  : '404',
        'Colonia'       : 'Copilco el Alto',
        'Delegación'    : 'Coyoacán',
        'Código Postal' : '04360'
     },
    'Ciudad'   : 'CDMX'
}


print(f'El innombrable está en la ciudad de: {persona_1["Ciudad"]}')