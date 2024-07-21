class Personaje:
    def __init__(self, nombre, nivel_de_poder, actitud, historia_pasada):
        
        self.nombre = nombre
        self.nivel_de_poder = nivel_de_poder
        self.actitud = actitud
        self.historia_pasada = historia_pasada 

def clasificar_personajes(personaje):
    
    if personaje.nivel_de_poder > 9000 or (personaje.actitud == 1 and personaje.historia_pasada == 0):
        return 'H'
    else:
        return 'V'
    

personajes = [ 
    Personaje ("Naruto", 9000, 1, 0),
    Personaje("Goku", 12000, 1, 0),
    Personaje("Light", 5000, -1, 1),
    Personaje("Freeza", 8000, -1, 1),
    Personaje("Luffy", 7500, 1, 0),
    Personaje("Sasuke", 8500, -1, 1),
    Personaje("Vegeta", 11000, -1, 0)
]

for personaje in personajes:
    print (f"{personaje.nombre}es un {'Heroe' if clasificar_personajes(personaje)== 'H' else 'Villano'}")