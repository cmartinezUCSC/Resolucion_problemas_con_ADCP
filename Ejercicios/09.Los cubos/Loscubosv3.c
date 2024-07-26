#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, i, suma, cubo;

    do{
        scanf("%d", &n);
        if (n <= 0)
            printf("Ingrese un entero positivo\n");
    } while (n <= 0);

    suma = (n * (n + 1)) / 2;
    cubo = 0;

    for (i = (((suma - 1) * 2) + 1); i >= ((suma - n)) * 2 + 1; i -= 2)
        cubo += i;
    printf("(%d)", cubo);

    return EXIT_SUCCESS;
}