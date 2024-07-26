# 8. Perrin

#### Dificultad: Intermedio

## Descripcion
*En matemáticas, los **números de Perrin** están definidos por la relación de recurrencia*
 
$P_0 = 3$

$P_1 = 0$

$P_2 = 2 ...$

$$P_n = P_{n-2} + P_{n-3} \text{ si } n > 2$$
  
*La serie sería:  3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39...*

*Determine el n-ésimo número de Perrín (n≥0).*

| Entrada | Salida |
|---------|--------|
| 3       | 3      |
| 6       | 5      |
| 8       | 10     |
| 0       | 3      |
| 1       | 0      |

# ADCP

## (A)nalisis

###### Entrada: 
n 

**Proceso mental:**
Es una sucesión infinita de números naturales introducida por François Oliver Raoul Perrin en 1899. Tiene su origen en un trabajo de 1876 de Édouard Lucas. Para explicar la regla de generación de los números, primero se debe inicializar los valores de P0=3, P1=0 y P2=2

$$P_n = P_{n-2} + P_{n-3} \text{ si } n > 2$$

Ejemplo

$P_0 = 3$ $P_1 = 0$ $P_2 = 2$ 

$P_3 = (P_1 + P_0) = 0+3 = 3$

$P_4 = (P_2 + P_1) = 2+0 = 2$

$P_5 = (P_3 + P_2) = 3+2 = 5$

$P_6 = (P_4 + P_3) = 2+3 = 5$

$P_7 = (P_5 + P_4) = 5+2 = 7$

Por lo tanto, para obtener el n-ésimo término de la serie se utilizará la expresión:  

$$P_n = P_{n-2} + P_{n-3}$$


###### Salida: 
n-ésimo término pn

###### Restricciones: 
n≥0, (con ello se podrá obtener p0, p1 y p2)

# (D)iseño

**En Lenguaje Natural:** 
1.	Primero, declaramos e inicializamos algunas variables: n (el número en la secuencia que queremos encontrar), i (variable de control para el ciclo) y las variables para los tres valores iniciales p0, p1 y p2.
2.	Luego, le pedimos al usuario que ingrese el valor de n.
3.	A continuación, comprobamos si n=0, n=1 o bien n=2, y se despliega el valor correspondiente de la secuencia (p0, p1 ó p2).
4.	Después, con un ciclo for que comienza desde i=3 hasta i=n. En cada iteración, se determina el siguiente valor de la secuencia de Perrin, que es la suma de p0 y p1, y se almacena en la variable perrin. Luego, actualizamos los valores de p0, p1 y p2 para la siguiente iteración.
5.	Finalmente, se despliega la variable perrin en pantalla, que es el número de la secuencia de Perrin correspondiente al valor de n ingresado por el usuario.



# (C)odificación en C
```c
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
```
# (C)odificación en Python
```py
def main():
    p0 = 3
    p1 = 0
    p2 = 2
    
    n = int(input("ingrese n:"))
    if n == 0:
        print(f"({p0})")
    elif n == 1:
        print(f"({p1})")
    elif n == 2:
        print (f"({p2})")
    else:
        perrin = 0
        for i in range (3, n + 1):
            perrin = p1 + p0
            p0 = p1
            p1 = p2
            p2 = perrin
        print(f"({perrin})")

if __name__ == "__main__":
    main()
```
# (P)ruebas

    |  Entrada(n)     | Salida (Perrin)   |
    |-----------------|-------------------|
    
    | 3               | 3                 |
    
    | 6               | 5                 |
    
    | 0               | 3                 |
    
    | 1               | 0                 |
    
    | 2               | 2                 |
    
    | 8               | 10                |
