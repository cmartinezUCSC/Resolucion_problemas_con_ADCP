# 10.Sucesión la Bicicleta

#### Dificultad: Intermedia

## Descripcion

$$b_n = \frac{b_{n-1} + 1}{b_{n-2}}, \quad \forall n \geq 3$$

*Esta sucesión se denomina así ya que para avanzar a través de sus términos basta con hacer “rodar” dos consecutivos. Por ejemplo, si tomamos los primeros términos de la sucesión 2 y 3 se obtiene que el siguiente es 2, sorprendentemente la generación es cíclica:*

\[2, 3, 2, 1, 1, 2, 3, …\]

*Dado un n≥ 3, construya un programa que genere los primeros **n** términos de la Sucesión Bicicleta.*

# ADCP

## (A)nalisis

###### Entrada: 
N  

**Proceso mental:** 
Tal como en sucesión de Fibonacci, el término n-ésimo de la sucesión de la bicicleta se obtiene a partir de los 2 términos anteriores, es por esto que es necesario partir con los términos b_0 y b_1:

\[ b_n = \frac{b_{n-1} + 1}{b_{n-2}}, \quad \forall n \geq 3 \]


###### Salida: 
N primeros términos de la sucesión de la bicicleta ($b_0, b_1, b_2...b_n$)

###### Restricciones: 
N>=3

# (D)iseño (pseudoCódigo)
```pseint
Algoritmo La_Bicicleta
    Repetir 
        Leer n
        Si n<3 entonces escribir "Error, debe ser >=3"
        FinSi
    Hasta Que n>=3
    b0=2
    b1=3
    Escribir b0, ",", b1

    Para i<-3 hasta N
        bn=(b1+1/b0)
        Escribir bn, ","
        b0=b1
        b1=bn
    FinPara
FinAlgoritmo
```

# (C)odificación en C
```c
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
```
# (C)odificación en Python
```py
def main():
    b0, b1, bn = 2.0, 3.0, 0.0
    i, n= 0, 0
    
    while n < 3:
        n = int(input("Ingrese un numero (debe ser >= 3) : "))
        if n >= 3:
            break
        else:
            print("Error, debe ser >= 3 ")
            
    b0,b1= 2.0, 3.0
    print("{}\n{}".format(b0, b1))
    
    for i in range(1, n - 1):
        bn = (b1 + 1)/b0
        print("{}".format(bn))
        b0, b1 = b1, bn
    

if __name__ == "__main__":
    main()
```
# (P)ruebas

    |   Entrada    |     Salida                               |
    |--------------|------------------------------------------|
    
    |  0           | Error debe ser >=3                       |
    
    |  3           | 2.0, 3.0, 2.0                            |

    |  7           | 2.0, 3.0, 2.0, 1.0, 1.0, 2.0, 3.0        |
    
    | -1           | Error debe ser >=3                       |



