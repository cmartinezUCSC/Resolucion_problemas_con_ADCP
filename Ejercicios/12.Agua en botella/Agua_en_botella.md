
# 12. Agua en botella

#### Dificultad: fácil

## Descripcion

*En algún lugar del mundo existen **n** personas en una fila para obtener agua, la i-ésima quiere llenar su botella de ci litros. Cuando se acaba el balde de agua del dispensador de agua (Cada balde de agua proporciona C litros de agua), quien esté utilizando el dispensador de agua (incluido el último) sustituirá el balde del dispensador por un balde nuevo o agua, incluso si tiene suficiente agua. Luego se va inmediatamente, por lo que uno puede irse con menos agua de la que quiere.*
    
*Ahora se requiere conocer cuántos baldes de agua se necesitan (incluido el primer balde).*

**Entrada**
    
La primera línea contiene un único número entero **T** (1≤**T**≤100) que corresponde al número de casos de prueba.
Cada caso de prueba contiene dos líneas.
La primera línea contiene dos números enteros **n, C** (1 ≤ ∑**n** ≤ 106,1≤ **C** ≤103)   
La segunda línea contiene **n** números enteros **$c_i$** (1≤ **$c_i$** ≤103), i=1..n

*4
3 1
6 4 5
4 1
1 6 4 5
1 10
5 2
5 10
8 6 7 10 2*

**Salida**

Para cada caso de prueba, imprima un número entero positivo que represente la cantidad de baldes necesarios.

*4
5
1
3*

# ADCP

## (A)nalisis

###### Entrada: T: 
número de casos de prueba, **n**: número de personas, **C**: capacidad en litros del balde, **$c_i$** : requerimientos de agua de cada persona, **i**=1..n

###### Salida: B:  
cantidad de baldes de agua necesarios para cubrir necesidades. 

###### Proceso: 
Podemos centrarnos en hacer una pregunta sencilla, ¿queda suficiente agua en el balde para llenar algo de la botella de la persona?, o dicho como una diferencia (C – $C_i$) >0, si eso se cumple entonces el balde cubre necesidad y se debe reducir según requerimiento, pero si no se cubre toda la botella se necesitará otro balde, aun cuando sobre agua.  Consideremos un ejemplo: n = 4 C = 10 Ci = [2,6,7,10], i=1..4

| Litros remanentes (C) | Litros requeridos por persona (Ci) | C - Ci | C - Ci < 0 | Baldes usados (B) |
|-----------------------|------------------------------------|--------|------------|-------------------|
| 10                    | 2                                  | 8      | no         | 1                 |
| 8                     | 6                                  | 2      | no         | 1                 |
| 2                     | 7                                  | -5     | sí         | 2                 |
| 10                    | 10                                 | 0      | sí         | 3                 |


# (D)iseño (PseudoCódigo):
```pseint
Leer T
 Para cada T hacemos:
   Leer C y n 
   C_uso=C
   Baldes=1
   Para cada i=1..n 
         Leer Ci en un arreglo
   FinPara
   Para cada Ci, 1..n 
       C_uso = C_uso-Ci
       SI C_uso <= 0
           Baldes++
           C_uso = C
       FINSI
       FinPara
 FinPara
Escribir (Baldes)
```


# (C)odificación en C
```c
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
```
# (C)odificación en Python
```py
T = int (input())

for j in range (T):
    n,c = [int(i) for i in input().split(" ")]
    C_uso = c
    baldes = 1
    
    Cn = [int(i) for i in input().split(" ")]
    for i in Cn:
        C_uso -= i
        if C_uso <= 0:
            baldes += 1
            C_uso = c
            
    print(baldes)
```
# (P)ruebas


    | Entrada    | Salida   |

    |------------|----------| 
    
    | 4          |   4      |
    | 3 1        |          |
    | 6 4 5      |          |

    | 4 1        |   5      |
    | 1 6 4 5    |          |

    | 2 10       |   1      |
    | 5 2        |          |

    | 5 10       |   3      |
    | 8 6 7 10 2 |          |
