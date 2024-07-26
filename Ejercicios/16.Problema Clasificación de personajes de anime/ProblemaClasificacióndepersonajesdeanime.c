#include <stdio.h>
#include <stdlib.h>

struct Personaje{
    char nombre[30];
    int nivelDePoder;
    int actitud;
    int historiaPasada;
};

char clasificarPersonaje(struct Personaje *p){
    if (p->nivelDePoder > 9000 || (p->actitud == 1 && p->historiaPasada == 0)){
        return 'H';
    }else{
        return 'V';
    }
}

int main(){
    struct Personaje personajes[] = {
        {"Naruto - Naruto", 9000, 1, 0},
        {"Goku - Dragon Ball", 12000, 1, 0},
        {"Light - Death Note", 5000, -1, 1},
        {"Freezer - Dragon Ball", 8000, -1, 1},
        {"Luffy - One Piece", 7500, 1, 0},
        {"Sasuke - Naruto", 8500, -1, 1},
        {"Vegeta - Dragon Ball", 11000, -1, 0}
    };

    for (int i = 0; i < sizeof(personajes) / sizeof(personajes[0]); i++){
        printf("%s es un %s\n", personajes[i].nombre, (clasificarPersonaje(&personajes[i]) == 'H') ? "Heroe" : "Villano");
    }
    
    return EXIT_SUCCESS;
}