# 9.Los cubos

#### Dificultad: fácil

## Descripcion

*Considera la siguiente propiedad descubierta por Nicómaco de Gerasa:*

*“Sumando el primer impar, se obtiene el primer cubo;
Sumando los 2 siguientes impares, se obtiene el segundo cubo;
Sumando los 3 siguientes, se obtiene el tercer cubo, etc.”*

*Desarrolle un programa que lea el valor de N y calcule el N-ésimo cubo.*

# ADCP

## (A)nalisis
Los cubos de Nicómaco consisten en la suma de los N números impares. Por ejemplo: 

	1^3=1
    2^3=3+5=8
	3^3=7+9+11=27
    4^3=13+15+17+19=64

###### Entrada:  
Un número N

**Proceso mental:** 
Se utilizará una estrategia interesante (entre muchas):

**Casos particulares**

*Para N=1, se considera el primer impar.
Para N=2, Se consideran los 2 siguientes impares.
Para N=3, considerar los 3 siguientes impares.*

**Generalizando…**

A partir de lo anterior, para obtener el cubo de N, se deben sumar N impares. Además, notar que, si se desea obtener el cubo de 2, se debe partir la suma desde el 2° término. Para N=3, se debe partir desde el 4° término. Para N=4, partir desde el 7° término.

Puedo obtener hasta qué posición debo llegar, ejemplo para N=4, debe terminar en la décima posición. Para obtener la posición de inicio, simplemente restar n a la cota superior. Ejemplo: N=4, cota superior: 10, cota inferior: 6

Como ya se tiene la cota inferior, se forma el número impar que se genera en esta posición:  1,3,5,7,9,11.

A partir del 11, se suma los 4 siguientes impares: 13,15,17,19. Sumando ambos se obtiene 64, ¡Eureka!

###### Salida: 
El cubo de este número N

###### Restricciones: 
N>0


# (D)iseño (Pseudocódigo)
1.	Solicita al usuario que ingrese un número N.
2.	Verifica que N sea un número entero positivo mayor que cero.
3.	Calcula la suma de los primeros N números impares.
4.	Verifica si esta suma es un cubo perfecto.
5.	Si la suma es un cubo perfecto, muestra el número N y la suma total obtenida.



# (C)odificación en C v1
```c
#include <stdio.h>
#include <stdlib.h>

int main(){

    int n, superior, inferior, i, impar, cubo;
    do{
        scanf("%d", &n);
        if (n <= 0)
            printf("Ingrese un entero positivo\n");
    } while (n <= 0);

    impar = 1;
    superior = (n * (n + 1)) / 2;
    inferior = (superior - n);

    printf("cota inferior es: %d\n", inferior);
    printf("cota superior es: %d\n", superior);

    for (i = 0; i < inferior; i++){
        impar += 2;
    }
    cubo = 0;
    for (i = 0; i < n; i++){
        cubo += impar;
        impar += 2;
    }

    printf("%d al cubo es %d", n, cubo);

    return EXIT_SUCCESS;
}
```
# (C)odificación en C v2
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, cubo, impar, i;
    cubo = 0;

    do{
        scanf("%d", &n);
        if (n <= 0)
            printf("Ingrese un entero positivo\n");
    } while (n <= 0);

    impar = (n * (n - 1)) + 1;

    for (i = 0; i < n; i++){
        cubo += impar;
        impar += 2;
    }

    printf("el cubo es: (%d)", cubo);

    return EXIT_SUCCESS;
}
```
# (C)odificación en C v3
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, i, suma, cubo;

    do{
        scanf("%d", &n);
        if (n <= 0)
            printf("Ingrese un entero positivo\n");
    } while (n <= 0);

    suma = (n * (n + 1)) / 2;
    cubo = 0;

    for (i = (((suma - 1) * 2) + 1); i >= ((suma - n)) * 2 + 1; i -= 2)
        cubo += i;
    printf("(%d)", cubo);

    return EXIT_SUCCESS;
}
```
# (C)odificación en Python (basado en la v2 de C)
```py
n= -1
while n <= 0:
    n=int(input("Ingrese un entero positivo : "))
    if n <= 0:
        print("Debe ser positivo!")
    

cubo = 0
impar = (n*(n-1))+1

for i in range (n):
    cubo += impar
    impar += 2
print (f"El cubo es : ({cubo})")
```
# (P)ruebas

	|      Entrada |     Salida           |
	|--------------|----------------------|
	
	| 0            | Ingrese un número >0 |
	
	| 25           | 15625                |
	
	| 33           | 35937                |
	
	| -1           | Ingrese un número >0 |

