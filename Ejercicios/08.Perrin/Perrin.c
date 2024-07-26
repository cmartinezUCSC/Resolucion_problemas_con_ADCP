#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, i, p0=3, p1=0, p2=2, perrin;
    do{
        printf("Ingrese n:");
        scanf("%d",&n);
        if (n < 0)
            printf("Error debe ser >=0"); 
    } while (n < 0);

    if (n == 0)
        printf("(%d)", p0);
    else if (n == 1)
        printf("(%d)", p1);
    else if (n == 2)
        printf("(%d)", p2);
    else{
        if (n == 2)
            printf("(%d)", p2);
        
        for (i = 3; i <= n; i++){
            perrin = p1 + p0;

            p0 = p1;
            p1 = p2;
            p2 = perrin;
        }
        
        printf("(%d)", perrin);  
    }

    return EXIT_SUCCESS;
}