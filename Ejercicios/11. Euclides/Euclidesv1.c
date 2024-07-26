#include <stdio.h>
#include <stdlib.h>

int main(){
    int final, i, m, n, maximo;

    scanf("%d", &m);
    scanf("%d", &n);

    if (n <= m){
        final = n;
    }else{
        final = m;
    }

    for (i = 1; i <= final; i += 1){
        if ((n % i == 0 && m % i == 0)){
            maximo = i;
        }  
    }
    
    printf("Maximo comun: %d\n", maximo);

    return EXIT_SUCCESS;
}