#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, n, t0=0;
    int t1=1, tn;

    do{
        printf("Ingrese n:");
        scanf("%d",&n);
        if (n<0){
            printf("Error, debe ser>=0\n");
        }
    } while (n<0);

    if (n==0){
        printf("t0=%d\n",t0);
    }else{
        printf("t0=%d\n",t0);
        printf("t1=%d\n",t1);
        for (i=2; i<=n; i+=1){
            tn = t0+t1;
            t0 = t1;
            t1 = tn;
            printf("t%d=%d\n",i,tn);
        } 
    }

    return EXIT_SUCCESS;
}