# origen 
proviene del siguiente link 
[origen](https://codeforces.com/gym/104146/problem/A)

traducido por Vicente Bastidas
# ejercicio

#### dificultad: facil - intermedio

## descripicion 

¡Alice, Bob y Cindy han decidido irse de viaje por las fiestas! Mientras el resto de sus amigos han ido a vacacionar a japon y europa, estos tres amigos han decidido una alternativa mas divertida (y económica), explorar las filipinas en grupo, por pura coincidencia los 3 compraron la misma maleta para el viaje. Por buena suerte todos decidieron rotular sus maletas con su nombre (estas etiquetas distinguen entre mayusculas y minusculas).
Por desgracia en estas etiquetas se han ido borrando algunas letras con el tiempo, al menos tienes asegurado que el largo de la palabra se mantiene, ayudemosles a que pasen unas vacaciones libres de estres escribiendo un programa que identifique al dueño de la maleta una etiqueta poco legible asumiendo que el dueño es Alice, Bob o Cindy

|Input  | Output            |
|-|-|
|Ali.e  | Alice             |
|bob    | SOMETHING'S WRONG |
|.i...  | Cindy             |



# ADCP

## (A)nalisis

###### entradas
un string S 

###### restricciones 
S debe tener entre 1 a 5 caracteres, estos caracteres deben ser letraslas cuales pueden ser mayusculas o minusculas o puede ser un punto

###### salida 
se asume que puede ser Alice, Cindy o Bob el dueño entonces 
para la salida tenemos 3 opciones posibles, 
- si con las letras visibles solo puede ser uno de los 3 nombres entonces  se imprime el nombre 
- si existiera mas de una posibilidad se imprime CAN'T TELL
- si el nombre no coincide con ninguno de los 3 se imprime SOMETHING'S WRONG

###### proceso
lo primero que podemos filtrar, es el caso de que el nombre ingresado devuelva "SOMETHING'S WRONG", eso en primer momento lo podemos solucionar de forma muy sensilla con una pregunta, ¿el string que nos entregan tiene 3 o 5 caracteres? si la respuesta es no, imprimimos "SOMETHING'S WRONG" y terminariamos el ejercicio, si la respuesta en un si por otro lado, podriamos ver como progresa, primero viendo con el caso de que fuera de solo 3 caracteres de largo. 

para eso usamos a Bob, como Bob solo tiene 3 caracteres podriamos comparar los posibles casos y compararlos uno a uno 

| B | . | . |
|---|---|---|
|B  |o  |b  |
|si | puede ser| puede ser|

en este caso como la cantidad de caracteres es 3 y el unico caracter que nos da la pista es correcto, podemos asumir que es la maleta de bob

|b|o|b|
|-|-|-|
|B|o|b|
|NO| si| si|

en este caso la maleta no es de bob porque el escribe su nombre con una mayuscula al principio por lo que imprimiriamos SOMETHING'S WRONG

|.|.|.|
|-|-|-|
|B|o|b|
|tal vez|tal vez|tal vez|

en este caso la respuesta seria Bob puesto que es la unica posibilidad con tres caracteres de los tres nombres


ahora en caso de que el largo sea de 5 tenemos un poco mas de variedad, para eliminar la posibilidad de que sea cualquiera descartamos la posibilidad de que sea cualquiera de los 2 nombres por lo que si diera que entregan ..... sabremos al instante que tenemos que imprimir CAN'T TELL.

si ese no fuera el caso habria que ver como reconocer a que persona corresponde, para eso podriamos ir comparando letra a letra de nuevo, pero ahora viendo que palabra forma de forma que si es un punto asumimos que es la letra correcta y si en algun momento aparece una letra que no calza intentamos con la otra persona posible 



## (D)iseño

![](diagrama.png)

## (C)odificacion

```py
S = input() 
nom = ["Bob","Alice","Cindy"] #anotamos los tres nombres para tener una gestion mas simple del 
resp = "" #dejamos esto como un string vacio para usarlo mas adelante

if len(S) == 3:   #aca es donde comienzas las preguntas, primero vemos si la palabra puede ser bob o no puesto que es el unico nombre con 3 caracteres de largo
    for i in range(3): 
        if S[i] == nom[0][i]: #si la letra en cuestion coincide con la de la misma posicion decimos que esta bien y en resp anotamos esa letra 
            resp = resp + S[i]
        elif S[i] == ".": #si la letra fuera un punto asumimos que es la letra del nombre que le corresponde 
            resp = resp + nom[0][i]
        else: # si ninguna de estas posibilidades se cumple asumiremos que algo salio mal y diremos que algo salio mal y terminaremos el programa 
            resp = "somethin wrong"
            break
elif S == ".....": #por otro lado si son todos puntos y son cinco caracteres diremos que no se puede determinar 
    resp = "CAN'T TELL"
else: #si ese no fuera el caso y ubiera algunas letras podemos replicar lo que hicimos con bob pero con los dos nombres que faltan por verificar.
    for i in range(5): 
        if S[i] == nom[1][i]:
            resp = resp + S[i]
        elif S[i] == ".":
            resp = resp + nom[1][i]
        else:
            resp = "somethin wrong"
            break
    if resp != nom[1]:
        resp = ""
        for i in range(5):
            if S[i] == nom[2][i]:
                resp = resp + S[i]
            elif S[i] == ".":
                resp = resp + nom[2][i]
            else:
                resp = "somethin wrong"
                break    
print(resp)
```

## (P)ruebas 

|input|output|
|-|-|
|Bob|Bob|
|B..|Bob|
|Ci...|Cindy|
|Ali.e  | Alice             |
|bob    | SOMETHING'S WRONG |
|.i...  | Cindy             |
