
# 2.Raíz i-ésima

#### Dificultad: fácil

## Descripcion

*Se desea determinar la raíz i-ésima, i>0 de un valor **n** ingresado. Para ello, el usuario ingresará 2 números, donde el primer término es el número al que se le calculará la raíz y el segundo el valor de i. El resultado de la operación debe generarse con 3 cifras decimales.*

| Entrada   | Salida                   |
|-----------|--------------------------|
| 1427, 3   | 11.258                   |
| 52538, 2  | 229.212                  |
| 144, 0    | Error, debe ser > 0      |
| -27, 3    | Error, debe ser >= 0     |
| 0, 3      | 0.000                    |

# ADCP

## (A)nalisis

###### Entradas:  
Un número representando la base **(n)** y otro representando el recíproco del exponente (i).

Proceso mental: Se sabe que la raíz i-ésima de un número n se puede trabajar como potencia con exponente fraccionario.

* Por ejemplo\*:    	
    \[ \sqrt[2]{4} = 4^{\frac{1}{2}} \]

    \[ \sqrt[3]{8} = 8^{\frac{1}{3}} \]

    \[ \sqrt[4]{16} = 16^{\frac{1}{4}} \]

    Generalizando, \[ \sqrt[i]{n} = n^{\frac{1}{i}} \]

###### Salida: 
La raíz i-ésima del número **n**

###### Restricciones: 
**n** debe ser mayor que 0, para evitar raíces imaginarias e **i** estrictamente positivo para evitar la división por 0, **n**≥0 e **i**>0

# (D)iseño (Lenguaje Natural):
1. Definir 3 variables **(n, i, raiz)**. 
2. Leer por teclado las variables **n, i** (no olvidarse que **i** > 0 y **n**≥0). 
3. Una vez leídos ambos valores, se hará el cálculo.
4. Finalmente mostrar el resultado por pantalla.

# (C)odificación en C
```c
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    float numero, i, raiz;

    do{
        scanf("%f", &numero);
        if (numero < 0){
            printf("ERROR, debe ser >= 0\n");
        } 
    } while (numero < 0);

    do{
        scanf("%f", &i);
        if (i <= 0){
            printf("ERROR, debe ser > 0\n");
        }    
    } while (i <= 0);

    raiz = pow(numero,(1/i));

    printf("%.3f", raiz);

    return EXIT_SUCCESS;
}
```
# (C)odificación en Python v1
```py
import math
numero = float(input())

while numero < 0:
    print("ERROR,debe ser >=0")
    numero = float(input())
    
i=float(input())
while i <= 0:
    print("ERROR,debe ser >0")
    i = float(input())
raiz = numero ** (1/i)

print(f"{raiz:.3f}")
```

# (C)odificación en Python v2
```py
import math

def main():
    numero,i,raiz = 0.0, 0.0, 0.0
    
    while True:
        try:
            numero = float(input())
            if numero < 0:
                print("Error,debe ser >= 0")
            else:
                break
        except ValueError:
            print("ERROR, entrada no valida. Ingrese un numero")
            
    while True:
        try:
            i = float(input())
            if i<= 0:
                print("ERROR, debe ser > 0")
            else:
                break
        except ValueError:
            print("ERROR, entrada no valida, ingrese un numero")
    
    raiz= numero ** ( 1 / i )
    
    print("{:.3f}".format(raiz))
    
if __name__ == "__main__":
    main()
```

# (P)ruebas


		| Entrada   | Salida                   |
		
		|-----------|--------------------------|
		
		| 1427,3    | 11.258                   |
		
		| 52538,2   | 229.212                  |
		
		| 144, 0    | Error, debe ser >0       |
		
		| -27, 3    | Error, debe ser >= 0     |
		
		| 0,3       | 0.000                    |
