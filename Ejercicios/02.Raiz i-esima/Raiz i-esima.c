#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    float numero, i, raiz;

    do{
        scanf("%f", &numero);
        if (numero < 0){
            printf("ERROR, debe ser >= 0\n");
        } 
    } while (numero < 0);

    do{
        scanf("%f", &i);
        if (i <= 0){
            printf("ERROR, debe ser > 0\n");
        }    
    } while (i <= 0);

    raiz = pow(numero,(1/i));

    printf("%.3f", raiz);

    return EXIT_SUCCESS;
}