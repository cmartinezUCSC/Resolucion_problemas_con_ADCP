#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, cubo, impar, i;
    cubo = 0;

    do{
        scanf("%d", &n);
        if (n <= 0)
            printf("Ingrese un entero positivo\n");
    } while (n <= 0);

    impar = (n * (n - 1)) + 1;

    for (i = 0; i < n; i++){
        cubo += impar;
        impar += 2;
    }

    printf("el cubo es: (%d)", cubo);

    return EXIT_SUCCESS;
}