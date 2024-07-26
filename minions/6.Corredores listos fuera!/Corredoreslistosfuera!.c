#include <stdio.h>
#include <stdlib.h>

int main(){
    int minutos,segundos,tiempo;
    float velocidad;

    do{
        do
        {
            printf("Ingrese tiempos en mm ss: ");
            scanf("%d %d",&minutos,&segundos);
            if(minutos<0 || segundos<0) printf("\nha ingresado un valor invalido, debe ser >=0. Reintente!\n ");
        } while (minutos<0 || segundos<0);
        
        if (segundos!=0 || minutos!=0){
            tiempo=segundos+(minutos*60);
            velocidad=1500/(float)tiempo;
            printf("La velocidad promedio es de: %.2f m/s\n",velocidad);
        }    
        
    } while (minutos!=0 || segundos!=0);   

    return EXIT_SUCCESS;
}