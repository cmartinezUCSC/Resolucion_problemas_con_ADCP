#include <stdio.h>
#include <stdlib.h>

int main(){
    int a,b,c,medio;

    do{
        printf("Edades de los 3 hermanos? (cada una separada por un espacio)\n");
        scanf("%d %d %d",&a,&b,&c);
    } while (a<=0 || b<=0 || c<=0);

    if ((b<a && a<c) || (c<a && a<b)){
        medio = a;
    }else{
        if ((a<b && b<c) || (c<b && b<a)){
            medio = b;
        }else{
            if ((a<c && c<b) || (b<c && c<a)){
                medio = c;
            }
        }  
    }

    printf("el hijo del medio es : %i\n",medio);

    return EXIT_SUCCESS;
}