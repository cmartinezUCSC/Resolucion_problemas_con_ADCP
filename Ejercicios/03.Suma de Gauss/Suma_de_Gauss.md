# 3. Suma de Gauss 

#### Dificultad: fácil

## Descripcion
*Pedrito, un estudiante de 1º básico de un colegio local aprendió hace muy poco a sumar enteros, sin embargo, se le complica cuando se le acaban los dedos de las manos para acumular y requiere la ayuda de un programador experto que acumule todos los enteros comprendidos entre 1 y N (ambos incluidos), con N≥0.* 

| Entrada | Salida              |
|---------|---------------------|
| 3       | 6                   |
| 2       | 3                   |
| 5       | 15                  |
| -1      | ERROR, debe ser>= 0 |
| 0       | 0                   |

# ADCP

## (A)nalisis

###### Entradas:   
ota superior (n)

**Proceso mental:** 
¿Se deben sumar todos los números comprendidos entre 1 y n? ¿Qué significa?:

**Casos particulares:**

Para n=1, se debería acumular 1  
Para n=2, se debería acumular: 1+2 = 3  
Para n=5, se debería acumular: 1+2+3+4+5 = 15  

**Generalizando:**
Por lo tanto, para n = k, acumular: 1+2+3+...+k    

###### Salida: 
1+2+3+…+n

###### Restricciones: 
n≥1

# (D)iseño (Lenguaje Natural semi estructurado):

1.	Definir 3 variables (n, i, sumaresultado)
2.	Comprobar que **n** sea mayor a 0.
3.	Hacer uso de un ciclo repetitivo de  tamaño n (dado que se conoce el número de iteraciones) incluyendo la instrucción **sumaresultado = sumaresultado + i** (i actúa como iterador con i  [1..n]; sumaresultado actúa como acumulador, observe el efecto de estar a ambos lados de la asignación).
4.	Finalmente, imprimir **sumaresultado**
    
*Y en Pseudocódigo quedaría así (observe la diferencia con el lenguaje natural semi estructurado):*

### Algoritmo Suma de Gauss
```pseint
Algoritmo suma_de_Gauss
	Definir suma,i, n Como Entero
	Repetir
		Escribir 'Ingrese un número mayor o igual a 1'
		Leer n
		Si n<1 Entonces
			Escribir 'Error, debe ser >=1'
		FinSi
	Hasta Que n>1
	suma=0;
	Para i<-1 Hasta n Hacer
		suma <- suma+i
	FinPara
	Escribir 'La suma de Gauss es para ', n,' es ', suma
FinAlgoritmo
```

# (C)odificación en C
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, i, resultado;
    resultado = 0;
    scanf("%d", &n);

    if (n < 1){
        printf("Error, debe ser >= 1");
    }else{
        for ( i = 0; i <= n; i++){
            resultado += i;
        }
        printf("%d", resultado);
    }

    return EXIT_SUCCESS;
}
```
# (C)odificación en Python
```py
def main():
    
    n = int (input("Ingrese un numero"))
    resultado = 0
    
    if n < 1:
        print("Error, debe >=1")
    else:
        for i in range (1, n + 1):
            resultado +=i
            
        print("La suma de los numeros desde 1 hasta {} en: {} ".format(n, resultado))

if __name__=="__main__":
    main()
```
# (P)ruebas


      |      Entrada | Salida               |
      |--------------|----------------------|
      
      |-3            | ERROR, debe ser >= 1 |
      
      | 0            | ERROR, debe ser >= 1 |
      
      | 5            | 15                   |
      
      | 10           | 55                   |

