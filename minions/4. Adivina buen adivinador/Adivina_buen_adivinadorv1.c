#include <stdio.h>
#include <stdlib.h>

int main(){
    int numero,leido;
    srand(time(NULL));
    numero = rand()%100+1;
    do{
        printf("Ingresa un numero");
        scanf("%d",&leido);

        if (numero<leido)printf("El numero a adivinar menor que el ingresaste\n");
        if (numero>leido)printf("El numero a adivinar es mayor que el que ingresaste\n");   
  
    } while (leido!=numero);
    
    printf("Felicidades, has adivinado!! ");

    return EXIT_SUCCESS;
}
// falta una libreria, time.h
