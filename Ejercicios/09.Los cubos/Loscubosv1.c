#include <stdio.h>
#include <stdlib.h>

int main(){

    int n, superior, inferior, i, impar, cubo;
    do{
        scanf("%d", &n);
        if (n <= 0)
            printf("Ingrese un entero positivo\n");
    } while (n <= 0);

    impar = 1;
    superior = (n * (n + 1)) / 2;
    inferior = (superior - n);

    printf("cota inferior es: %d\n", inferior);
    printf("cota superior es: %d\n", superior);

    for (i = 0; i < inferior; i++){
        impar += 2;
    }
    cubo = 0;
    for (i = 0; i < n; i++){
        cubo += impar;
        impar += 2;
    }

    printf("%d al cubo es %d", n, cubo);

    return EXIT_SUCCESS;
}