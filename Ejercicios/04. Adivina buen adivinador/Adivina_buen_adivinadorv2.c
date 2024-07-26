#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    int numero,leido,intentos,acierto;
    srand(time(NULL));
    numero = rand()%100 + 1;
    intentos=10;
    acierto=0;

    do{
        do{
            printf("Ingresa un numero\n");
            scanf("%d",&leido);

            if (leido>100 || leido<1)printf("El numero no esta en el rango del juego");

        } while (leido>100 || leido<1);

        if (numero<leido)printf("El numero a adivinar menor que el ingresaste\n");
        if (numero>leido)printf("El numero a adivinar es mayor que el que ingresaste\n"); 
        if (leido==numero) acierto=1;
        intentos--;
        
    } while (acierto==0 && intentos>0); system("cls");

    if(acierto==1)printf("Felicidades, has adivinado en (%d) intentos!!.\nEl numero es el (%d)",10-intentos,numero);
    else printf("Lo siento, has fallado. El numero generado al azar es el (%d)",numero);
    system("pause");

    return EXIT_SUCCESS;
}