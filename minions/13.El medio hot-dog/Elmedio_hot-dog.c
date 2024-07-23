#include <stdio.h>
#include <stdlib.h>

int main(){
    int N, i, t = 0;
    float deposito, total;

    do{
        scanf("%d", &N);
    } while (N <= 0);

    do{
        scanf("%f", &total);
    } while (total <= 0);
    
    for (i = 0; i < N; i++){
        scanf("%f", &deposito);
        total += deposito;

        if ((int)total / total != 1)
            t++;
        else
            total = 0;
    }
    
    printf("%d", t);

    return EXIT_SUCCESS;
}