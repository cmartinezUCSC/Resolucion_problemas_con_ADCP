#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, j, k, m, S1 = 0, S2 = 0;
    do{
        scanf("%d", &m);
    } while (m <= 0);

    for (k = 1; k <= m; k++){
        S1 = 0;
        for (i = 0; i < k; i++){
            S2 = 0;
            if (k % i == 0){
                S1 = S2 + i;
            }

            for (j = 1; j < i; j++){
                if (i % j == 0){
                    S2 = S2 + j;
                }    
            }
            
            printf("\ni=%d\tk=%d\tS1=%d\tS2=%d", i, k, S1, S2);

            if ((S1 == i) && (S2 == k)){
                printf("\nlos numeros %d y %d son numeros amigos", i, k);
                getchar();
            }   
        }  
    }   

    return EXIT_SUCCESS;
}
// no corre