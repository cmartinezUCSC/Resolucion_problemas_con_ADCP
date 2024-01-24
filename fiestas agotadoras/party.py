D,C,R = [int(i) for i in input().split(" ")] #recibimos los datos
ago = [] #lista de actividades que agotan a william
rev = [] #lista de actividades que relajan a william
cant = 0 # la respuesta que buscamos 

for i in range(C): #guardamos las actividades en sus dos grupos
    ago.append(int(input()))

for i in range(R):
    rev.append(int(input()))

while(D>0 ): #esto pregunta escencialmente si nos queda energia para realizar alguna actividad
    print(str(D) + " " + str(ago) + " "+ str(rev))
    if ago: # vemos si queda alguna actividad agotante, de esta forma revisara automaticamente el tamaño, si no queda nada sera falso
        if(D>=ago[0]):
            cant+=1
            D-=ago[0]
            ago.pop(0)
        elif rev: #revisamos si podemos recuperar energia haciendo activides que relajen
            cant+=1
            D+=rev[0]
            rev.pop    
            pass
    elif rev: # si no quedan actividades agotantes, revisa si quedan actividades relajantes
        cant+=1
        rev.pop(0)
    else: # si no quedan actividades agotantes y relajantes terminamos el bucle
        break

print(cant)