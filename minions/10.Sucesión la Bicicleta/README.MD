# 10. Sucesión la Bicicleta

#### Dificultad: Intermedia

## Descripcion

b_n = (b_n-1 + 1)/(b_n-2) , ∀ n≥ 3

Esta sucesión se denomina así ya que para avanzar a través de sus términos basta con hacer “rodar” dos consecutivos. Por ejemplo, si tomamos los primeros términos de la sucesión 2 y 3 se obtiene que el siguiente es 2, sorprendentemente la generación es cíclica:

2, 3, 2, 1, 1, 2, 3, …

Dado un n≥ 3, construya un programa que genere los primeros n términos de la Sucesión Bicicleta.

# Solución ADCP

# (A)NÁLISIS
###### Entrada: N  

###### Proceso mental: Tal como en sucesión de Fibonacci, el término n-ésimo de la sucesión de la bicicleta se obtiene a partir de los 2 términos anteriores, es por esto que es necesario partir con los términos b_0 y b_1:

b_n = (b_n-1 + 1)/(b_n-2) , ∀ n≥ 3


###### Salida: N primeros términos de la sucesión de la bicicleta (b_0, b_1, b_2...b_n)

###### Restricciones: N>=3

## DISEÑO (pseudoCódigo)
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



# (C)odificación Py:
```py

```
# (C)odificación C:
```c
    
```
# (P)ruebas

|      Entrada |     Salida           |
\|-------------|-----------------------|

| 0            |Error debe ser >=3    |

| 3            |2, 3, 2               |

| 7            | 2, 3, 2, 1, 1, 2, 3… |

| -1           |Error debe ser >=3    |



