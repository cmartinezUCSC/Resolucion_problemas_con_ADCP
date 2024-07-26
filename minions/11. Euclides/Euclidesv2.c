#include <stdio.h>
#include <stdlib.h>

int main(){
    int m, n, mod;
    scanf("%d %d", &m, &n); 

    if (m % n == 0){
        if (m < n)
            printf("%d\n", m);
        if (n < m)
            printf("%d\n", n);
    }else{
        while (m % n != 0){
            mod = m % n;
            m = n;
            n = mod;
        }
        
        printf("%d", mod);
    }

    return EXIT_SUCCESS;
}