# origen 
proviene del siguiente link
[origen](https://codeforces.com/gym/104791/problem/A)

traducido y adaptado por Vicente bastidas
# ejercicio

#### dificultad: facil 

## descripicion 
***EL AGUA*** 

en algun lugar del mundo existen **N** personas en una fila para obtener agua, la **i**-ecima quiere llenar su botella de **Ci** litros.

cuando el suministro de agua se agota (cada suministro proporciona **C** litros de agua)
el que estaba usando el suministro (incluso si este es el ultimo) reemplazara el suministro con uno nuevo, sin importar que ya haya terminado, luego de reemplazar el suministro este se retirara de inmediato asi que uno puede quedar con menos litros de los que queria.

ahora tu quieres saber cuantos suministros de agua hacen falta (contando el primero)

## input 
la primera linea es conformada por un solo entero T (1 <= T < 100) que representa la cantidad de casos de prueba.
cada caso de prueba contiene 2 lineas 
la primera linea contiene dos enteros n y c ( 1 < n <10000 , 1 < c< 1000)
la segunda linea contiene n enteros (1 < nc < 1000)



## output 
para cada caso de prueba debes imprimir un solo entero positivo que representa la cantidad de suministros ocupados 

# ADCP

## (A)nalisis

###### entradas
T entero, por cada entero  tenemos un 
N,C enteros, por cada N tenemos un Nc
Nc arreglo entero 

###### restricciones 

todos los numeros entregados deben ser positivos y distintos a 0
T debe estar entre 1 y 100
n debe estar entre 1 y 10000
c debe estar enter 1 y 1000
cada nc debe estar enter 1 y 1000

###### proceso

por como funcionan las restricciones, podemos centrarnos en hacer una pregunta sensilla, queda suficiente agua en el deposito para llenar algo de la botella de la persona?, o dicho como una resta, C - Nc es mayor a 0, si eso se cumple entonces el deposito actual de agua solo se hara mas pequeño, pero si no se cumple eso entonces contamos que se necesitara otro suministro y diremos que el suministro actual esta lleno eso se puede mostrar con una tabla o con un dibujo que muestre la progresion. 

podemos ver que sucede haciendo un ejemplo individual y una tabla 

N = 4 C = 10  Cn = [2,6,7,10]

|   litros deposito (Cd)    |   litros de la persona (Cn)   |   Cd - Cn     |   Cd - Cn <= 0    |   suministros usados  |
|   ---                     |   ---                         |   ---         |   ---             |   ---                 | 
|   10                      |   2                           |    8          |     no            |       1               |
|   8                       |   6                           |   2           |     no            |       1               |
|   2                       |   7                           |   -5          |       si          |       2               |
|   10                      |   10                          |   0           |       si          |       3               |  

siendo cada linea de la tabla la evolucion paso por paso de la fila de personas podriamos hacer un bosquejo de como se puede obtener la respuesta solo fijandonos si en cualquier momento el suministro tiene una cantidad negativa de litros 

##### salida 
un entero que indique cuantos suministros de agua se usaron 

---

## (D)iseño

por como es este ejercicio podemos realizar un pseudo codigo
```
> recibimos T
> POR cada T hacemos:
>   recibimos C y N 
>   creamos C_usar y lo igualamos a C
>   creamos dep_usa y lo igualamos a 1
>   recogemos todos los Cn en un arreglo
>   POR cada Cn hacemos:
>       C_usar lo igualamos a C_usar-Cn
>       SI C_usar es menor o igual a 0:
>           dep_usa crece en 1 
>           C_usar se resetea volviendo a C
>   imprimir (dep_usa)
```



## (C)odificacion


```py
T = int(input()) #casos que pide 

for j in range(T):
    n,c = [int(i) for i in input().split(" ")]; #recogemos la cantidad de personas y la cantidad de litros que soportara el tanque
    C_usar = c; # cuantos litros tiene en un momento especifico el tanque 
    dep_usa = 1 #la respuesta a imprimir
    Cn = [int(i) for i in input().split(" ")] #la cantidad de agua que quieren sacar 
    for i in Cn:
        C_usar = C_usar - i; #restamos la cantidad que quiere sacar la persona 
        if C_usar <= 0: # y revisamos si el valor es mayo a 0 y si lo es 
            dep_usa+=1; #contamos el hecho de rellenar el estanque 
            C_usar = c; #y lo volvemos a rellenar
    print(dep_usa)       
```

## pruebas 

|   input   | output|
|   ---     | ------|
|   4
3 1
6 4 5
4 1
1 6 4 5
2 10
5 2
5 10
8 6 7 10 2       |b      |