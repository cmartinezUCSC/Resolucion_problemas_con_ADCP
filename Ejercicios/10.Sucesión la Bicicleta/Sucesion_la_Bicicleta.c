#include <stdio.h>
#include <stdlib.h>

int main(){
    float b0 = 2, b1 = 3, bn;
    int i, n;

    do{
        scanf("%d", &n);
        if (n < 3){
            printf("Error, debe ser >=3\n");
        }   
    } while (n < 3);

    printf("%3.1f\n%3.1f\n", b0, b1);

    for (i = 1; i <= n - 2; i += 1){
        bn = (b1 + 1) / b0;
        printf("%3.1f\n", bn);

        b0 = b1;
        b1 = bn;
    }

    return EXIT_SUCCESS;
}