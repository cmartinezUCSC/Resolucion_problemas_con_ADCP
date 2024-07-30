# origen 
[origen](https://codeforces.com/gym/103185/problem/E)

traducido por Vicente Bastidas 
# ejercicio

#### dificultad: media 

## descripición 
Ciudad brillante, es una hermosa ciudad conocida por 3 cosas, por su reconocida unica calle, por el hecho de que cada edificio tiene distintos tamaños y las maravillosas vistas que se pueden ver desde arriba de los edificios.

Desde el comienzo de la pandemia la canidad de turisstas a disminuido considerablemente pero tu como el buen periodista que eres sabes que si haces el mejor post este atraera turistas y salvara de la ruina economica a tu ineficiente ciudad, miserablemente te falta informacion acerca de tu ciudad. 

En ciudad brillante existen N edificios, donde el edificio i-esimo se identifica por su posicion i, para ir del edificio i al edificio j, toma |i-j| minutos, cada edificio tiene un tamaño Hi distinto y entre mas alto sea el edificio mejor sera la vista desde arriba.

Si uno esta en un edificio especifico, podria valer la pena ir a un edificio diferente con una mejor vista, por temas de costes de transporte  nunca es conveniente ir a un edificio si existe uno con mejor vista a menos distancia que recorrer.

Formalmente, podemos decir que ir desde el edificio i hasta otro edificio j vale la pena si no existiera otro edificio k de tal forma que |i−k|≤|i−j| y que Hj < Hk (puede ser que K sea igual a i).

asi que con esa informacion lo tienes claro, tienes que escribir en tu post cuantos otros edificios merece la pena visitar desde cada uno de los edificios, ahora solo queda ver como obtener esa informacion para evitar la caida de ciudad brillante. 

*ejemplo*
| input | output | 
| --- | --- |
| 10 | 3 4 3 2 1 0 1 2 1 2 |
|23 20 7 30 43 70 5 42 67 10 | | 
# ADCP

## (A)nalisis

###### entradas

un entero N 
N enteros separados por un espacio 

###### proceso

este ejercicio puede parecer enredado, pero si nos fijamos bien nos indica directamente que es lo que tenemos que hacer para poder resolverlo. 

asi que tendremos que ir distancia a distancia (es decir los edificios que estan a 1 minuto, luego ir a los que estan a 2 minutos y asi) y ver si esos edificios cumplen con la condicional de que _son mas grandes que el edificio desde donde partimos_ y que _no existe ningun otro edificio a la misma distancia o menos que sea mas grande_, cada vez que encontremos un caso que cumpla ambas condiciones anotaremos ese numero como el "edificio mas grande", contaremos el edificio y seguiremos la busqueda, no necesitamos verificaciones ni guardar la distancia porque como vamos avanzando siempre sabremos que existe un valor mas grande a menos distancia (puede parecer sentido comun pero tomo un vergonzoso tiempo llegar a esa conclusion) repetiremos esto hasta llegar al final de la ciudad por ambos lados, una vez hecho esto habremos visto todos los edificios de la ciudad y por ende habremos recorrido toda la ciudad. 

##### salida

una lista de N enteros con la cantidad de edificios que valen la pena estudiar. 

###### restricciones 

la unica restriccion que se encuentra es que los numeros sean positivos y que solo hayan numeros. 

## (D)iseño

![](Diagrama%20.png)

## (C)odificación
```py

n = int(input()) #cantidad de edificios en la ciudad
edificios = [int(i) for i in input().split(" ")]  #la altura de estos edificios
respuestas = [] #donde anotaremos todos las repuestas 
rspsts = ""

# con este for avanzaremos edificio a edificio
for i in range(n):
    respuesta = 0
    # estas 3 lineas separaran las listas en los edificios atras del 
    ant = edificios[:i] #separa la lista desde el inicio hasta el edificio i
    ant = ant[::-1] # invierte la lista para facilitar la lectura de datos 
    sig = edificios[i+1:] # los edificios desde i hasta el final 
    mejor_vista = edificios[i]# anotaremos el edificio desde el que partimos como el primero mas alto para que las matematicas funcionen
    
    # esto es un operador ternario, basicamente le entregas una premisa que puede ser verdadera o falsa y el ternario va a entregar una de las dos opciones 
    #con esto veremos la distancia maxima que abria que recorrer (con esto no nos preocuparemos por el largo de ambas listas)
    max_dist = len(ant) if  len(ant) > len(sig) else len(sig)  
    
    #ahora en este for podremos recorrer y contar los edificios.
    for j in range(max_dist):
        #creamos estas dos variables para evitar problemas y las hacemos numeros negativos para evitar problemas
        edi1 = -999
        edi2 = -999

        #esta ultima verificacion es para evitar el caso de que querramos ir a una posicion que ya esta 
        if j < len(ant):
            edi1 = ant[j]
        if j < len(sig):
            edi2 = sig[j] 

        #tomamos el edificio mas grande de entre los dos 
        mas_grande = edi1 if edi1 > edi2 else edi2

        #finalmente revisamos si ese numero es mas grande que el edificio
        if mas_grande > mejor_vista:
            mejor_vista = mas_grande
            respuesta = respuesta + 1
    
    #agregamos las respuestas a un string 
    rspsts +=str(respuesta)
    # si no es el ultimo elemento agregamos un espacio
    if i<n:
        rspsts += " "
#imprimimos la respuesta final
print(rspsts)


```
## (P)ruebas 
