
# 2.Raíz i-ésima

#### Dificultad: fácil

## Descripcion

*Se desea determinar la raíz i-ésima, i>0 de un valor n ingresado. Para ello, el usuario ingresará 2 números, donde el primer término es el número al que se le calculará la raíz y el segundo el valor de i. El resultado de la operación debe generarse con 3 cifras decimales.*

| Entrada  | Salida                    |

\|----------|---------------------------|

| 1427,3    | 11.258                   |

| 52538,2   | 229.212                  |

| 144, 0    | Error, debe ser >0       |

| 27, 3     | Error, debe ser >= 0     |

| 0,3       | 0.000                    |



# Solución ADCP

# ANÁLISIS:

###### Entradas:  
Un número representando la base (n) y otro representando el recíproco del exponente (i).

Proceso mental: Se sabe que la raíz i-ésima de un número n se puede trabajar como potencia con exponente fraccionario.

* Por ejemplo\*:    	

    √(4)  =4^(1/2)

    ∛8=8^(1/3)

    ∜16=16^(1/4)

    Generalizando,

    √(i&n)=n^(1/i)con i>0

###### Salida: 
La raíz i-ésima del número n

###### Restricciones: 
n debe ser mayor que 0, para evitar raíces 

*imaginarias e i estrictamente positivo para evitar la división por 0, n≥0 e i>0*

# DISEÑO (Lenguaje Natural):
	Definir 3 variables (n, i, raiz). 
	Leer por teclado las variables n, i (no olvidarse que i > 0 y n≥0). 
	Una vez leídos ambos valores, se hará el cálculo.
	Finalmente mostrar el resultado por pantalla.

# (C)odificación Py v1
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

# (C)odificación Py v2
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
# (C)odificación C
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

# (P)ruebas


| Entrada  | Salida                    |

\|----------|---------------------------|

| 1427,3    | 11.258                   |

| 52538,2   | 229.212                  |

| 144, 0    | Error, debe ser >0       |

| -27, 3    | Error, debe ser >= 0     |

| 0,3       | 0.000                    |