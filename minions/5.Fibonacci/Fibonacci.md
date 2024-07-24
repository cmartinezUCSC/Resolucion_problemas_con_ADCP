# 5.Fibonacci

#### Dificultad: fácil

## Descripción
La sucesión de Fibonacci es la sucesión de números:

**0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...**

Cada número se calcula sumando los dos anteriores a él. 

Ejemplo:

*El 2 se calcula sumando (1+1)
análogamente, el 3 es sólo (1+2),
y el 5 es (2+3),
¡y así!*

Genere **la sucesión de Fibonacci** hasta el n-ésimo término de Fibonacci, considere t0=0, t1=1



# ADCP

## (A)nálisis
###### Entrada: 
n  

**Proceso mental:** 
Para explicar la secuencia se podría aplicar la siguiente función de recurrencia:

t0 = 0, t1 = 1  
t2 = (t0+t1) = 0+1 = 1  
t3 = (t1+t2) = 1+1 = 2  
t4 = (t2+t3) = 1+2 = 3  

Por lo tanto, para obtener el n-ésimo término de Fibonacci, se debe sumar el valor de

tn = tn-1+tn-2

###### Salida: 
tn

###### Restricciones: 
n>=0

# (D)iseño

**En Lenguaje Natural:**

1.	Como se sabe que los casos iniciales t0=0 y t1=1, debiéramos definir estas dos variables, en 0 y 1 respectivamente, también se debe definir un acumulador tn (inicializado en 0, tn=0). 
2.	Solicitar por teclado el valor de “N” y comprobar que sea mayor o igual a cero. Acá se pueden dar 3 casos: 
3.	Si n=0 -> simplemente mostrar en la salida t0=0
4.	Si n=1-> mostrar t1=1
5.	Si n>1, se debe realizar un ciclo repetitivo (desde 1 hasta n-1), y por cada iteración darle al acumulador la suma de t0y t1, una vez realizada la suma, intercambiar t0 por t1 y t1 por acumulador tn. Finalmente, mostrar el resultado en pantalla.



**En pseudocódigo (Pseint)**
```pseint
Algoritmo Fibonacci
    Definir t0,t1 Como Entero
    t0=0
    t1=1
    Repetir
        Escribir 'Ingrese un número mayor o igual a 0'
        Leer n
        Si (n<0) Entonces Escribir 'Error, debe ser >=0'
        FinSi
    Hasta Que n>=0
    Si n=0 Entonces Escribir "t0=",t0
    sino
        Si n=1 entonces 
            Escribir "t0=",t0
            Escribir"t1=",t1
        sino
            Escribir "t0=",t0
            Escribir "t1=",t1
            Para i<-2 hasta n-1 hacer
                tn=t0+t1
                t0+t1
                Escribir"t",i,"=",tn
            FinPara
        FinSi
    FinSi
FinAlgoritmo
```

## Diagrama de Flujo (Pseint)
![](imagen.png)


# (C)odificación en C
```c
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
```
# (C)odificación en Python
```py
def main ():
    n = -1
    
    while n < 0:
        try:
         
         n = float(input("Ingrese un numero mayor o igual a 0:"))
         if n < 0:
            print("Error, debe ser >= 0")
        except ValueError:
            print("Error, ingrese un numero valido.")
    
    t0 = 0
    t1 = 1
    
    if n == 0:
        print(f"t0={t0}")
    else:
        print(f"t0={t0}")
        print(f"t1={t1}")
        
        for i in range(2, int(n) + 1):
            tn= t0 + t1
            t0, t1 = t1,tn
            print(f"{i}={tn}")
            
if __name__ == "__main__":
    main()
```
# (P)ruebas

    |    Entrada   |     Salida              |
    |--------------|-------------------------|
    
    | 0            | 0                       |
    
    | 1            | 0 1                     |
    
    | 2            | 0 1 1                   |
    
    | 9            | 0 1 1 2 3 5 8 13 21 34  |
    
    |-1            | ERROR, debe ser >= 0    |

