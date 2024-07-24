#include <stdio.h>
#include <stdlib.h>

int main(){
    int T;
    scanf("%d", &T);

    for (int j = 0; j < T; j++){
        int n, c;
        scanf("%d %d", &n, &c);

        int C_uso = c;
        int baldes = 1;

        int Cn[n];
        for (int i = 0; i < n; i++){
            scanf("%d", &Cn[i]);
        }

        for (int i = 0; i < n; i++){
            C_uso -= Cn[i];
            if (C_uso <= 0){
                baldes++;
                C_uso = c;
            }   
        }
        
        printf("%d\n", baldes);
    }

    return EXIT_SUCCESS;
}