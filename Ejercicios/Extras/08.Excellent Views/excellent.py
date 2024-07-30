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
