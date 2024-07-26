#include <stdio.h>
#include <stdlib.h>

int main(){
    int suma, i, n, m;
    suma = 0;

    do{
        printf("Ingrese un numero mayor a 0\n");
        scanf("%i", &m);
        if (m <= 0){
            printf("Error, debe ser >0\n");
        }   
    } while (m <= 0);

    do{
        printf("Ingrese un numero mayor a 0\n");
        scanf("%i", &n);
        if (n <= 0){
            printf("Error, debe ser >0\n");
        }
    } while (n <= 0);  
     
    for (i = 0; i < n; i++){
        suma = suma + m;
    }

    printf("%i x %i = %i\n", m, n, suma);

    return EXIT_SUCCESS;
}