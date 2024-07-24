# 11.Euclides

#### Dificultad: fácil

## Descripcion

*Obtener el máximo común divisor de 2 números usando el algoritmo de Euclides.*

# ADCP

## (A)nalisis

###### Entradas: 
2 Números enteros (m, n)  

**Proceso mental:** 

¿máximo común divisor? El máximo común divisor (MCD) es el mayor número entero que divide exactamente a dos o más números
enteros sin dejar residuo. En  otras palabras, es el número más grande que es un divisor común a todos los números dados.

El MCD es una noción importante en la teoría de números y tiene varias aplicaciones en matemáticas y ciencias 
computacionales, como en simplificación de fracciones, criptografía, algoritmos de optimización, entre otros. 
El algoritmo de Euclides es un método antiguo y eficaz para calcular el máximo común divisor (MCD).

¿Qué es la divisibilidad? se dice que m es divisible por 

i si (m mod i=0)

¿Cómo se describiría en lenguaje natural?

1. paso 1 Leer m, n
2. paso 2 Verificar cuál de los 2 números es mayor...para definir la cota superior del divisor
3. paso 3 Calcular el resto de la división de m y n por el iterador i hasta que este llegue a la cota superior
4. paso 4 Guardar el valor de i en caso de cumplir condición de divisibilidad para m y simultáneamente para n
5. paso 5 Imprimir el máximo

###### Salida: 
MCD

###### Restricciones: 
Ninguna


# (D)iseño (pseudoCódigo)
```pseint
Algoritmo Euclides
	leer m,n
	si n<=m Entonces
		final=n
	Sino
		final=m
	FinSi
	Para i=1 hasta final hacer //excluir el 1 
		si (n%i=0 y m%i=0) entonces
				maximo=i;
		FinSi
	FinPara
	Escribir "Máximo comun: ",maximo;
FinAlgoritmo
```

# (C)odificación en C v1
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int final, i, m, n, maximo;

    scanf("%d", &m);
    scanf("%d", &n);

    if (n <= m){
        final = n;
    }else{
        final = m;
    }

    for (i = 1; i <= final; i += 1){
        if ((n % i == 0 && m % i == 0)){
            maximo = i;
        }  
    }
    
    printf("Maximo comun: %d\n", maximo);

    return EXIT_SUCCESS;
}
```
# (C)odificación en C v2
```c
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
```
# (C)odificación en Python
```py
def main():
    m, n=0,0
    
    while True:
        try:
            m, n =map(int, input("Ingrese dos numeros separados por espacio: ").split())
            
            if m != 0 and n != 0:
                if m%n == 0:
                    if m < n:
                            print (m)
                    if n < m:
                            print (n)
                else:
                    while m % n != 0:
                        mod = m % n
                        m = n
                        n = mod
                    print (mod)
                break
            else:
                print("ERROR, deben ser != 0 ")
        except ValueError:
            print ("ERROR, entrada no valida. Ingres numeros enteros")
        

if __name__ == "__main__":
    main()
```
# (P)ruebas
    
    | Entrada   | Salida   |
    
    |-----------|----------|
    
    | 3, 4      | 1        |
    
    | 12, 3     | 3        |
    
    | 24, 14    | 2        |
    
    | 21, 7     | 7        |


