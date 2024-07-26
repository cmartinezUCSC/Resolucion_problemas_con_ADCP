# 15.Amigos

#### Dificultad: fácil

## Descripcion

*Dos números son amigos, si cada uno de ellos es igual a la suma de los divisores del otro (sin incluir al mismo número en la suma).
Por ejemplo, 220 y 284 son amigos, ya que:*

Suma de divisores de 220:  1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
Suma de divisores de 284:  1 + 2 + 4 + 71 + 142 = 220

*Implemente un algoritmo que permita obtener las parejas de números amigos menores o iguales a **m**, siendo **m** un número ingresado por teclado.*

# ADCP

## (A)nalisis

###### Entradas: 
Cota superior (m)


###### Proceso mental:

¿Cómo se obtiene el divisor de un número?, si (K MOD  i = 0 )  con i=5, n  significa que k es divisible por 5  
¿Cómo se obtienen números amigos k, i? si suma divisores de k = suma divisores de i con k ≤ m e i<k

Recuerde que: (a MOD b) es el resto de la división entera entre a y b, también conocido como operador módulo.

Ahora bien, ¿cómo generar números entre 1 y m?

Para k=1, m hacer //generará números de [1..m]
            
Para i=1 hasta k-1 hacer //Generará números entre [1..k-1]
Y aplicando la regla de divisores
    
Si (k MOD i=0) Entonces
S1 <- S1+i; //acumulará a los divisores de k
FinSi

###### Salida: 
números amigos (i,k)

###### Restricciones: 
m >0

# (D)iseño 

## En Diagrama N-S

![](Imagen.png)

# (C)odificación C:
```c
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
```
# (C)odificación en Python
```py
def main():
    i = 0
    j = 0
    k = 0
    
    m = int(input("Ingrese un entero positivo: "))
    while m <= 0 :
        if(m <= 0): print("Error! m debe ser >0 ")
        m= int(input("Ingrese un entero positivo: "))
        
    for k in range (1, m + 1):
        S1 = 0
        
        for i in range (1, k):
            S2 = 0
            
            if k % i == 0 :
                S1 = S1 + i
            
            for j in range (1, i):
                if i % j == 0:
                    S2 = S2 + j
                    
            print(f"\ni= {i} \tk={k} \tS1={S1} \tS2={S2}")
            
            if S1 == i and S2 == k:
                print(f"Los numeros {i} y {k} son numeros amigos")
            
            
if __name__ == "__main__":
    main()
```
# (P)ruebas

    
    | m        | amigo 1                                                |   amigo 2                                             | 
    
    |----------|--------------------------------------------------------|-------------------------------------------------------|
    
    |   290    | 220                                                    | 284                                                   |  
    
    |   1300   | 220                                                    | 284                                                   |
    |          | 1184                                                   | 1210                                                  |  
    
    |   -1     |   ¡Error! m debe ser >0                                |        	                                            |  
    
    |   2950   | 220                                                    | 284                                                   |
    |          | 1184                                                   | 1210                                                  |
    |          | 2620                                                   | 2924                                                  |  
    
    |  100000  | 220                                                    | 284                                                   |
    |          | 1184                                                   | 1210                                                  |
    |          | 2620                                                   | 2924                                                  |
    |          | 5020                                                   | 5564                                                  |
    |          | 6232                                                   | 6368                                                  |
    |          | 10744                                                  | 10856                                                 |
    |          | 12285                                                  | 14595                                                 |
    |          | 17296                                                  | 18416                                                 |
    |          | 63020                                                  | 76084                                                 |
    |          | 66928                                                  | 66992                                                 |
    |          | 67095                                                  | 71145                                                 |
    |          | 69615                                                  | 87633                                                 |
    |          | 71145                                                  | 67095                                                 |
    |          | 76084                                                  | 63020                                                 |
    |          | 79750                                                  | 88730                                                 |
    |          | 87633                                                  | 69615                                                 |
    |          | 88730                                                  | 79750                                                 |  
    





