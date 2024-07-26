#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, i, resultado;
    resultado = 0;
    scanf("%d", &n);

    if (n < 1){
        printf("Error, debe ser >= 1");
    }else{
        for ( i = 0; i <= n; i++){
            resultado += i;
        }
        printf("%d", resultado);
    }

    return EXIT_SUCCESS;
}