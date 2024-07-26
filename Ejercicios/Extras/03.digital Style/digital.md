# Origen 

https://codeforces.com/gym/104146/problem/D

traducido por Vicente Bastidas

# Ejercicio 3

#### dificultad: facil 

## Descripición 
En el mundo digital, solo existen 3 cosas para hacer.

¡Hello, realidad virtual! ¡bob esta exitado de explorar el descabellado e increible sitio conosido como la www (world wild web)! [ya vio el detallado tutorial](https://www.youtube.com/watch?v=A81IwlDeV6c) del internet que le enseñara a un cabro genial como el como navegar en el ciberespacio. ¡Lo unico que le falta es un nombre de usuario!.

Por desgracia, su nombre de usuario preferido bobTheBuilder ya esta tomado asi que como es abitual bob va a agregarle un numero al final de su usuario, pero no cualquier numero sirve, bob quiere que sea un numero positivo que tome en cuenta el _estilo digital_ del mismo, es mas, el numero no puede ser ni muy grande ni muy pequeño ni muy grande.

el estilo digital de un positivo **n** es unicamente el producto de sus digitos, por ejemplo el estilo digital de **1984** es **1 x 9 X 8 x 4 = 288**.
Pero a Bob le gusta llevar la contraria, veras el de hecho quiere **minimizar** su estilo digital porque piensa que no siendo genial es la nueva cosa genial, (mientras lo hagas de forma ironica al menos). asi que dado dos enteros **L** y **R** cual es el estilo digital minimo eentre todos los **n** tal que **L <= n <= R**.

**Input**
las entradas constan de una sola linea que contiene enteros **L** y **R** separados por un espacio.

**Output**
entrega un entero simple que sea el minimo entre los posibles estilos digitales entre todos los enteros dados.

**ejemplo**

|input     | output|
|----------|-------|
|42 47     |    8  |
|225 228   |   20  |

# ADCP

## (A)nálisis

###### entradas
dos enteros positivos entre 1 y 1000

###### restricciones 
que los valores sean positivos y que L sea menor que R 

###### proceso
en este caso para ver como realizar el ejercicio podemos ver como se ven los estilos digitales de los casos de prueba que implementa
por ejemplo con 225 y 228

|225|2 * 2 * 5|20|
|-|-|-|
|226|2 * 2 * 6|24|
|227|2*  2 * 7|28|
|228|2*  2 * 8|32|

con esto podemos ver porque nos daba 20 y si probamos con una muestra un tanto mas particular podriamos probar con 126 y 135 

lo que nos daria 

|126| 1 * 2 * 6 |12|
|-|-|-|
|127| 1 * 2 * 7 |14|
|128| 1 * 2 * 8 |16|
|129| 1 * 2 * 9 |18|
|130| 1 * 3 * 0 |0|
|131| 1 * 3 * 1 |3|
|132| 1 * 3 * 2 |6|
|133| 1 * 3 * 3 |9|
|134| 1 * 3 * 4 |12|
|135| 1 * 3 * 5 |15|

con todo esto podemos tener todos los casos y vemos que aqui el estilo digital seria 0 porque es el valor mas bajo 

###### salida 
un numero entero 

## (D)iseño

```
> recibimos los dos valores L y R
> creamos una lista vacia para poner las opciones posibles
> recorremos todos los numeros entre los valores L y R 
> en cada numero aplicamos la logica del estilo, eso es separar por digitos el numero y multiplicar el resultado
> si ese valor es 0 paramos de hacer los estilos, porque no puede haber un numero positivo mas pequeño que 0
> si el valor no es 0 entonces lo agremos a la lista 
> ordenamos la lista (esto lo hacemos siempre por si acaso no ubiera un 0 )
> imprimimos el primer numero de la lista
```

## (C)odificación
```py
L,R = [int(i) for i in input().split(" ")] #recogemos los dos elementos
resp = [] 
for i in range(L,R+1): #R+1 para que alcance a R 
    aux = 1 #creamos una variable auxiliar
    for j in str(i): #tratamos al numero que evaluamos como un string para poder separarlo elemento a elemento  
        aux = aux*int(j) #realizamos uno a uno el estilo digital
    if aux == 0: #si en algun momento aux da 0 cancelamos de inmediato porque es el numero mas pequeño que va a haber nunca 
        break
    resp.append(aux) #si no hay ningun 0 entonces agregamos todo esto a un arreglo de respuestas
resp.sort() #ordenamos las opciones posibles 
print(resp[0]) #y simplemente imprimimos la primera porque sera la mas pequeña
```

## (P)ruebas 

|input|output|
|---|---|
|126 181| 0|
|225 228|20|
|761 769| 42|

